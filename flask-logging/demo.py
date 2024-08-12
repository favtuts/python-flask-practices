#/usr/bin/env python3
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, request, jsonify, g, session
import uuid
import rfc3339
import time
import datetime
from time import strftime
import traceback

app = Flask(__name__)
app.secret_key = "c00de22a8b1e4daa2cabc8b3f82fdb753574293f8b673f9a"

@app.route("/")
def get_index():
    return "Welcome to Flask! "

@app.route("/data")
def get_hello():
    data = {
            "Name":"Ivan Leon",
            "Occupation":"Software Developer",
            "Technologies":"[Python, Flask, MySQL, Android]"
    }
    return jsonify(data)

@app.route("/update", methods=['POSt'])
def update_data():
    data = request.get_json()
    return jsonify(data)

@app.route("/error")
def get_json():
    # Intentional non existent variable.
    return non_existent_variable

@app.before_request
def log_request_info():
    
    ts = strftime('[%Y-%b-%d %H:%M]')
    # start timer
    g.start = time.time()
    request_id = str(uuid.uuid4())
    session["ctx"] = {"request_id": request_id}
    
    logger.debug('Start request: %s %s %s %s %s', ts, request.remote_addr,  request.method,  request.scheme,  request.full_path)
    logger.debug('Headers: %s', request.headers)
    logger.debug('Body: %s', request.get_data())

@app.after_request
def after_request(response):
    "Log HTTP request details"
    
    # Ignore logging for static files
    if (
        request.path == "/favicon.ico"
        or request.path.startswith("/static")
        or request.path.startswith("/admin/static")
    ):
        return response
    
    # This IF avoids the duplication of registry in the log,
    # since that 500 is already logged via @app.errorhandler.
    if response.status_code == 500:
        return response    
    
            
    now = time.time()
    duration = round(now - g.start, 6)  # to the microsecond
    ip_address = request.headers.get("X-Forwarded-For", request.remote_addr)
    host = request.host.split(":", 1)[0]
    params = dict(request.args)

    request_id = request.headers.get("X-Request-ID", "")

    log_params = {
        "method": request.method,
        "path": request.path,
        "status": response.status_code,
        "duration": duration,
        "ip": ip_address,
        "host": host,
        "params": params,
        "request_id": request_id,
    }

    print(log_params)

    # logger.error("request",  **log_params)
        
        
    ts = strftime('[%Y-%b-%d %H:%M]')
    logger.error('%s %s %s %s %s %s',
                    ts,
                    request.remote_addr,
                    request.method,
                    request.scheme,
                    request.full_path,
                    response.status)
    logger.debug('Body: %s', response.get_data())
    
    return response

@app.errorhandler(Exception)
def exceptions(e):
    ts = strftime('[%Y-%b-%d %H:%M]')
    tb = traceback.format_exc()
    logger.error('%s %s %s %s %s 5xx INTERNAL SERVER ERROR\n%s',
                  ts,
                  request.remote_addr,
                  request.method,
                  request.scheme,
                  request.full_path,
                  tb)
    return "Internal Server Error", 500

if __name__ == '__main__':
    # The maxBytes is set to this number, in order to demonstrate the generation of multiple log files (backupCount).
    handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=3)
    # getLogger('__name__') - decorators loggers to file / werkzeug loggers to stdout
    # getLogger('werkzeug') - werkzeug loggers to file / nothing to stdout
    logger = logging.getLogger('__name__')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    app.run(host="127.0.0.1",port=8000, debug=True)



### Ref:
# https://gist.github.com/jleei/1250be450aca00cd5fb14edb8a65d63b
# https://dev.to/rhymes/logging-flask-requests-with-colors-and-structure--7g1
### log ###
#
#    [2017-Aug-09 01:51] 127.0.0.1 GET http /? 200 OK
#    [2017-Aug-09 01:51] 127.0.0.1 GET http /data? 200 OK
#    [2017-Aug-09 01:51] 127.0.0.1 GET http /error? 5xx INTERNAL SERVER ERROR
#    Traceback (most recent call last):
#    File "/home/ivanlmj/git/env_flask_templates/lib/python3.4/site-packages/flask/app.py", 
#        line 1612, in full_dispatch_request
#    rv = self.dispatch_request()
#    File "/home/ivanlmj/git/env_flask_templates/lib/python3.4/site-packages/flask/app.py", 
#        line 1598, in dispatch_request
#    return self.view_functions[rule.endpoint](**req.view_args)
#    File "test.py", line 26, in get_json
#    return non_existent_variable # ---> intentional <---
#    NameError: name 'non_existent_variable' is not defined
#
###########

# Check it out: https://stackoverflow.com/questions/14037975/how-do-i-write-flasks-excellent-debug-log-message-to-a-file-in-production/39284642#39284642