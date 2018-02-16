#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 13:27:09 2018

@author: vicky
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time

#import time;
#from facepy import GraphAPI
#
#token = 'EAACEdEose0cBAFXg7joJVZCji3WWBZCxhWj3jywekBiJVUdz7ZAUugMqpJjzWSHlz1e8T5M0qVxtfjEh8UZB1TjgUO6ARAVNkqOS8iR5A1IaoJ3HaaqaVOTfnXKUJTvzasY2HiOXO6uNvAebfImX4Fmz1KCkoSeBV4OVhlbdMwCZAFhLe6gUvq8oqdlpOzyR9aYl4i09beAZDZD'
#
#graph=GraphAPI(token)
#friends_list= graph.get("me/friends?fields=birthday") 
#print (friends_list['data'])

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(chrome_options=chrome_options)

#browser = webdriver.Chrome()
browser.get('https://www.facebook.com/')

username = "YOUR USERNAME OR EMAIL-ID"
with open('test.txt', 'r') as myfile:  
    password = myfile.read().replace('\n', '')

print("Let's Begin")

element = browser.find_elements_by_xpath('//*[@id="email"]')
element[0].send_keys(username)

print("Username Entered")

element = browser.find_element_by_xpath('//*[@id="pass"]')
element.send_keys(password)

print("Password Entered")

log_in = browser.find_elements_by_id('loginbutton')
log_in[0].click()

print("Login Successfull")

browser.get('https://www.facebook.com/events/birthdays/')

feed = 'Happy Birthday!'

#//*[@class='enter_submit uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea inlineReplyTextArea mentionsTextarea textInput']/

element = browser.find_elements_by_xpath("//*[@class='enter_submit uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea inlineReplyTextArea mentionsTextarea textInput']")
cnt=0
for el in element:
    cnt+=1
    element_id = str(el.get_attribute('id'))
    #//*[@id="u_0_z"]
    XPATH = '//*[@id="'+element_id+'"]'
    post_field = browser.find_element_by_xpath(XPATH)
    post_field.send_keys(feed)
    post_field.send_keys(Keys.RETURN)
    print("Birthday Wish posted for friend"+str(cnt))
##element.clear()
##element = browser.find_element_by_xpath('.//*[@data-testid="status-attachment-mentions-input"]/div/div/div')
#post_wait = WebDriverWait(browser, 10)
#element = post_wait.until(EC.presence_of_element_located((By.CLASS_NAME, '_1p1v')))
#print("Page is ready!")
#element.send_keys(feed)
#element.send_keys(Keys.RETURN)
#post = browser.find_elements_by_xpath('.//*[@data-testid="react-composer-post-button"]')
#post.click()

time.sleep(5)
browser.close()

#761143670662908
#//*[@id="pass"]

#//*[@id="loginbutton"]
