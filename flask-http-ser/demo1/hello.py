#!/usr/bin/python3
from flask import Flask
import json
app = Flask(__name__)

@app.route("/")
def hello_world():
    t = {}
    t['a'] = 1
    t['reply'] = 'hello'
    t['reply2'] = 'world'
    return json.dumps(t)

if __name__ == '__main__':
    app.run(debug=True)