# Doing some
import time
import requests
from bs4 import BeautifulSoup
from selenium import *
from selenium import webdriver
# from selenium import By
from selenium.webdriver.common.by import By
import json
import urllib.request
import os
save_pathi = 'A:/Docu/project/Stuffs/vi_images/'
save_pathc = 'A:/Docu/project/Stuffs/vi_content/'

print("Enter today on which topic we should create news")
ch = input("A. entertainment\nB. Normal\nC. Sports\nD. World\nE. Business\nX. Hatke\n: ")
if ch == "a" or ch == "A":
    url = 'https://www.inshorts.com/en/read/entertainment'
elif ch == "b" or ch == "B":
    url = 'https://www.inshorts.com/en/read'
elif ch == "c" or ch == "C":
    url = 'https://www.inshorts.com/en/read/sports'
elif ch == "d" or ch == "D":
    url = 'https://www.inshorts.com/en/read/world'
elif ch == "e" or ch == "E":
    url = 'https://www.inshorts.com/en/read/business'
elif ch == "x" or ch == "X":
    url = 'https://www.inshorts.com/en/read/hatke'
else:
    print("Sorry sahi choice to dall yaar!!")

options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
# chrome_options.add_experimental_option('prefs', prefs)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)
browser.get(url)
time.sleep(20)

url_req = requests.get(url)
soup = BeautifulSoup(url_req.content,'html.parser')

links = list()

title = list()
content = list()
imur = list()
data = {}
for i in range(5):

    news1=soup.find_all('div', class_=["news-card-title news-right-box"])[i]
    title.append(news1.find('span',attrs={'itemprop':"headline"}).string)
    news1=soup.find_all('div', class_=["news-card-content news-right-box"])[i]
    content.append(news1.find('div',attrs={'itemprop':"articleBody"}).string)
    news1=soup.find_all('div', class_=["news-card-image"])[i]
    imur.append(news1['style'].split("url('")[1][:-3])


for i in range(5):
    file_name = f"image{i}"
    full_path = save_pathi + 'project'+file_name+'.jpg'
    urllib.request.urlretrieve(imur[i],full_path)
    data.update({title[i]:content[i]})



json_string = json.dumps(data)
# print(f"{json_string}")
json_string = json_string.strip("'\n''\'")
# print(json_string)
with open(save_pathc + 'scriptData.json', 'w') as outfile:
    outfile.write(json_string)

with open(save_pathc + 'scriptData.json') as json_file:
    data = json.load(json_file)
    print(data)
