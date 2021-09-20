import serial

def arduwrite(port,msg):
	error = None
	ser = serial.Serial(port,9600)
	try:
		ser.write(b'b')
	except:
		error = True
	ser.close()
	if error is None:
		print('msg sent!')
	else:
		print('msg not sent, exception occured!')