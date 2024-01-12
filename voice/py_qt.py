import sys
import datetime
import pyttsx3
import speech_recognition as sr
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie

class TextToSpeechApp(QWidget):
    def __init__(self):
        super().__init__()

        # Text-to-Speech Engine Initialization
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)  # Set a default voice (you can customize this)

        # Speech Recognition Initialization
        self.listener = sr.Recognizer()

        # GUI Components
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Voice-Controlled Text-to-Speech App')

        # Microphone Icon
        self.mic_label = QLabel()
        mic_pixmap = QPixmap('mic_icon.png').scaledToWidth(50)  # Replace 'mic_icon.png' with your microphone icon
        self.mic_label.setPixmap(mic_pixmap)
        self.mic_label.setAlignment(Qt.AlignTop) 
        
        # Speaker Icon with Animation
        self.speaker_label = QLabel()
        self.speaker_label.setMovie(QMovie('speaking_gif.gif'))  # Replace 'speaker_animation.gif' with your animated GIF
        self.speaker_label.setAlignment(Qt.AlignCenter)
        self.speaker_label.movie().start()

        # Listen Button
        self.listen_button = QPushButton('Listen and Speak')
        self.listen_button.clicked.connect(self.listen_and_speak)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.mic_label)
        layout.addWidget(self.speaker_label)
        layout.addWidget(self.listen_button)
        self.setLayout(layout)

        # Timer for updating the speaker animation
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_speaker_animation)
        self.timer.start(50)  # Update every 50 milliseconds

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen_and_speak(self):
        try:
            self.speak("Try speaking now")
            with sr.Microphone() as source:
                voice = self.listener.listen(source)
                command = self.listener.recognize_google(voice)
                command = command.lower()
                print(command)
                self.command_list(command)
        except sr.UnknownValueError:
            self.speak("Sorry, I couldn't understand that.")
        except sr.RequestError as e:
            self.speak(f"Error accessing the speech recognition service: {e}")

    def command_list(self, command):
        if "time" in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            self.speak(f"The time is {time}")
        if "date" in command:
            date = datetime.datetime.today().date()
            self.speak(f"Today is {date}")

    def update_speaker_animation(self):
        # Perform any updates or animations related to the speaker visual here
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = TextToSpeechApp()
    main_app.show()
    sys.exit(app.exec_())
