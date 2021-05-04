# encoding: utf-8
import json
from datetime import datetime

from flask import g, request
from flask_script import Manager

from project.app import create_app

app = create_app()

@app.before_request
def before_request_function():
    g.dateTimeStart = datetime.utcnow()
    g.endpoint = request.endpoint


@app.after_request
def after_request_function(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"
    response.method = g.endpoint

    return response

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
