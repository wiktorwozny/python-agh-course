from tkinter import *
from lab2.task.mqtt.mqttclient import MqttClient
from lab2.task.stt.stt import SttService


class Communicator(Tk):

    def __init__(self):
        self.client = MqttClient()
        self.stt = SttService()

        Tk.__init__(self)
        self.title("Communicator")
        self.geometry("500x300")

        self.create_buttons_frame()
        self.create_announcements_frame()

    def create_buttons_frame(self):
        self.buttons = Frame(self, highlightbackground="blue", highlightthickness=2, width=150, height=280)
        self.buttons.pack(side=LEFT, padx=10, pady=10)

        # RECORD BUTTON
        self.mic_img = PhotoImage(
            file="gui\imgs\\free-microphone-icon-342-thumb.png")
        self.record_button = Button(self.buttons, image=self.mic_img, command=self.record_mess)
        self.record_button.pack(side=TOP, pady=20, padx=50)

        self.record_btn_label = Label(self.buttons, text="record and send message", font=("Arial", 10))
        self.record_btn_label.pack(side=TOP)

        # MUTE BUTTON
        self.unmuted_img = PhotoImage(
            file="gui\imgs\icons8-audio-48.png")
        self.mute_button = Button(self.buttons, image=self.unmuted_img, command=self.mute_toggle)
        self.mute_button.pack(side=TOP, pady=20, padx=50)

        self.mute_btn_label = Label(self.buttons, text="mute/unmute listening \nfor announcements", font=("Arial", 10))
        self.mute_btn_label.pack(side=TOP)

    def create_announcements_frame(self):
        self.announcements = Frame(self, highlightbackground="red", highlightthickness=2, width=310, height=280)
        self.announcements.pack(side=RIGHT, padx=10, pady=10)

        # DISPLAYING ANNOUNCEMENTS
        self.ann_frame = Frame(self.announcements, highlightbackground="black", highlightthickness=1, width=310,
                               height=180)
        self.ann_frame.grid(row=1, column=0)
        self.ann_frame.pack(side=TOP)
        self.ann_frame.grid_propagate(False)

        self.title_label = Label(self.ann_frame, text="Current announcement:", font=("Arial", 15))
        self.title_label.pack(side=TOP, pady=10)
        self.title_label.grid(row=0, column=0)

        self.announcement_label = Label(self.ann_frame, text="", font=("Arial", 15))
        self.announcement_label.pack(side=TOP)
        self.announcement_label.grid(row=3, columnspan=3)

        # DISPLAYING WARNINGS
        self.warning_frame = Frame(self.announcements, highlightbackground="black", highlightthickness=1, width=310,
                               height=80)
        self.warning_frame.pack(side=TOP)

        self.warning_label = Label(self.warning_frame, text="", font=("Arial", 15))
        self.warning_label.pack(side=TOP)

    def record_mess(self):
        text = self.stt.listen()
        self.client.send("msg/mic", text)

    def mute_toggle(self):
        if self.client.tts.isActive:
            self.client.tts.isActive = False
            self.unmuted_img['file'] \
                = "gui\imgs\icons8-no-audio-48.png"
        else:
            self.client.tts.isActive = True
            self.unmuted_img['file'] \
                = "gui\imgs\icons8-audio-48.png"
            self.client.tts.say_all()




