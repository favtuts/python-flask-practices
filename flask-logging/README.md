# How to Get Started with Logging in Flask
* https://tuts.heomi.net/how-to-get-started-with-logging-in-flask/

# Prequisites

Create a new working directory and change into it with the command below:
```sh
$ mkdir flask-logging && cd flask-logging
```

Ensure to use Python3.10
```sh
$ python3 --version
Python 3.10.14
```

Install the Pipenv:
```sh
$ pip install --upgrade pip
$ pip install pipenv
```

Activate the virtual environment
```sh
$ pipenv shell
```

Get out of the virtual environment
```sh
$ deactivate
$ exit
```

Install the latest version of Flask
```sh
$ pipenv install Flask
```

# Getting started with logging in Flask

Create new Flask application
```sh
$ code app.py
```

Input script for [app.py](app.py)
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/info")
def info():
    return "Hello, World! (info)"

@app.route("/warning")
def warning():
    return "A warning message. (warning)"
```

Try to run the Flask application
```sh
$ flask run
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

Test these endpoints
```sh
$ curl http://127.0.0.1:5000/
$ curl http://127.0.0.1:5000/info
$ curl http://127.0.0.1:5000/warning
```