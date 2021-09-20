from flask import Flask,redirect,url_for
from arducom import arduwrite

app = Flask(__name__)

@app.route('/')
def index():
	return "Smart howse"

@app.route('/toggle')
def toggle():
	arduwrite('/dev/rfcomm0',b'b')
	return redirect(url_for('index'))