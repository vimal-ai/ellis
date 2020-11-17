"""
Import python packages
"""
import subprocess
from datetime import datetime
import os

import filePath
from Memory import Memory

import playsound
import speech_recognition as sr
from gtts import gTTS

import re
import pandas as pd
import pickle
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

"""
read model, word2vec and data file
"""
filename = './models/nlu.sav'
nlu = pickle.load(open(filename, 'rb'))
filename = './models/word2vec.sav'
word2vec = pickle.load(open(filename, 'rb'))
filename = './data/data.csv'
df = pd.read_csv(filename)

"""
create object of memory class
"""
m = Memory()

"""
main method for chatbot
"""
def chat(ip):
    test = []
    review = re.sub('[^a-zA-Z]', ' ', ip)
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review]
    review = ' '.join(review)
    test.append(review)

    x = word2vec.transform(test).toarray()

    ans = nlu.predict(x)

    m.push(ans[0])

    count = 0

    for i in range(0, 9):
        if m.store[9] == m.store[i]:
            count += 1
    output = ''
    if count >= len(df[df['id'] == ans[0]]['answer'].values):
        output = df[df['id'] == ans[0]]['answer'].values[len(df[df['id'] == ans[0]]['answer'].values) - 1]
    else:
        output = df[df['id'] == ans[0]]['answer'].values[count]

    if 'task' in ans[0]:
        temp = doTask(output)
        if type(temp) == str:
            output = temp
    speek(output)
    return output

"""
method for speek
"""
def speek(text):
    tts = gTTS(text= text, lang = "en")
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

"""
for automation in computer
"""
def doTask(output):
    """try except block: if file not found then program don't get crashed"""
    try:
        if 'firefox' in output:
            path = filePath.root_path + filePath.firefox
            os.system(path)

        elif 'terminal' in output:
            os.system(filePath.terminal)

        elif 'webcam' in output:
            path = filePath.root_path + filePath.webcam
            os.system(path)

        # elif 'calculator' in output:
        #     subprocess.call(filePath.calculator)
        #    os.system(path)

        # elif 'file manager' in output:
        #     subprocess.call(filePath.files)
        #    os.system(path)

        elif 'vs code' in output:
            path = filePath.root_path + filePath.vsCode
            os.system(path)

        elif 'pycharm' in output:
            path = filePath.root_path + filePath.pycharm
            os.system(path)

        elif 'anaconda navigator' in output:
            path = filePath.root_path + filePath.conda
            os.system(path)

        # elif 'text editor' in output:
        #     subprocess.call(filePath.text)
        #    os.system(path)

        elif 'discord' in output:
            path = filePath.root_path + filePath.discord
            os.system(path)
            #subprocess.call(filePath.discord)
        elif 'thunderbird' in output:
            path = filePath.root_path + filePath.email
            os.system(path)

        elif 'time' in output:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            return current_time
        else:
            pass
    except Exception as e:
        return str(e)
