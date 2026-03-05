<div align="center">
🐍 Higher Level Programming
Holberton School — Full Stack Track

From Python basics to databases, ORM, APIs and DOM manipulation
</div>

📌 What is this repo?
This repository contains all the projects completed during the Higher Level Programming curriculum at Holberton School France. It covers the full journey from Python fundamentals all the way to relational databases, REST APIs, and JavaScript front-end interaction.
Each folder is an independent project with its own objectives and constraints.

🗂️ Projects Overview
🐍 Python
Python is the core language of this curriculum. The projects go from the very basics to advanced OOP concepts.
ProjectWhat it coverspython-hello_worldPrint statements, strings, f-strings — the very first stepspython-if_else_loops_functionsConditionals, loops, defining and calling functionspython-import_modulesImporting modules, using __name__, command line argspython-data_structuresLists, tuples, how Python handles sequences under the hoodpython-more_data_structuresDictionaries, sets, lambda, map/filter/reducepython-exceptionsTry/except, raising exceptions, cleaning up with finallypython-test_driven_developmentWriting tests before code, docstrings, doctest and unittestpython-classesOOP basics — classes, instances, attributes, __init__, __del__python-more_classesClass vs instance attributes, __str__, __repr__, static & class methodspython-inheritanceInheritance, super(), isinstance, issubclass, mixinspython-abcAbstract Base Classes, interfaces in Python, pycodestylepython-input_outputReading/writing files, JSON serialization with json modulepython-serializationPickling, marshalling, converting between data formatspython-everything_is_objectHow Python handles objects in memory, mutability, references

💡 Key Python commands used across these projects:
pythonprint(f"Hello {name}")          # f-strings
with open("file.txt") as f:     # safe file handling
json.dumps(obj) / json.loads()  # serialization
class Dog(Animal):              # inheritance
    def __init__(self):
        super().__init__()
try:
    ...
except TypeError as e:          # exception handling
    print(e)


🗄️ SQL & Databases
Two projects focused on relational databases with MySQL — from raw SQL to Python ORM.
ProjectWhat it coversSQL_introductionCore SQL: CREATE, SELECT, INSERT, UPDATE, DELETE, GROUP BY, AVGSQL_more_queriesJOINs, subqueries, privileges, multiple tables, constraintspython-object_relational_mappingSQLAlchemy ORM — querying databases from Python without raw SQL

💡 Key SQL commands used across these projects:
sqlCREATE TABLE IF NOT EXISTS users (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256));
SELECT name, score FROM table WHERE score > 10 ORDER BY score DESC;
INSERT INTO table (name, score) VALUES ('John', 15);
UPDATE table SET score = 10 WHERE name = 'Bob';
DELETE FROM table WHERE score < 5;
SELECT AVG(score) AS average FROM table;
SELECT t1.name, t2.score FROM t1 JOIN t2 ON t1.id = t2.user_id;


🌐 JavaScript
Two projects covering JavaScript — first the language itself, then DOM manipulation in the browser.
ProjectWhat it coversjavascript-warm_upVariables, functions, loops, scoping, const/let, callbacksjavascript-dom_manipulationSelecting elements, handling events, fetching APIs, updating the DOM

💡 Key JS patterns used across these projects:
javascriptconst el = document.querySelector('#my-id');   // select element
el.addEventListener('click', () => { ... });   // handle event
el.textContent = 'Hello';                      // update content
fetch('https://api.example.com/data')          // call an API
  .then(res => res.json())
  .then(data => console.log(data));


🔌 REST API
ProjectWhat it coversrestful-apiBuilding and consuming REST APIs — HTTP methods, status codes, endpoints

🛠️ General Rules across all projects

✅ Python files use pycodestyle (PEP8 style)
✅ SQL keywords always in UPPERCASE
✅ Every file starts with a comment or docstring describing its purpose
✅ No hardcoded values that should be dynamic (ids, database names...)
✅ All files end with a new line

