import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename 

UPLOAD_FOLDER = 'D:\14-10-2023\Flaskapp\10\static'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'txt', 'pdf'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS