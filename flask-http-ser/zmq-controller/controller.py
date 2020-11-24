#!/usr/bin/python3
import socket, time, uuid, asyncio, select, sys, json, threading, struct, os
from flask import Flask, url_for, redirect, request
from werkzeug.utils import secure_filename
import zmq
import zhelpers

_POST = 'POST'
_GET = 'GET'

app = Flask(__name__)

@app.route("/")
def ctrl_index():
    return redirect("/welcome")

@app.route("/welcome")
def ctrl_get_welcome():
    return "welcome"

@app.route("/help", methods=[_GET, _POST])
def ctrl_help():
    if request.method == _POST:
        print("POST!")
        print(request.headers)
        print(request.form)
        data = request.data.decode('utf-8')
        print(type(data),data)
        try:
            jd = json.loads(data)
        except Exception as e:
            print('JSON loads', e)
        else:
            print(jd)

        # jd = json.loads(data)
        # print(jd)
        # jdata = json.loads(request.data.decode('utf-8'))
        # print(jdata)
    return "help"

@app.route("/scan", methods=[_GET, _POST])
def ctrl_scan():
    return "scan result"

if __name__ == "__main__":
    app.run(debug=True)