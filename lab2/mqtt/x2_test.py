#!/usr/bin/python3
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt

BROKER = "localhost"
# BROKER = "192.168.1.11"
# BROKER = "mqtt.lab.ii.agh.edu.pl"

################################################################################


def send(topic,payload):
  global client

  client.publish(topic,payload,retain=True) #publish
  # client.publish(topic,payload,retain=False) #publish


################################################################################

def on_message(client, userdata, message):

  topic = message.topic
  payload = str(message.payload.decode("utf-8"))

  print("rcv",topic,payload)


################################################################################


def init():
  global client

  # print("creating new instance")
  client = mqtt.Client("abc") #create new instance
  client.on_message=on_message #attach function to callback
  print("connecting to broker")
  client.connect(BROKER) #connect to broker
  client.loop_start() #start the loop
  client.subscribe([("ala/#",0),("ola/#",0)])


################################################################################

def loop():
  while True:
    x = input(">>")
    send("ula",x)

################################################################################

init()
loop()

################################################################################
