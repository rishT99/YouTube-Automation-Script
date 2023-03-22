import pyttsx3
# from gtts import gTTS

engine = pyttsx3.init(driverName='sapi5')
theText = "hello this will work?"

#Saving part starts from here 
# tts = gTTS(text=theText, lang='en')
# tts.save("saved_file.mp3")
# print("File saved!")

voices = engine.getProperty('voices')
for voice in voices:
    print(voice, voice.id)
    engine.setProperty('voice',voice.id,)
    engine.say(theText)
    engine.runAndWait()