'''
FIRST SETUP THE VIRTUAL ENVIORNMENT WITH THE HELP OF THE BELOW INSTUCTIONS:

Create a folder, we will call it Main
Make Main current working directory in terminal/command prompt
To open Main in vscode type                      code  .
To initialize the virtual enviroment type        python -m venv  .
To activate the virtual environment type         .\Scripts\activate.bat 
To Install Flask type                            pip install flask
To deactivate and exit the virtual environment   deactivate

After running the identity file in the Identity Directory we can now run this main file:
python main.py (NOTE: Make sure to Run the identity file first)
Open the browser at 127.0.0.1:8080
See the login.db file for the correct username & password
'''

from flask import Flask, render_template, redirect, url_for, session, request
import sqlite3
import requests
from datetime import timedelta

session_timeout = 30

app = Flask(__name__)
app.permanent_session_lifetime = timedelta(session_timeout)

app.secret_key = "#!!!secretkey!!!@"

identity_service = "http://localhost:8085"

def authenticate(username, password):
    #   1st parameter: URL of another server i.e. identity server
    #   2nd parameter: data = Data to be sent to the another server in the json Object/format 
    r = requests.post("{}/authenticate".format(identity_service), data = {
        "username" : username,
        "password" : password
    })
    return r.json() # Creates the json file recieved into a dictionary and returns it

@app.route('/',methods = ["GET"])
def login():
    if "username" in session:
        return redirect(url_for("user", name = session["username"]))
    if not ("try" in session):
        session["try"] = 0
    if session["try"] < 3:
        error = False
        if session["try"] > 0:
            error = True
        return render_template("login.html",error = error)
    return render_template(url_for("failure"))

@app.route('/authenticator', methods = ['POST'])
def authenticator():
    if "username" in session:
        return redirect(url_for("user",name = session["username"]))
    if "try" in session and session["try"] < 3:
        username = request.form.get('name')
        password = request.form.get('pass')
        res = authenticate(username, password)
        
        if res["isAuth"]:
            session["username"] = res["username"]
            session.pop("try")
            return redirect(url_for("user", name = res["username"]))
        
        session["try"] += 1
        return redirect(url_for("login", username = username))
    return redirect(url_for("login"))


@app.route('/user/<name>')
def user(name):
    if "username" in session:
        return render_template("success.html", name = name)
    return redirect(url_for("login"))

@app.route('/failure')
def failure():
    if "username" in session:
        return redirect(url_for("success.html", name = session["username"]))
    if "try" in session and session["try"] < 3:
        return redirect(url_for("login"))
    session.permanent = True
    return render_template("failure2.html", timeout = session_timeout)

@app.route('/logout')
def logout():
    if "username" in session:
        session.pop("username")
    return redirect(url_for("login"))
    
app.run(debug=True, port=8080)