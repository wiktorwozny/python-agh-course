import paho.mqtt.client as mqtt
from time import sleep
BROKER = "localhost"


class Publisher:

    def __init__(self):
        self.client = mqtt.Client("publisher")
        self.client.connect(BROKER)

    def send(self, topic, payload):
        self.client.publish(topic, payload, retain=True)
        sleep(3)
