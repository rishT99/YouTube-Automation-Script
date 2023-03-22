from moviepy.editor import *
from moviepy import editor
from gtts import gTTS
from mutagen.mp3 import MP3
from PIL import Image
from pathlib import Path
import audioread


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
image_list[0].save('temp1.gif', save_all = True, duration = 10 )
image_list[1].save('temp2.gif', save_all = True, duration = 10 )
# im = Image.open('in.gif').resize((1920, 1000), Image.ANTIALIAS)
# im.save('temp3.gif', save_all = True, duration = 10 )

video1 = editor.VideoFileClip('temp1.gif')
audio1 = editor.AudioFileClip('texttoS1.mp3')

video2 = editor.VideoFileClip('temp2.gif')
audio2 = editor.AudioFileClip('texttoS2.mp3')

# video3 = editor.VideoFileClip("temp3.gif") 
# audio3 = editor.AudioFileClip("introVoice.mp3")

final_video1 = video1.set_audio(audio1)
# final_video1.resize(1.5)

final_video1.write_videofile('texttoS1V.mp4', fps=20)


final_video2 = video2.set_audio(audio2)
# final_video2.resize(1.5)
final_video2.write_videofile('texttoS2V.mp4', fps=20)



intro = VideoFileClip('introVideoo.mp4')
# video3 = VideoFileClip("entry.mp4")
outro = VideoFileClip('outroVideoo.mp4')
video1 = VideoFileClip("texttoS1V.mp4")
video2 = VideoFileClip("texttoS2V.mp4")


# video2 = video2.resize(0.10)
intro = intro.resize([1080, 1920])
outro = outro.resize([1080, 1920])
short1 = concatenate_videoclips([intro, video1, outro])
short2 = concatenate_videoclips([intro, video2, outro])

short1.write_videofile("short1.mp4")
short2.write_videofile("short2.mp4")

size1 = video1.size
size2 = video2.size

print("size 1 is : ",size1)
print("size 2 is : ",size2)
# video1.ipython_display(width = 420)


# # concatenating both the clips
# final = concatenate_videoclips([intro, video1, video2, outro])
# #writing the video into a file / saving the combined video
# final.write_videofile("merged.mp4")

# this also works darling...



