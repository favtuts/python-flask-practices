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