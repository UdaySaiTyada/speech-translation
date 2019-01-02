from translate import Translator
import os
import speech_recognition as sr
from gtts import gTTS
r = sr.Recognizer()
print('Say something in english')
with sr.Microphone() as source:
     audio = r.listen(source)
     text = r.recognize_google(audio)
     print(text)
translator= Translator(to_lang="hi")
translation = translator.translate(text)
hindi_audio = gTTS(text = translation, lang='hi')
hindi_audio.save('hindi_audio.mp3')
os.startfile('hindi_audio.mp3')
print(translation)
