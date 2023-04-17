import speech_recognition as sr


class SttService:

    def __init__(self):
        self.r = sr.Recognizer()

    def listen(self) -> str:
        with sr.Microphone() as source:
            print("listening ...")
            audio = self.r.listen(source)
            try:
                text = self.r.recognize_google(audio, language='pl_PL')
                print(text)
                return text
            except sr.UnknownValueError:
                print("can not understand :(")
            except sr.RequestError as e:
                print("error: ", e)


