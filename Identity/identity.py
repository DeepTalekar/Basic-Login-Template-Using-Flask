'''
FIRST SETUP THE VIRTUAL ENVIORNMENT WITH THE HELP OF THE BELOW INSTUCTIONS:

Create a folder, we will call it Identity
Make Identity current working directory in terminal/command prompt
To open Identity in vscode type                      code  .
To initialize the virtual enviroment type        python -m venv  .
To activate the virtual environment type         .\Scripts\activate.bat 
To Install Flask type                            pip install flask
To deactivate and exit the virtual environment   deactivate

Now after activating the .bat file we are now going to run this program with: 
python identity.py (Make sure to run db.py file before this file, if you are running this file for the first time)
'''
from flask import Flask, request
import sqlite3
import json

app = Flask(__name__)

db = []

@app.before_request
def init():
    global db
    db = sqlite3.connect("login.db", check_same_thread=False)

def get_user(username):
    cur = db.cursor()
    out = [row for row in cur.execute("SELECT * FROM users WHERE username = (?)",(username,))]
    if len(out) > 0:
        return {"username" : out[0][0], "password" : out[0][1]}
    return False

@app.route('/authenticate', methods = ['POST'])
def authenticate():
    username = request.form.get("username")
    password = request.form.get("password")
    record = get_user(username)
    if record:
        if password == record["password"]:
            # The Below statement Converts dict. into json Object/format
            return json.dumps({"username":record["username"], "isAuth" : True})
    return json.dumps({"isAuth" : False})

app.run(debug=True, port=8085)
