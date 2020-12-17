import speech_recognition as sr
from gtts import gTTS

# import playsound


"""
method for speek
"""


def speek(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


"""
get input from mic
"""


def getAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('0')
        audio = r.listen(source, timeout=2, phrase_time_limit=5)
        print('1')
        said = ""
        try:
            print('2')
            said = r.recognize_google(audio)
            print('3')
            return said
        except Exception as e:
            return str(e)
