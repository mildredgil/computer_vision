#!/usr/bin/env python
# coding: utf-8
#Authors:
#Francisco Carlos Sanchez Ramirez   
#Mildred Irais Gil Melchor          
#Victor Sebastian Martínez Pérez    

import os 
import time
import math  
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import numpy as np
import requests
import cv2
from PIL import Image
from io import BytesIO

def setPath(parent, dir):
    # Path 
    path = os.path.join(parent, dir)
    
    try:
        os.makedirs(path) 
        print("Directory '%s' created" %dir) 
    except:
        print("Directory '%s' wasn't created" %dir) 

def deleteFolder(dir_path):
    try:
        os.rmdir(dir_path)
        print("Directory deleted successfully: %s" % (dir_path))
    except OSError as e:
        print("Error: %s : %s" % (dir_path, e.strerror))

def pathConfiguration(folder_name):
    main_dir = "C:\\Users\\mimit\\Documents\\computer vision\\HMW3\\"
    train_dir = folder_name + "\\train\\"
    test_dir = folder_name + "\\test\\"

    setPath(main_dir, folder_name)
    dir = main_dir + folder_name

    setPath(dir, "train")
    train_dir = main_dir + train_dir

    setPath(dir, "test")
    test_dir = main_dir + test_dir
    
    return train_dir, test_dir, dir

def getImagesUrl(driver, user_search, train_dir, test_dir, search_dir):
    BASE_URL = "http://www.image-net.org/"
    driver.get(BASE_URL + "search?q=" + user_search)

    #get first link from options
    try:
        link = driver.find_element_by_partial_link_text("Synset: ")
    except:
        print("No elements found for this search.")
        deleteFolder(train_dir)
        deleteFolder(test_dir)
        deleteFolder(search_dir)
        return []
    
    link.click()
    synset_url = driver.current_url
    wind = synset_url[synset_url.find("=") + 1:]

    #get url for the dataset 
    url_link = BASE_URL +"/api/text/imagenet.synset.geturls?wnid=" + wind
    driver.get(url_link)

    #get urls from page
    return driver.find_element_by_tag_name("pre").text.splitlines()

def donwloadImageNetImages(driver, user_search, train_dir, test_dir, search_dir):
    img_links = getImagesUrl(driver,user_search, train_dir, test_dir, search_dir)

    train_img_limit = math.floor(len(img_links) * 0.8)

    #download images from urls
    for link in img_links:
        img_name =  user_search + str(img_links.index(link))

        try:
            if img_links.index(link) <= train_img_limit: 
                urllib.request.urlretrieve(link, train_dir + img_name + ".jpg")
            else:
                urllib.request.urlretrieve(link, test_dir + img_name + ".jpg")
        except:
            print("can't download image " + str(img_links.index(link)) + " link " + link) 

def downloadImage(url, file_path):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    imgarr = np.asarray(img)
    fixedimg = cv2.cvtColor(imgarr, cv2.COLOR_RGB2BGR)
    cv2.imwrite(file_path, fixedimg)
    
def downloadShutterStockImages(driver, search_input, train_dir, test_dir, search_dir):
    driver.get('https://www.shutterstock.com/search/' + search_input + '?image_type=photo')
    try:
        aux = driver.find_element_by_class_name('b_ay_g').text
    except:
        print("No elements found for this search.")
        deleteFolder(train_dir)
        deleteFolder(test_dir)
        deleteFolder(search_dir)
        return 
    
    aux = aux.split()[1]
    total_results = int(aux.replace(',', ''))
    
    number_of_downloads = min(10, total_results)
    photos_downloaded = 0
    train_index = 0
    test_index = 0

    while photos_downloaded < number_of_downloads:
        button_div = driver.find_element_by_class_name('z_b_g')
        button = button_div.find_element_by_tag_name('a')
        body = driver.find_element_by_tag_name('body')
        for x in range(20):
            body.send_keys(Keys.PAGE_DOWN)
        imgs = driver.find_elements_by_css_selector('img.z_h_a.z_h_b')
        photos_downloaded += len(imgs)

        os.chdir(train_dir)
        for i in range(int(len(imgs)*0.8)):
            downloadImage(imgs[i].get_attribute('src'), search_input + str(train_index) + '.jpg')
            train_index = train_index + 1
            print(imgs[i].get_attribute('src'))

        os.chdir(test_dir)
        for i in range(int(len(imgs)*0.8), len(imgs)):
            downloadImage(imgs[i].get_attribute('src'), search_input + str(test_index) + '.jpg')
            test_index = test_index + 1
            print(imgs[i].get_attribute('src'))

        driver.get(button.get_attribute('href'))

driver = webdriver.Chrome('C:\webdrivers\chromedriver')
search_input = input("Which dataset you want to search? : \n")
website = ''

while website == '':
    website = input("Choose a siteweb to download images. Type 'I' for ImageNet or 'S' for shutterstock\n")
    if website == 'I':
        TRAIN_DIR, TEST_DIR, SEARCH_DIR = pathConfiguration(search_input)
        donwloadImageNetImages(driver, search_input, TRAIN_DIR, TEST_DIR, SEARCH_DIR)
    elif website == 'S':
        TRAIN_DIR, TEST_DIR, SEARCH_DIR = pathConfiguration(search_input)
        downloadShutterStockImages(driver, search_input, TRAIN_DIR, TEST_DIR, SEARCH_DIR)
    else:
        website = ''

driver.quit()

