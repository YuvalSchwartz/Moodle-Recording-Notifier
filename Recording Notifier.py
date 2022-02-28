from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from gtts import gTTS
from playsound import playsound
import pathlib
import os

#settings
path_of_chromedriver = "@@@@@"
username = "@@@@@"
password = "@@@@@"
course_link = "@@@@@"
teacher = "@@@@@"
text_when_uploaded = "The recording has been uploaded"

#web actions
driver = webdriver.Chrome(path_of_chromedriver)
driver.get(course_link)
driver.find_element_by_xpath("//form[@method='get']").click()
driver.find_element_by_xpath("//*[@id='username']").send_keys(username)
driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
driver.find_element_by_id("loginbtn").click()
while (driver.find_element_by_xpath("//*[@id='videoslist_table_r0_c4']").text) != teacher:
    time.sleep(5)
    driver.refresh()

#actions to do after done searching for recording
my_tts = gTTS(text=text_when_uploaded)
my_tts.save("recording.mp3")
playsound(str(pathlib.Path().resolve()) + "\\recording.mp3")
os.remove("recording.mp3")
driver.quit()