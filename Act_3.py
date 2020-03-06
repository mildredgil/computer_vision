#!/usr/bin/env python
# coding: utf-8

# In[9]:


import os 
import time
import math  
from selenium import webdriver
import urllib.request

def setPath(parent, dir):
    # Path 
    path = os.path.join(parent, dir)
    
    try:
        os.makedirs(path) 
        print("Directory '%s' created" %dir) 
    except:
        print("Directory '%s' wasn't created" %dir) 
        

def getImagesUrl(user_search):
    BASE_URL = "http://www.image-net.org/"

    driver = webdriver.Chrome('C:\webdrivers\chromedriver')
    driver.get(BASE_URL + "search?q=" + user_search)

    #get first link from options
    link = driver.find_element_by_partial_link_text("Synset: ")
    link.click()
    synset_url = driver.current_url
    wind = synset_url[synset_url.find("=") + 1:]

    #get url for the dataset 
    url_link = BASE_URL +"/api/text/imagenet.synset.geturls?wnid=" + wind
    driver.get(url_link)

    #get urls from page
    return driver.find_element_by_tag_name("pre").text.splitlines()

user_search = input("Which dataset you want to get? : \n")

MAIN_DIR = "C:\\Users\\mimit\\Documents\\computer vision\\HMW3\\"
TRAIN_DIR = user_search + "\\train\\"
TEST_DIR = user_search + "\\test\\"

setPath(MAIN_DIR, user_search)
DIR = MAIN_DIR + user_search

setPath(DIR, "train")
TRAIN_DIR = MAIN_DIR + TRAIN_DIR

setPath(DIR, "test")
TEST_DIR = MAIN_DIR + TEST_DIR

img_links = getImagesUrl(user_search)

train_img_limit = math.floor(len(img_links) * 0.8)

#download images from urls
for link in img_links:
    img_name =  user_search + str(img_links.index(link))
    
    try:
        if img_links.index(link) <= train_img_limit: 
            urllib.request.urlretrieve(link, TRAIN_DIR + img_name + ".jpg")
        else:
            urllib.request.urlretrieve(link, TEST_DIR + img_name + ".jpg")
    except:
        print("can't download image " + str(img_links.index(link)) + " link " + link) 

