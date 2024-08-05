from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/info")
def info():
    app.logger.info("Hello, World!")
    return "Hello, World! (info)"

@app.route("/warning")
def warning():
    app.logger.warning("A warning message.")
    return "A warning message. (warning)"