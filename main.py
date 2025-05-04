from kivy.app import App
from kivy.uix.label import Label
from voice.recognizer import recognize_uzbek
from intents.telegram import open_telegram
from intents.gpt_client import ask_gpt

class AzizaApp(App):
    def build(self):
        self.label = Label(text="Aziza tayyor!")
        self.listen_and_respond()
        return self.label

    def listen_and_respond(self):
        command = recognize_uzbek()
        if "telegram" in command:
            open_telegram()
        elif "salom aziza" in command:
            javob = ask_gpt("Salom")
            self.label.text = javob

if __name__ == "__main__":
    AzizaApp().run()
