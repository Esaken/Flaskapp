from flask import Flask  

import os
import random


app = Flask(__name__)

# Define the directory where images will be stored
IMAGE_DIR = './images'

# Define the route for uploading images
@app.route('/upload', methods=['POST'])
def upload():
    # Get the uploaded image file
    image_file = request.files['image']

    # Save the image file to the server
    image_file.save(os.path.join(IMAGE_DIR, image_file.filename))

    # Return a success message
    return 'Image uploaded successfully!'

# Define the route for visualizing images
@app.route('/view/<image_name>')
def view(image_name):
    # Check if the image file exists
    if not os.path.exists(os.path.join(IMAGE_DIR, image_name)):
        return 'Image not found!'

    # Open the image file and send it to the browser
    with open(os.path.join(IMAGE_DIR, image_name), 'rb') as f:
        image_data = f.read()

    return send_file(image_data, mimetype='image/jpeg')

# Define the route for downloading images
@app.route('/download/<image_name>')
def download(image_name):
    # Check if the image file exists
    if not os.path.exists(os.path.join(IMAGE_DIR, image_name)):
        return 'Image not found!'

    # Send the image file to the browser as an attachment
    return send_file(os.path.join(IMAGE_DIR, image_name), as_attachment=True)

# Define the route for the main page
@app.route('/')
def index():
    # Get a list of all the image files in the server directory
    image_files = os.listdir(IMAGE_DIR)

    # Return the HTML template for the main page
    return render_template('index.html', image_files=image_files)

if __name__ == '__main__':
    app.run(debug=True)