from moviepy import editor
from gtts import gTTS
from mutagen.mp3 import MP3
from PIL import Image
from pathlib import Path
import json
import os
from moviepy.editor import *
import pyttsx3;

with open('scriptDataHi.json') as json_file:
    data = json.load(json_file)
    print(data)
title = list()
content = list()
for key in data:
    title.append(key)
    content.append(data[key])
myText = "Hello kya ye chalega maybe"

#list index
li1 = 0
li2 = 1
li3 = 2
li4 = 3
li5 = 4
li6 = 5

titlePlay = "तो खबर का शीर्षक है कि| "
contentPlay = "तो खबर कह रही है कि| "

myText1 = titlePlay+title[li1]+contentPlay+content[li1]
print("********************************************************************************")
print(myText1)
myText2 = titlePlay+title[li2]+contentPlay+content[li2]
myText3 = titlePlay+title[li3]+contentPlay+content[li3]
myText4 = titlePlay+title[li4]+contentPlay+content[li4]
myText5 = titlePlay+title[li5]+contentPlay+content[li5]
#language is english as 'en' 
language = 'en'
introText = "हेलो दर्शकों मैं आपका डेली न्यूज बॉय हूं तो चलिए देखते हैं खबरें।"
outroText = "तो अभी के लिए बस इतना ही। देखने के लिए धन्यवाद! अधिक समाचारों के लिए उस लाइक और सब्सक्राइब बटन को दबाएं"
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices") 
engine.setProperty('voice', voices[3].id)
engine.setProperty("rate", 170)
# engine.save_to_file(introText, 'introVoiceHi.mp3')
# engine.save_to_file(outroText, 'outroVoiceHi.mp3')
engine.save_to_file(myText1, 'texttoS1.mp3')
engine.save_to_file(myText2, 'texttoS2.mp3')
engine.save_to_file(myText3, 'texttoS3.mp3')
engine.save_to_file(myText4, 'texttoS4.mp3')
engine.save_to_file(myText5, 'texttoS5.mp3')

# engine.save_to_file(text, filename)
engine.runAndWait() # don't forget to use this line



# the actual video path is 


path_images = Path('')

#basically it will take all png file 
images = list(path_images.glob('*.jpg'))

#and here image_list that will store list of images and then
image_list = list()
#but firstly it will resize them and then creates
for image_name in images:
   image = Image.open(image_name).resize((1080, 1920), Image.ANTIALIAS)
   image_list.append(image)
# video_clip = 
#from here just a few combining..... audio and those image that we are storing as gif
# image_list[0].save('temp.gif', save_all = True, append_images = image_list[1:],duration = 100000 )
image_list[li1].save('temp1.gif', save_all = True, duration = 10 )
image_list[li2].save('temp2.gif', save_all = True, duration = 10 )
image_list[li3].save('temp3.gif', save_all = True, duration = 10 )
image_list[li4].save('temp4.gif', save_all = True, duration = 10 )
image_list[li5].save('temp5.gif', save_all = True, duration = 10 )

# im = Image.open('in.gif').resize((1920, 1000), Image.ANTIALIAS)
# im.save('temp3.gif', save_all = True, duration = 10 )

video1 = editor.VideoFileClip('temp1.gif')
audio1 = editor.AudioFileClip('texttoS1.mp3')

video2 = editor.VideoFileClip('temp2.gif')
audio2 = editor.AudioFileClip('texttoS2.mp3')

video3 = editor.VideoFileClip('temp3.gif')
audio3 = editor.AudioFileClip('texttoS3.mp3')

video4 = editor.VideoFileClip('temp4.gif')
audio4 = editor.AudioFileClip('texttoS4.mp3')

video5 = editor.VideoFileClip('temp5.gif')
audio5 = editor.AudioFileClip('texttoS5.mp3')
# video3 = editor.VideoFileClip("temp3.gif") 
# audio3 = editor.AudioFileClip("introVoice.mp3")

final_video1 = video1.set_audio(audio1)
# final_video1.resize(1.5)

final_video1.write_videofile('texttoS1V.mp4', fps=180)


final_video2 = video2.set_audio(audio2)
# final_video2.resize(1.5)
final_video2.write_videofile('texttoS2V.mp4', fps=180)

final_video3 = video3.set_audio(audio3)
final_video3.write_videofile('texttoS3V.mp4', fps=180)

final_video4 = video4.set_audio(audio4)
final_video4.write_videofile('texttoS4V.mp4', fps=180)

final_video5 = video5.set_audio(audio5)
final_video5.write_videofile('texttoS5V.mp4', fps=180)


intro = VideoFileClip('introVideoHi.mp4')
# video3 = VideoFileClip("entry.mp4")
outro = VideoFileClip('outroVideoHi.mp4')
video1 = VideoFileClip("texttoS1V.mp4")
video2 = VideoFileClip("texttoS2V.mp4")
video3 = VideoFileClip("texttoS3V.mp4")
video4 = VideoFileClip("texttoS4V.mp4")
video5 = VideoFileClip("texttoS5V.mp4")



# video1 = video1.resize(0.10)
# video2 = video2.resize(0.10)
intro = intro.resize([1080, 1920])
outro = outro.resize([1080, 1920])
short1 = concatenate_videoclips([intro, video1, outro])
short2 = concatenate_videoclips([intro, video2, outro])
short3 = concatenate_videoclips([intro, video3, outro])
short4 = concatenate_videoclips([intro, video4, outro])
short5 = concatenate_videoclips([intro, video5, outro])
short1.write_videofile("short1.mp4")
short2.write_videofile("short2.mp4")
short3.write_videofile("short3.mp4")
short4.write_videofile("short4.mp4")
short5.write_videofile("short5.mp4")


size1 = video1.size
size2 = video2.size

print("size 1 is : ",size1)
print("size 2 is : ",size2)