"""
API Security and Authentication Implementation
"""

from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'votre_secret_key_super_securisee'  # À changer en production
auth = HTTPBasicAuth()
jwt = JWTManager(app)

"""
Base de données utilisateurs en mémoire
Stockage des mots de passe hachés avec werkzeug.security
"""
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

"""
Gestionnaire d'erreurs pour l'authentification Basic
Retourne une erreur 401 pour tous les échecs d'authentification
"""
@auth.error_handler
def auth_error(status):
    """Gère les erreurs d'authentification Basic"""
    return jsonify({"error": "Authentication required"}), status

"""
Vérification des identifiants pour l'authentification Basic
Compare le mot de passe fourni avec le hash stocké
"""
@auth.verify_password
def verify_password(username, password):
    """Vérifie le nom d'utilisateur et le mot de passe"""
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None

"""
Gestionnaires d'erreurs JWT personnalisés
Tous retournent une erreur 401 comme spécifié dans les instructions
"""
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Gère les requêtes sans token JWT"""
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Gère les tokens JWT invalides"""
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Gère les tokens JWT expirés"""
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Gère les tokens JWT révoqués"""
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Gère les tokens JWT nécessitant un rafraîchissement"""
    return jsonify({"error": "Fresh token required"}), 401

"""
Routes de l'API
"""

@app.route('/')
def home():
    """Route racine - accessible sans authentification"""
    return "Welcome to the Flask API!"

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """
    Route protégée par authentification Basic
    Retourne un message de succès si l'authentification est valide

    Expected Outputs:
        - Sans credentials: HTTP 401, {"error": "Authentication required"}
        - Avec credentials valides: HTTP 200, "Basic Auth: Access Granted"
    """
    return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    """
    Route de connexion pour l'authentification JWT
    Accepte un JSON avec username et password
    Retourne un token JWT si les identifiants sont valides

    Expected Outputs:
        - Credentiels valides: HTTP 200, {"access_token": "<JWT_TOKEN>"}
        - Credentiels invalides: HTTP 401, {"error": "Invalid credentials"}
    """
    if not request.is_json:
        return jsonify({"error": "JSON required"}), 400

    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    # Vérification des identifiants
    if username not in users or not check_password_hash(users[username]['password'], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Création du token JWT avec le rôle de l'utilisateur
    access_token = create_access_token(
        identity=username,
        additional_claims={"role": users[username]['role']}
    )
    return jsonify({"access_token": access_token})

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """
    Route protégée par JWT
    Retourne un message de succès si le token est valide

    Expected Outputs:
        - Sans token ou token invalide: HTTP 401, {"error": "Missing or invalid token"}
        - Avec token valide: HTTP 200, "JWT Auth: Access Granted"
    """
    return "JWT Auth: Access Granted"

@app.route('/admin-only')
@jwt_required()
def admin_only():
    """
    Route protégée par JWT avec contrôle de rôle
    Accessible seulement aux utilisateurs avec le rôle 'admin'
    Retourne une erreur 403 si l'utilisateur n'est pas admin

    Expected Outputs:
        - Token non-admin: HTTP 403, {"error": "Admin access required"}
        - Token admin: HTTP 200, "Admin Access: Granted"
    """
    current_user = get_jwt_identity()

    # Vérification du rôle de l'utilisateur
    if users[current_user]['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"

"""
Point d'entrée de l'application
Lance le serveur Flask sur le port 5001
"""
if __name__ == '__main__':
    app.run(port=5001, debug=True)
