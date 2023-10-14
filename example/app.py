
# an object of WSGI application 
from flask import Flask     
app = Flask(__name__)   # Flask constructor 
  
@app.route('/upload-image', methods=['GET', 'POST'])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
            return render_template("upload_image.html", uploaded_image=image.filename)
    return render_template("upload_image.html")


@app.route('/uploads/<filename>')
def send_uploaded_file(filename=''):
    from flask import send_from_directory
    return send_from_directory(app.config["IMAGE_UPLOADS"], filename)
  
  
  
  
  
  
if __name__=='__main__': 
   app.run() 
   