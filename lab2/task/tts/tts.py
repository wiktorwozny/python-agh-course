import pyttsx3 as tts


class TtsService:

    def __init__(self):
        self.isActive = True
        self.commands = []
        self.engine = tts.init()
        self.engine.setProperty('volume', 0.7)
        self.engine.setProperty('rate', 190)

    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def say_all(self):
        while self.commands:
            self.say(self.commands.pop(0))


