# Basic-Login-Template-Using-Flask
## Setting up the virtual environment with the help of the below instructions:

### Creating a Identity module

- This will help us to verify/identify the user from the database.

- This module interacts with the database alone.


> Create a folder, we will call it Identity
>
> Make Identity current working directory in terminal/command prompt

- To open Identity in vscode type                  `code  .`
- To initialize the virtual enviroment type        `python -m venv  .`
- To activate the virtual environment type         `.\Scripts\activate.bat`
- To Install Flask type                            `pip install flask`
- To deactivate and exit the virtual environment   `deactivate`

Now after activating the .bat file we are now going to run this program with: 

`python identity.py` 

**NOTE:** _Make sure to run **`db.py`** file before this file, if you are running this file for the first time_

> Create a folder, we will call it Main
>
> Make Main current working directory in terminal/command prompt
- To open Identity in vscode type                  `code  .`
- To initialize the virtual enviroment type        `python -m venv  .`
- To activate the virtual environment type         `.\Scripts\activate.bat`
- To Install Flask type                            `pip install flask`
- To deactivate and exit the virtual environment   `deactivate`

After running the identity file in the Identity Directory we can now run this main file:
python main.py 

**NOTE:** _Make sure to Run the **`identity.py`** file first_

> Open the browser at 127.0.0.1:8080

> **See the login.db file for the correct username & password**
