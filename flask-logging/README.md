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

# Logging to files

Send log records to local files on the server
```python
. . .
dictConfig(
    {
        "version": 1,
        . . .
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "default",
            },
            "file": {
                "class": "logging.FileHandler",
                "filename": "flask.log",
                "formatter": "default",
            },
        },
        "root": {"level": "DEBUG", "handlers": ["console", "file"]},
    }
)
. . .
@app.route("/")
def hello():

    app.logger.debug("A debug message")

    return "Hello, World!"

```

You can view its contents:
```sh
$ cat flask.log

[August 05, 2024 16:42:27 +07] INFO | _internal >>> WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
[August 05, 2024 16:42:27 +07] INFO | _internal >>> Press CTRL+C to quit
[August 05, 2024 16:43:04 +07] DEBUG | app >>> A debug message
[August 05, 2024 16:43:04 +07] INFO | app >>> An info message
[August 05, 2024 16:43:04 +07] WARNING | app >>> A warning message
[August 05, 2024 16:43:04 +07] ERROR | app >>> An error message
[August 05, 2024 16:43:04 +07] CRITICAL | app >>> A critical message
[August 05, 2024 16:43:04 +07] INFO | _internal >>> 127.0.0.1 - - [05/Aug/2024 16:43:04] "GET / HTTP/1.1" 200 -
```

# Rotating your log files

To rotate your log files, you can use either `RotatingFileHandler` or `TimedRotatingFileHandler`.

Example, using `RotatingFileHandler `:
```python
. . .

dictConfig(
    {
        "version": 1,
        . . .
        "handlers": {
            "size-rotate": {
                "class": "logging.handlers.RotatingFileHandler",
                "filename": "flask.log",
                "maxBytes": 1000000,
                "backupCount": 5,
                "formatter": "default",
            },
        },
        "root": {"level": "DEBUG", "handlers": ["size-rotate"]},
    }
)
. . .

```

Example using `TimedRotatingFileHandler `:

```python
. . .

dictConfig(
    {
        "version": 1,
        . . .
        "handlers": {
            "time-rotate": {
                "class": "logging.handlers.TimedRotatingFileHandler",
                "filename": "flask.log",
                "when": "D",
                "interval": 10,
                "backupCount": 5,
                "formatter": "default",
            },
        },
        "root": {
            "level": "DEBUG",
            "handlers": ["time-rotate"],
        },
    }
)
. . .

```

# Logging HTTP requests

Can use sessions to store the request_id, and for the sessions to be secure, you need to create a secret key for your application.
```python
from flask import session
import uuid

. . .

app = Flask(__name__)

app.secret_key = "<secret_key>"


@app.route("/")
def home():

    session["ctx"] = {"request_id": str(uuid.uuid4())}

    app.logger.info("A user visited the home page >>> %s", session["ctx"])

    return render_template("home.html")

```

Beside the sessions, you can attach more object into the log:
```python
. . .
    # Pass the search query to the Nominatim API to get a location
    location = requests.get(
        "https://nominatim.openstreetmap.org/search",
        {"q": query, "format": "json", "limit": "1"},
    ).json()

    # If a location is found, pass the coordinate to the Time API to get the current time
    if location:

        app.logger.info(
            "A location is found. | location: %s >>> %s", location, session["ctx"]
        )
```

You can also log something about the response as well by using `@app.after_request` decorator:
```python
. . .
@app.after_request
def logAfterRequest(response):

    app.logger.info(
        "path: %s | method: %s | status: %s | size: %s >>> %s",
        request.path,
        request.method,
        response.status,
        response.content_length,
        session["ctx"],
    )

    return response

```


# Working with multiple loggers

We can create more loggers than the `root` logger:
```python
from flask import Flask
from logging.config import dictConfig
import logging

dictConfig(
    {
        "version": 1,
        "formatters": {
            . . .
        },
        "handlers": {
            . . .
        },
        "root": {"level": "DEBUG", "handlers": ["console"]},

        "loggers": {
            "extra": {
                "level": "INFO",
                "handlers": ["time-rotate"],
                "propagate": False,
            }
        },
    }
)

root = logging.getLogger("root")
extra = logging.getLogger("extra")

app = Flask(__name__)


@app.route("/")
def hello():

    root.debug("A debug message")
    root.info("An info message")
    root.warning("A warning message")
    root.error("An error message")
    root.critical("A critical message")

    extra.debug("A debug message")
    extra.info("An info message")
    extra.warning("A warning message")
    extra.error("An error message")
    extra.critical("A critical message")

    return "Hello, World!"

```