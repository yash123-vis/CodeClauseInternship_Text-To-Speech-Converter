from tkinter import *
from gtts import gTTS
import pygame
import tempfile
import os

root = Tk()
root.geometry('600x400')
root.resizable(0, 0)
root.config(bg='#2c3e50')
root.title('Text to Speech Converter')

pygame.mixer.init()

Label(root, text='Text to Speech Converter', font='Helvetica 20 bold', bg='#2c3e50', fg='white').pack(pady=10)
Label(root, text='Enter Text:', font='Helvetica 15 italic', bg='#2c3e50', fg='white').place(x=20, y=60)

Msg = StringVar()
entry_field = Entry(root, textvariable=Msg, width=50, font='Helvetica 12')
entry_field.place(x=20, y=100)

Label(root, text='Select Voice:', font='Helvetica 12 italic', bg='#2c3e50', fg='white').place(x=20, y=140)
voice_option = StringVar(value='en')
OptionMenu(root, voice_option, 'en', 'en-uk', 'en-au', 'en-ca', 'en-in').place(x=120, y=135)

Label(root, text='Speech Rate:', font='Helvetica 12 italic', bg='#2c3e50', fg='white').place(x=20, y=180)
rate_scale = Scale(root, from_=0.5, to=2.0, orient=HORIZONTAL, resolution=0.1, bg='#2c3e50', fg='white', troughcolor='#ecf0f1')
rate_scale.set(1.0)
rate_scale.place(x=120, y=170)

def Text_to_speech():
    Message = entry_field.get()
    voice = voice_option.get()
    rate = rate_scale.get()
    if Message:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_file:
            filename = temp_file.name
        speech = gTTS(text=Message, lang=voice, slow=rate < 1.0)
        speech.save(filename)
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        def cleanup():
            if os.path.exists(filename):
                os.remove(filename)
        root.after(int(len(Message) / rate * 1000), cleanup)
    else:
        Label(root, text='Please enter some text', font='Helvetica 12 italic', bg='#2c3e50', fg='red').place(x=20, y=230)

def Exit():
    root.destroy()

def Reset():
    Msg.set("")
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()

button_style = {
    'font': 'Helvetica 12 bold',
    'bg': '#ecf0f1',
    'fg': '#2c3e50',
    'bd': 0,
    'activebackground': '#bdc3c7',
    'activeforeground': '#2c3e50',
    'relief': 'flat'
}

Button(root, text="PLAY", command=Text_to_speech, **button_style).place(x=25, y=270, width=100, height=40)
Button(root, text='EXIT', command=Exit, **button_style).place(x=250, y=270, width=100, height=40)
Button(root, text='RESET', command=Reset, **button_style).place(x=475, y=270, width=100, height=40)

root.mainloop()
