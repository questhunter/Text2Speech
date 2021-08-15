import pyttsx3
from tkinter import *

# gui window properties
tkWindow = Tk()
tkWindow.geometry('460x400')
tkWindow.title('Text2Speech')


engine = pyttsx3.init()  # pyttsx3 initialization
voices = engine.getProperty('voices')  # voice selection
engine.setProperty('voice', voices[1].id)  # voice selection


rate = engine.getProperty('rate')  # speech rate
engine.setProperty('rate', 140)  # speech rate


def speak(audio_string):
    engine.say(audio_string)  # text to speech
    engine.runAndWait()


def get_input():
    # get the entire text from text area
    stringInput = text_space.get("1.0", "end-1c")
    speak(stringInput)


font_name = ('calibre', 10, 'normal')
text_space = Text(tkWindow, height=20, width=60, font=font_name)  # text area
text_space.pack(pady=16)


speak_button = Button(tkWindow, text='Speak',
                      command=get_input, width=10, fg='#ffffff', bg='#808080')  # button
speak_button.pack()

tkWindow.resizable(False, False)
tkWindow.mainloop()
