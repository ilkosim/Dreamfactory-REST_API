import json
import unirest
import binascii
import os
import serial
import time

# Get authenticated and grab the session id

response = unirest.post("http://localhost/api/v2/system/admin/session",
headers = {"Content-Type": "application/json"},
params=json.dumps({ "email": "ilko_sim@mail.bg", "password": "Pass4admin"}))
session_id=json.loads(response.raw_body) ["session_id"]

print "Successfully authenticated with DreamFactory:" + session_id

while 1:
   	ser = serial.Serial('/dev/ttyAMA0', 9600)
	response = unirest.get("http://localhost/api/v2/db/_table/RTW/6",
	headers = {"Content-Type": "application/json", "X-DreamFactory-Session-Token": session_id}, params= {})
	SensorValue_6=json.loads(response.raw_body) ["SensorValue"]
	#print "raw_body:"+ str(response.raw_body)
	print "Successfully authenticated with DreamFactory:" + str(SensorValue_6)
	response = unirest.get("http://localhost/api/v2/db/_table/RTW/7",
	headers = {"Content-Type": "application/json", "X-DreamFactory-Session-Token": session_id}, params= {})
	SensorValue_7=json.loads(response.raw_body) ["SensorValue"]
	#print "raw_body:"+ str(response.raw_body)
	print "Successfully authenticated with DreamFactory:" + str(SensorValue_7)
	Slider=str(SensorValue_6)
	Button=str(SensorValue_7)
	a=[Slider,Button]
	print a
	ser.write("a")
	#ser = serial.Serial('/dev/ttyAMA0', 9600)
#	ser.write(Slider)
# 	print ser.write(Slider)
#	print ser.readline()
#  	ser.write(Button)
#  	print ser.write(Button) 
	
