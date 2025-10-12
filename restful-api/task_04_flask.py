from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/status')
def get_status():
    return jsonify({"status": "OK"})

@app.route('/users/<username>')
def get_user(username):
    user_data = users.get(username)
    if user_data:
        return jsonify(user_data)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/data')
def get_data():
    list_usernames = list(users.keys())
    return jsonify(list_usernames)

@app.route('/add_user', methods=['POST'])
def add_user():
    if not request.is_json:
        return jsonify({"error": "Data must be in JSON format"}), 415
    
    user_data = request.get_json()
    
    if 'username' not in user_data:
        return jsonify({"error": "'username' field is required"}), 400
    
    username = user_data['username']
    
    users[username] = user_data
    
    return jsonify({
        "message": "User added successfully",
        "user": user_data
    }), 201

if __name__ == "__main__":
    app.run(port=5001, debug=True)
