from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random
import os

CHROME_EXECUTABLE = os.environ.get('CHROME_EXECUTABLE')

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

s=Service(CHROME_EXECUTABLE)
browser = webdriver.Chrome(service=s, options=chrome_options)

url='https://www.netflix.com/in/browse/genre/839338'

browser.get(url)
play = True

def randomseriespicker():
    ### picks a random series from the home page

    title = browser.find_elements(By.CSS_SELECTOR, "a.nm-collections-title.nm-collections-link")
    randomseriesnumber = random.randint(0,(len(title)-1))
    title[randomseriesnumber].click()

def playvideo():
    ### plays the video from the random page

    video = browser.find_elements(By.CSS_SELECTOR, "button.additional-video")
    if len(video) > 0:
        video[0].click()
    else:
        print("No free videos to watch")


randomseriespicker()
playvideo()