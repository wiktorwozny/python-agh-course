import paho.mqtt.client as mqtt
from lab2.task.tts.tts import TtsService

BROKER = "localhost"


class Subscriber:

    def __init__(self):
        self.tts = TtsService()
        self.client = mqtt.Client("subscriber")
        self.client.on_message = self.on_message
        self.client.connect(BROKER)
        self.client.subscribe([("msg/spk/+", 0), ("msg/mic/+", 0)])
        self.client.loop_start()

    def on_message(self, client, userdata, message):
        topic = message.topic
        print(topic)
        payload = str(message.payload.decode("utf-8"))

        print("rcv", topic, payload)

        if topic == "msg/spk":
            if self.tts.isActive:
                self.tts.say(payload)
            else:
                self.tts.commands.append(payload)




