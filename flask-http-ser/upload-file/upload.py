#!/usr/bin/python3
import os
from flask import Flask, request, redirect, url_for
from flask import send_from_directory

# UPLOAD_FOLDER = '/path/to/the/uploads'
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'down')
# UPLOAD_FOLDER = './down'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


repHtml =  '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file webkitdirectory directory>
         <input type=submit value=Upload>
    </form>
'''

# repHtml =  '''
#     <!doctype html>
#     <title>Upload new File</title>
#     <h1>Upload new File</h1>
#     <form action="" method=post enctype=multipart/form-data>
#       <p><input type=file name=file accept=image/jpeg>
#          <input type=submit value=Upload>
#     </form>
#     '''

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    print(request)
    if request.method == 'POST':
        # print(type(request.files), request.files)
        
        # file = request.files['file']
        files = [f for f in request.files.getlist('file') if allowed_file(f.filename)]
        print('amount of files:', len(files))
        for file in files:
            # if file and allowed_file(file.filename):
            filename = file.filename.split('/')[-1]
                # filename = secure_filename(file.filename)
                # print("save file ", filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                # return redirect(url_for('uploaded_file',filename=filename))
    return repHtml
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
