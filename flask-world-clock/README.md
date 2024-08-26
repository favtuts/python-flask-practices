# Flask World Clock

A world clock application built to demonstrate logging in Flask.

**Tutorial**: [How to Start Logging with Flask](https://tuts.heomi.net/how-to-get-started-with-logging-in-flask/).

![Flask World Clock](screenshot.png)


Typing "Ha noi" and click on Submit button, you can see the Clock information

![Ha noi Clock](world-clock-hanoi.png)

## 🟢 Prerequisites

You must have the latest version of [Python 3](https://www.python.org) installed on your machine. This project is tested against Python 3.10.0.

## 📦 Getting started

- Clone this repo to your machine:

  ```bash
  git clone https://github.com/favtuts/python-flask-practices.git
  ```

- `cd` into the project directory:

  ```bash
  cd flask-world-clock
  ```

- Install Python virtual environment:

  ```bash
  python3 -m venv env
  ```

- Activate the virtual environment.

  On Windows, run:

  ```bash
  env\Scripts\activate
  ```

  On Unix or macOS, run:

  ```bash
  source env/bin/activate
  ```

- Install the requirements:

  ```bash
  python -m pip install -r requirements.txt
  ```

- Start the dev server:

  ```bash
  flask run
  ```

You should see the following output if the dev server is started successfully:

```text
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

## ⚖ License

The code used in this project and in the linked tutorial are licensed under the [Apache License, Version 2.0](LICENSE).


# Creating a logging system

Setting up the configurations:
```python
from logging.config import dictConfig

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] [%(levelname)s | %(module)s] %(message)s",
                "datefmt": "%B %d, %Y %H:%M:%S %Z",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
            },
            "file": {
                "class": "logging.FileHandler",
                "filename": "worldClock.log",
                "formatter": "default",
            },
            "logtail": {
                "class": "logtail.LogtailHandler",
                "source_token": "qU73jvQjZrNFHimZo4miLdxF",
                "formatter": "default",
            },
        },
        "root": {"level": "DEBUG", "handlers": ["console", "file", "logtail"]},
    }
)


app = Flask(__name__)

app.secret_key = "<secret_key>"
```

Make sure you put the configurations before you declare the Flask application (`app = Flask(__name__)`). This example uses [sessions](https://flask.palletsprojects.com/en/2.2.x/api/?highlight=session#flask.session) to store the `request_id`, and for the sessions to be secure, you need to create a secret key for your application.

```python
@app.route("/")
def home():

    session["ctx"] = {"request_id": str(uuid.uuid4())}
    ...
    
```

