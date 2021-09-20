from flask import Flask,redirect,url_for
import serial
import atexit
#from arducom import arduwrite

ser = serial.Serial('COM9',9600)
app = Flask(__name__)

@app.route('/')
def index():
	return "Smart howse"

@app.route('/toggle')
def toggle():
	ser.write(b'b')
	return redirect(url_for('index'))

def onExit():
        ser.close()
        print("serial conn closed, exiting app...")

atexit.register(onExit)
