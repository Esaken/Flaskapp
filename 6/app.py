from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
   
    return render_template('upload_form.html')


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' in request.files:
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # Here you should save the file
            # file.save(path_to_save_file)
            return 'File uploaded successfully'

    return 'File upload failed'


from werkzeug.utils import secure_filename
secure_filename = secure_filename(file.filename)


app.config['UPLOAD_FOLDER'] = './upload'

import os
file.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename))


from werkzeug.exceptions import RequestEntityTooLarge

@app.errorhandler(RequestEntityTooLarge)
def file_too_large(e):
    return 'File is too large', 413

 #return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(debug=True)