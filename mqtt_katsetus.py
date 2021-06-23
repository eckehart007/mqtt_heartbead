#!/usr/bin/python3

import paho.mqtt.client as paho
import time

broker="192.168.0.19"
port=1883

def on_publish(client,userdata,result):             #create function for callback
    print("Heartbeat: " + str(result) +"\n")
client1= paho.Client("control1")                           #create client object
client1.on_publish = on_publish                          #assign function to callback
client1.connect(broker,port)                                 #establish connection
heartbeat = 0
while True:
    ret= client1.publish("heartbeat", str(heartbeat))                   #publish
    heartbeat = heartbeat + 1
    time.sleep(1)