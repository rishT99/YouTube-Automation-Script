#Text to speech and then to video
from moviepy import editor
from gtts import gTTS
from mutagen.mp3 import MP3
from PIL import Image
from pathlib import Path
import json
import os
from moviepy.editor import *
import pyttsx3;

save_patha = 'A:/Docu/project/Stuffs/vi_audio/'
save_pathv = 'A:/Docu/project/Stuffs/vi_video/'
save_pathc = 'A:/Docu/project/Stuffs/vi_content/'
save_pathi = 'A:/Docu/project/Stuffs/vi_images/'
save_pathf = 'A:/Docu/project/Stuffs/vi_final/'



# engine = pyttsx3.init();
# engine.say("hello Rishabh how are you ")
# voices = engine.getProperty('voices')
# for voice in voices:
#    engine.setProperty('voice', voice.id)  # changes the voice
#    print(voice.id)
#    print(voice)
#    engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()
#here's my text
with open(save_pathc + 'scriptData.json') as json_file:
    data = json.load(json_file)
    # print(data)
title = list()
content = list()
for key in data:
    title.append(key)
    content.append(data[key])
myText = "Hello my self Rishabh Tiwari. kya ye chalega maybe"

#list index
li1 = 0
li2 = 1
li3 = 2
li4 = 3
li5 = 4
li6 = 5 

# for i in range(5):
#     myText += "so the title is "+title[i]+"Now content is "+content[i]
myText1 = ". so the title is. "+title[li1]+". So new is saying. "+content[li1]
myText2 = "so the title is. "+title[li2]+". So news is saying. "+content[li2]
myText3 = "so the title is. "+title[li3]+". So news is saying. "+content[li3]
myText4 = "so the title is. "+title[li4]+". So news is saying. "+content[li4]
myText5 = "so the title is. "+title[li5]+". So news is saying. "+content[li5]

#language is english as 'en' 
language = 'en'
# introText = "Hello viewers i am your Daily news boy so let's see news."
# outroText = "So that was for now guys hit that like and subscribe button for more news thanks for watching! "
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices") 
engine.setProperty('voice', voices[4].id)
engine.setProperty("rate", 170)
# engine.save_to_file(introText, 'introVoice.mp3')
# engine.save_to_file(outroText, 'outroVoice.mp3')
engine.save_to_file(myText1, save_patha + ' texttoS1.mp3')
engine.save_to_file(myText2, save_patha + ' texttoS2.mp3')
engine.save_to_file(myText3, save_patha + ' texttoS3.mp3')
engine.save_to_file(myText4, save_patha + ' texttoS4.mp3')
engine.save_to_file(myText5, save_patha + ' texttoS5.mp3')

# engine.save_to_file(text, filename)
engine.runAndWait() # don't forget to use this line



# the actual video path is 


path_images = Path(save_pathi)

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
image_list[li1].save(save_pathi + 'temp1.gif', save_all = True, duration = 10 )
image_list[li2].save(save_pathi + 'temp2.gif', save_all = True, duration = 10 )
image_list[li3].save(save_pathi + 'temp3.gif', save_all = True, duration = 10 )
image_list[li4].save(save_pathi + 'temp4.gif', save_all = True, duration = 10 )
image_list[li5].save(save_pathi + 'temp5.gif', save_all = True, duration = 10 )

# im = Image.open('in.gif').resize((1920, 1000), Image.ANTIALIAS)
# im.save('temp3.gif', save_all = True, duration = 10 )

video1 = editor.VideoFileClip(save_pathi + 'temp1.gif')
audio1 = editor.AudioFileClip(save_patha +' texttoS1.mp3')

video2 = editor.VideoFileClip(save_pathi + 'temp2.gif')
audio2 = editor.AudioFileClip(save_patha +' texttoS2.mp3')

video3 = editor.VideoFileClip(save_pathi + 'temp3.gif')
audio3 = editor.AudioFileClip(save_patha +' texttoS3.mp3')

video4 = editor.VideoFileClip(save_pathi + 'temp4.gif')
audio4 = editor.AudioFileClip(save_patha +' texttoS4.mp3')

video5 = editor.VideoFileClip(save_pathi + 'temp5.gif')
audio5 = editor.AudioFileClip(save_patha +' texttoS5.mp3')
# video3 = editor.VideoFileClip("temp3.gif") 
# audio3 = editor.AudioFileClip("introVoice.mp3")

final_video1 = video1.set_audio(audio1)
# final_video1.resize(1.5)

final_video1.write_videofile(save_pathv +' texttoS1V.mp4', fps=20)


final_video2 = video2.set_audio(audio2)
# final_video2.resize(1.5)
final_video2.write_videofile(save_pathv +' texttoS2V.mp4', fps=20)

final_video3 = video3.set_audio(audio3)
final_video3.write_videofile(save_pathv +' texttoS3V.mp4', fps=20)

final_video4 = video4.set_audio(audio4)
final_video4.write_videofile(save_pathv +' texttoS4V.mp4', fps=20)

