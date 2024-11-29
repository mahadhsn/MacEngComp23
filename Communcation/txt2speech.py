import pyttsx3

text_speech = pyttsx3.init()

voices = text_speech.getProperty('voices')
text_speech.setProperty('voices', voices[1].id)


answer = input("enter input: ")
text_speech.say(answer)
text_speech.runAndWait()

