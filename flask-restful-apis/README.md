# Developing RESTful APIs with Python and Flask

Let's learn how to develop RESTful APIs with Python and Flask.


# Bootstrapping a Flask Application

We will need to install [Python 3](https://docs.python.org/3/), [Pip (Python Package Index)](https://pypi.python.org/pypi/pip), and [Flask](http://flask.pocoo.org/).

## Installing Python 3

```sh
$ pyenv versions
$ pyenv install --list
$ pyenv install 3.8.19
$ pyenv global 3.8.19
$ python --version
Python 3.8.19
$ python3 --version
Python 3.8.19
```

## Installing Pip

```sh
$ pip --version
pip 23.0.1 from /home/tvt/.pyenv/versions/3.8.19/lib/python3.8/site-packages/pip (python 3.8)
```

You can make sure that pip is up-to-date by running:
```sh
$ python3 -m pip install --upgrade pip
$ python3 -m pip --version
pip 24.1.2 from /home/tvt/.pyenv/versions/3.8.19/lib/python3.8/site-packages/pip (python 3.8)
```

## Virtual environments (virtualenv)

* `pip` as the tool for installing Python packages globally, making it hard to manage multiple versions of the same package on the same machine. It's true that `pip` supports package management through the [requirements.txt](https://pip.pypa.io/en/stable/user_guide/#requirements-files) file
* `requirements.txt`  need all dependencies and sub-dependencies listed explicitly, a manual process that is tedious and error-prone.

We are going to use [Pipenv which is a dependency manager](https://github.com/kennethreitz/pipenv) that isolates projects in private environments, allowing packages to be installed per project

```sh
$ pip install pipenv
$ pipenv --version
pipenv, version 2024.0.1
```

We will use pipenv to start our project and manage our dependencies
```sh
# use pipenv to create a Python 3 (--three) virtualenv for our project
# $ pipenv --three
# $ pipenv install --three
$ pipenv --python 3.8

Creating a virtualenv for this project...
Pipfile: /home/tvt/techspace/python/python-flask-practices/flask-restful-apis/Pipfile
Using /home/tvt/.pyenv/versions/3.8.19/bin/python (3.8.19) to create virtualenv...
⠧ Creating virtual environment...created virtual environment CPython3.8.19.final.0-64 in 1174ms
  creator CPython3Posix(dest=/home/tvt/.local/share/virtualenvs/flask-restful-apis-vUa4VgeR, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/tvt/.local/share/virtualenv)
    added seed packages: pip==24.1, setuptools==70.1.0, wheel==0.43.0
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

✔ Successfully created virtual environment!
Virtualenv location: /home/tvt/.local/share/virtualenvs/flask-restful-apis-vUa4VgeR
Creating a Pipfile for this project...
```

Then install Flask app
```sh
# install flask a dependency on our project
$ pipenv install flask
```

Activate the environment
```sh
$ pipenv shell
. /home/tvt/.local/share/virtualenvs/flask-restful-apis-vUa4VgeR/bin/activate
(flask-restful-apis) tvt@TVTLAP:~/flask-restful-apis$ 
```

Create a file named `hello.py`, in the status bar of VS Code, you need to select right Python interpreter

![select_interpreter](./images/flask-restful-apis-select-python-interpreter.png)

Add 5 lines of code:
```python
# hello.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"
```

To run it, we execute the following command:
```sh
$ flask --app hello run
```

After executing these commands, we can reach our application by opening a browser and navigating to `http://127.0.0.1:5000/` or by issuing `curl http://127.0.0.1:5000/`.
```sh
$ curl http://127.0.0.1:5000/
Hello, World!
```

## Python modules

Similar to Java packages and C# namespaces, [modules in Python](https://docs.python.org/3/tutorial/modules.html) are files organized in directories that other Python scripts can import. To create a module on a Python application, we need to create a folder and add an empty file called `__init__.py`

Let's create our first main module on our application. Let's create the directory `cashman`. The root directory will hold metadata about our project, like dependencies.
```sh
# create source code's root
mkdir cashman && cd cashman

# create an empty __init__.py file
touch __init__.py
```

Inside the main module, let's create a script called `index.py`. In this script, we will define the first endpoint of our application.
```py
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"
```

Let's create an executable file called `bootstrap.sh` in the root directory of our application.
```sh
# move to the root directory
cd ..

# create the file
touch bootstrap.sh

# make it executable
chmod +x bootstrap.sh
```

The goal of this file is to facilitate the start-up of our application. Its source code will be the following:
```sh
#!/bin/sh
# Defines the main script to be executed by Flask
export FLASK_APP=./cashman/index.py
# Runs our Flask app in the context of the virtual environment listening to all interfaces on the computer (-h 0.0.0.0)
pipenv run flask --debug run -h 0.0.0.0
```

Note: we are setting flask to run in debug mode to enhance our development experience and activate the hot reload feature, so we don't have to restart the server each time we change the code.

Run the script 
```sh
$ ./bootstrap.sh
Courtesy Notice: Pipenv found itself running within a virtual environment, so it will automatically use that environment, instead of creating its own for any project. You can set PIPENV_IGNORE_VIRTUALENVS=1 to force pipenv to ignore that environment and create its own instead. You can set PIPENV_VERBOSITY=-1 to suppress this warning.
 * Serving Flask app './cashman/index.py'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.29.248.234:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 226-427-834
```

Now we can invoke the Hello World endpoint
```sh
$ curl http://127.0.0.1:5000/
Hello, World!
```