final_video5 = video5.set_audio(audio5)
final_video5.write_videofile(save_pathv +' texttoS5V.mp4', fps=20)


# final_video3 = video3.set_audio(audio3)
# # final_video1.resize(1.5)

# final_video3.write_videofile('entry.mp4', fps=20)

# video1 = VideoFileClip("texttoS1V.mp4")
# video2 = VideoFileClip("texttoS2V.mp4")




# video1 = video1.resize(1.5)
# video2 = video2.resize(1.5)

# video1.write_videofile("short1.mp4")
# video2.write_videofile("short2.mp4")
# os.system("mpg321 texttoS1.mp3")
# os.system("mpg321 texttoS2.mp3")

intro = VideoFileClip(save_pathv +'introVideoo.mp4')
# video3 = VideoFileClip("entry.mp4")
outro = VideoFileClip(save_pathv +'outroVideoo.mp4')
video1 = VideoFileClip(save_pathv +" texttoS1V.mp4")
video2 = VideoFileClip(save_pathv +" texttoS2V.mp4")
video3 = VideoFileClip(save_pathv +" texttoS3V.mp4")
video4 = VideoFileClip(save_pathv +" texttoS4V.mp4")
video5 = VideoFileClip(save_pathv +" texttoS5V.mp4")



# video1 = video1.resize(0.10)
# video2 = video2.resize(0.10)
intro = intro.resize([1080, 1920])
outro = outro.resize([1080, 1920])
short1 = concatenate_videoclips([intro, video1, outro])
short2 = concatenate_videoclips([intro, video2, outro])
short3 = concatenate_videoclips([intro, video3, outro])
short4 = concatenate_videoclips([intro, video4, outro])
short5 = concatenate_videoclips([intro, video5, outro])
short1.write_videofile(save_pathf +"  short1.mp4")
short2.write_videofile(save_pathf +"  short2.mp4")
short3.write_videofile(save_pathf +"  short3.mp4")
short4.write_videofile(save_pathf +"  short4.mp4")
short5.write_videofile(save_pathf +" short5.mp4")


size1 = video1.size
size2 = video2.size

print("size 1 is : ",size1)
print("size 2 is : ",size2)
# video1.ipython_display(width = 420)


# concatenating both the clips
# final = concatenate_videoclips([intro, video1, video2, outro])
#writing the video into a file / saving the combined video
# final.write_videofile("merged.mp4")

# this also works darling...

#before this was this alll 


# #so here creating 
# myObj1 = gTTS(text = myText1, lang = language, slow = False)
# myObj2 = gTTS(text = myText2, lang = language, slow = False)

# #offcourse saving bro....
# myObj1.save("texttoS1.mp3")
# myObj2.save("texttoS2.mp3")

# # ok this works bro....


# #uhhh so from here start's for video
# song1 = MP3('texttoS1.mp3')
# song2 = MP3('texttoS2.mp3')
# length1 = song1.info.length
# length2 = song2.info.length

# path_images = Path('')

# #basically it will take all png file 
# images = list(path_images.glob('*.jpg'))

# #and here image_list that will store list of images and then
# image_list = list()
# #but firstly it will resize them and then creates
# for image_name in images:
#    image = Image.open(image_name).resize((1920, 1000), Image.ANTIALIAS)
#    image_list.append(image)
# # video_clip = 
# #from here just a few combining..... audio and those image that we are storing as gif
# # image_list[0].save('temp.gif', save_all = True, append_images = image_list[1:],duration = 100000 )
# image_list[0].save('temp1.gif', save_all = True, duration = 10 )
# image_list[1].save('temp2.gif', save_all = True, duration = 10 )

# video1 = editor.VideoFileClip('temp1.gif')
# audio1 = editor.AudioFileClip('texttoS1.mp3')

# video2 = editor.VideoFileClip('temp2.gif')
# audio2 = editor.AudioFileClip('texttoS2.mp3')

# final_video1 = video1.set_audio(audio1)
# final_video1.write_videofile('texttoS1V.mp4', fps=20)

# final_video2 = video2.set_audio(audio2)
# final_video2.write_videofile('texttoS2V.mp4', fps=20)

# # os.system("mpg321 texttoS1.mp3")
# # os.system("mpg321 texttoS2.mp3")

# intro = VideoFileClip('introVideoo.mp4')
# outro = VideoFileClip('outroVideoo.mp4')
# video1 = VideoFileClip("texttoS1V.mp4")
# video2 = VideoFileClip("texttoS2V.mp4")


# video1 = video1.resize(0.10)
# video2 = video2.resize(0.10)

# short1 = concatenate_videoclips([intro, video1, outro])
# short2 = concatenate_videoclips([intro, video2, outro])

# short1.write_videofile("short1.mp4")
# short2.write_videofile("short2.mp4")


# # concatenating both the clips
# final = concatenate_videoclips([intro, video1, video2, video3, video4, video5, outro])
# #writing the video into a file / saving the combined video
# final.write_videofile(save_pathf + "merged.mp4")

# # this also works darling...



