import uuid
from flask import Flask, request, session
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

app.secret_key = "c00de22a8b1e4daa2cabc8b3f82fdb753574293f8b673f9a"

@app.route("/")
def hello():
    
    session["ctx"] = {"request_id": str(uuid.uuid4())}
    
    app.logger.debug("A debug message")
    app.logger.info("An info message")
    app.logger.warning("A warning message")
    app.logger.error("An error message")
    app.logger.critical("A critical message")
    
    app.logger.info("A user visisted the home page >>> %s", session["ctx"])
    
    return "Hello, World!"

@app.route("/info")
def info():
    
    session["ctx"] = {"request_id": str(uuid.uuid4())}
    
    app.logger.info("Hello, World! >>> %s", session["ctx"])
    return "Hello, World! (info)"

@app.route("/warning")
def warning():
    
    session["ctx"] = {"request_id": str(uuid.uuid4())}
    
    app.logger.warning("A warning message. >>> %s", session["ctx"])
    return "A warning message. (warning)"

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