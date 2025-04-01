import json
import unirest
import binascii
import os
import serial
import time
data=""
# Get authenticated and grab the session id

response = unirest.post("http://localhost/api/v2/system/admin/session",
headers = {"Content-Type": "application/json"},
params=json.dumps({ "email": "ilko_sim@mail.bg", "password": "Pass4admin"}))
session_id=json.loads(response.raw_body) ["session_id"]

print "Successfully authenticated with DreamFactory:" + session_id

while 1:
  try:
    ser = serial.Serial('/dev/ttyAMA0', 9600)
    #if ser.inWaiting():
    data=ser.readline().split(',')
    time.sleep(.25)
    #ser.flushInput()
    #ser.flushOutput()
  except Exception, e:
    print "Error ", e
    continue
  if len(data)==7: #and data[0] !=0: 
#     ser.flushInput()
#     ser.flushOutput()
     for sensorid in range(5):
          Rec={}
          Rec["RoomID"] = data[0]
          Rec["DeviceID"] = data[1]
          Rec["SensorID"] = sensorid
          Rec["SensorValue"] = data[sensorid+2].rstrip()

          if (sensorid==0):
               Rec["SensorType"] = "Humidity"
               Rec["SensorUnit"] = "Percentage"
          if (sensorid==1):
               Rec["SensorType"] = "Temperature"
               Rec["SensorUnit"] = "Celsius"
          if (sensorid==2):
               Rec["SensorType"] = "Potentiometer"
               Rec["SensorUnit"] = "Scale"
          if (sensorid==3):
               Rec["SensorType"] = "PM 2,5"
               Rec["SensorUnit"] = "mg-m3"
          if (sensorid==4):
               Rec["SensorType"] = "PM 10"
               Rec["SensorUnit"] = "mg-m3"


          Rec["Date"] = time.strftime("%Y-%m-%d")
          Rec["Time"] = time.strftime("%H:%M:%S")

          print "RoomID - " + str(Rec["RoomID"])
          print "DeviceID -" + str(Rec["DeviceID"])
          print "SensorID - " + str(Rec["SensorID"])
          print "SensorValue - " + str (Rec["SensorValue"])
          print "SensorType - " + str(Rec["SensorType"])
          print "Time - " + str(Rec["Time"])
          print  "Date - " + str(Rec["Date"])

          # Ingest data from sensor
          if (sensorid==0):
               response = unirest.patch("http://localhost/api/v2/db/_table/RTW/1",
               headers = {"Content-Type": "application/json", "X-DreamFactory-Session-Token": session_id},
               params=json.dumps({'SensorID': Rec["SensorID"], 'SensorType': Rec["SensorType"], 'SensorValue': Rec["SensorValue"], 'Date': Rec["Date"], 'Time': Rec["Time"]}), auth = (), callback = None) 
          if (sensorid==1):
               response = unirest.patch("http://localhost/api/v2/db/_table/RTW/2",
               headers = {"Content-Type": "application/json", "X-DreamFactory-Session-Token": session_id},
               params=json.dumps({'SensorID': Rec["SensorID"], 'SensorType': Rec["SensorType"], 'SensorValue': Rec["SensorValue"], 'Date': Rec["Date"], 'Time': Rec["Time"]}), auth = (), callback = None)
          if (sensorid==2):
               response = unirest.patch("http://localhost/api/v2/db/_table/RTW/3",
               headers = {"Content-Type": "application/json", "X-DreamFactory-Session-Token": session_id},
               params=json.dumps({'SensorID': Rec["SensorID"], 'SensorType': Rec["SensorType"], 'SensorValue': Rec["SensorValue"], 'Date': Rec["Date"], 'Time': Rec["Time"]}), auth = (), callback = None)
          if (sensorid==3):
               response = unirest.patch("http://localhost/api/v2/db/_table/RTW/4",
               headers = {"Content-Type": "application/json", "X-DreamFactory-Session-Token": session_id},
               params=json.dumps({'SensorID': Rec["SensorID"], 'SensorType': Rec["SensorType"], 'SensorValue': Rec["SensorValue"], 'Date': Rec["Date"], 'Time': Rec["Time"]}), auth = (), callback = None)
          if (sensorid==4):
               response = unirest.patch("http://localhost/api/v2/db/_table/RTW/5",
               headers = {"Content-Type": "application/json", "X-DreamFactory-Session-Token": session_id},
               params=json.dumps({'SensorID': Rec["SensorID"], 'SensorType': Rec["SensorType"], 'SensorValue': Rec["SensorValue"], 'Date': Rec["Date"], 'Time': Rec["Time"]}), auth = (), callback = None)
	  print "Added sensor data as of " + time.strftime("%H:%M:%S")
          response = unirest.post("http://localhost/api/v2/system/admin/session",
          headers = {"Content-Type": "application/json"},
          params=json.dumps({ "email": "ilko_sim@mail.bg", "password": "Pass4admin"}))
          session_id=json.loads(response.raw_body) ["session_id"]

     #ser.flushInput()
     #ser.flushOutput()
     #time.sleep(1)
     #time.sleep(60)
