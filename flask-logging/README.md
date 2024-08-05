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
$ flask --debug run
 * Debug mode: one
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


Now add logging calls to the `info()` and `warning()` functions
```python
@app.route("/info")
def info():
    app.logger.info("Hello, World!")
    return "Hello, World! (info)"


@app.route("/warning")
def warning():
    app.logger.warning("A warning message.")
    return "A warning message. (warning)"
```

Now test again:
```sh
$ curl http://127.0.0.1:5000/warning
```

You can see in the Terminal the log record with timestamp:
```sh
[2024-08-05 16:13:13,592] WARNING in app: A warning message.
127.0.0.1 - - [05/Aug/2024 16:13:13] "GET /warning HTTP/1.1" 200 -
```


# Understanding log levels

Flask offers six differentlog levels, each associated with an integer value: `CRITICAL`(50), `ERROR`(40), `WARNING`(30), `INFO`(20) and `DEBUG`(10).


# Configuring your logging system

Flask recommends that you use the `logging.config.dictConfig()` method to overwrite the default configurations
```python
from flask import Flask
from logging.config import dictConfig

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "default",
            }
        },
        "root": {"level": "DEBUG", "handlers": ["console"]},
    }
)

app = Flask(__name__)

. . .
```

# Formatting your log records

```python
. . .

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s | %(module)s >>> %(message)s",
            }
        },
        . . .
    }
)

. . .

@app.route("/")
def hello():
    app.logger.info("An info message")
    return "Hello, World!"
```

You can customize how the timestamp is displayed by adding a `datefmt` key in the configurations:
```python
. . .

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s | %(module)s >>> %(message)s",
                "datefmt": "%B %d, %Y %H:%M:%S %Z",
            }
        },
        . . .
    }
)

. . .

```