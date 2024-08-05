from flask import Flask
from logging.config import dictConfig


dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s | %(module)s >>> %(message)s",
                "datefmt": "%B %d, %Y %H:%M:%S %Z",
            }
        },
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
            "size-rotate": {
                "class": "logging.handlers.RotatingFileHandler",
                "filename": "logs/flask-size-rotate.log",
                "maxBytes": 1000000,
                "backupCount": 5,
                "formatter": "default",
            },
            "time-rotate": {
                "class": "logging.handlers.TimedRotatingFileHandler",
                "filename": "logs/flask-time-rotate.log",
                "when": "D",
                "interval": 10,
                "backupCount": 5,
                "formatter": "default",
            },
        },
        "root": {"level": "DEBUG", "handlers": ["console", "file", "size-rotate", "time-rotate"]},
    }
)

app = Flask(__name__)

@app.route("/")
def hello():
    
    app.logger.debug("A debug message")
    app.logger.info("An info message")
    app.logger.warning("A warning message")
    app.logger.error("An error message")
    app.logger.critical("A critical message")
    
    return "Hello, World!"

@app.route("/info")
def info():
    app.logger.info("Hello, World!")
    return "Hello, World! (info)"

@app.route("/warning")
def warning():
    app.logger.warning("A warning message.")
    return "A warning message. (warning)"