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
url = 'https://www.inshorts.com/hi/read'
options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
# chrome_options.add_experimental_option('prefs', prefs)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)
browser.get(url)
time.sleep(2)

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
    full_path = 'project'+file_name+'.jpg'
    urllib.request.urlretrieve(imur[i],full_path)
    data.update({title[i]:content[i]})

# imgs = soup.findAll("div", {"class":"news-card-image"})
# for img in imgs:
#     print (img.a['href'].split("imgurl=")[1])

json_string = json.dumps(data)
# print(f"{json_string}")
json_string = json_string.strip("'\n''\'")
# print(json_string)
with open('scriptDataHi.json', 'w') as outfile:
    outfile.write(json_string)

with open('scriptDataHi.json') as json_file:
    data = json.load(json_file)
    print(data)
