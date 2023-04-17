import paho.mqtt.client as mqtt
from lab2.task.tts.tts import TtsService
from time import sleep
BROKER = "127.0.0.1"


class MqttClient:

    def __init__(self):
        self.tts = TtsService()
        self.client = mqtt.Client("client")
        self.client.on_message = self.on_message
        self.client.connect(BROKER, 1883, 60)
        self.client.subscribe("msg/spk/#")
        self.client.loop_start()

    def send(self, topic, payload):
        self.client.publish(topic, payload)
        sleep(3)

    def on_message(self, client, userdata, message):
        topic = message.topic
        payload = str(message.payload.decode("utf-8"))

        print("rcv", topic, payload)

        if topic == "msg/spk":
            if self.tts.isActive:
                self.tts.say(payload)
            else:
                self.tts.commands.append(payload)

