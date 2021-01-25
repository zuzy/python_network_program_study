#!/usr/bin/python3
import os
from flask import Flask, request, redirect, url_for
from flask import send_from_directory
import uuid
import time

_POST = 'POST'
_GET = 'GET'

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'image')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UID'] = None
app.config['UID-index'] = 0

repDirectory =  '''
    <!doctype html>
    <title>Upload Directory</title>
    <h1>Upload jpgs in side Directory</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file webkitdirectory directory>
         <input type=submit value=Upload>
    </form>
'''

repFile =  '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload Loadable File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file accept=image/jpeg>
         <input type=submit value=Upload>
    </form>
    '''

def _jpg():
    j = ['J', 'j']
    p = ['P', 'p']
    g = ['G', 'g']
    return  tuple(_j + _p + _g for _j in j for _p in p for _g in g)
ALLOWED_EXTENSIONS = _jpg()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def _upload_file(files, more = False):
    # username = request.cookies.get('username')
    # uid = request.cookies.get('uid')
    uid = app.config['UID'] if app.config['UID'] is not None \
        else str(uuid.uuid1(clock_seq=int(time.time())))
    path = os.path.join(app.config['UPLOAD_FOLDER'], uid, str(app.config['UID-index']))
    print('path')
    try:
        os.makedirs(path)
    except FileExistsError:
        pass
    except Exception as e:
        print(e)
        exit(1)

    for file in files:
        if file and allowed_file(file.filename):
            filename = file.filename.split('/')[-1]
            print("save file ", filename)
            file.save(os.path.join(path, filename))

    if more == False:
        app.config['UID-index'] = 0
        app.config['UID'] = None
    else:
        app.config['UID-index'] += 1
    return uid

@app.route('/images', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        files = request.files.getlist('file')
        return _upload_file(files)
    return repDirectory

@app.route('/imagesMore', methods=['GET', 'POST'])
def upload_file_more():
    if request.method == 'POST':
        files = request.files.getlist('file')
        return _upload_file(files, more=True)
    return repDirectory
