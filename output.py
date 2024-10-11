import pyttsx3

engine = pyttsx3.init()
engine.setProperty('voice', 'com.apple.voice.compact.uk-UA.Lesya')

def say(text):
    engine.say(text)