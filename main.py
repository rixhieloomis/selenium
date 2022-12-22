from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random
import os
import time


os.environ["CHROME_EXECUTABLE"] = <<path-to-your-executable>>
CHROME_EXECUTABLE = os.environ.get('CHROME_EXECUTABLE')

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

s=Service(CHROME_EXECUTABLE)
browser = webdriver.Chrome(service=s, options=chrome_options)

def randomseriespicker():
    """picks a random series from the home page"""
    url = 'https://www.netflix.com/in/browse/genre/839338'
    browser.get(url)

    title = browser.find_elements(By.CSS_SELECTOR, "a.nm-collections-title.nm-collections-link")
    randomseriesnumber = random.randint(0, (len(title) - 1))
    title[randomseriesnumber].click()


def playvideo():
    """ plays the video from the random page """

    video = browser.find_elements(By.CSS_SELECTOR, "button.additional-video")
    if len(video) > 0:
        starcast = browser.find_element(By.CSS_SELECTOR, "span.title-data-info-item-list")
        star = starcast.text.split(",")
        print(f"The Star-cast of the movie is {star[0]}")

        description = browser.find_element(By.CSS_SELECTOR, "div.title-info-synopsis")
        print(f"The description follows '{description.text}'")

        video[0].click()
        return True

    else:
        print("Loading a new video")
        return False

play = True
i = 0

while play:
    randomseriespicker()
    if playvideo():
        time.sleep(10)
        videoplaying = float(browser.find_element(By.TAG_NAME, "video").get_attribute("currentTime"))
        if videoplaying > 0 and i < 2:
            print("Video is running")
            play = False
        else:
            if i > 2:
                play = False
                print("Try again")
            else:
                print("Video is not loading, trying a new video")
                play = True
    else:
        play = True











