from distutils.log import debug 
from fileinput import filename 
from flask import *
from gevent.pywsgi import WSGIServer

app = Flask(__name__) 

@app.route('/') 
def main(): 
	return render_template("index.html") 

@app.route('/success', methods = ['POST']) 
def success(): 
	if request.method == 'POST': 
		f = request.files['file'] 
		f.save(f.filename) 
		return render_template("Acknowledgement.html", name = f.filename) 

        if __name__ == '__main__':
        # Debug/Development
        # app.run(debug=True, host="0.0.0.0", port="5000")
        # Production
        http_server = WSGIServer(('', 5000), app)
        http_server.serve_forever()
