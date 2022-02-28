from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyttsx3

#settings
path_of_chromedriver = "@@@@@"
username = "@@@@@"
password = "@@@@@"
course_link = "@@@@@"
teacher = "@@@@@"
text_when_uploaded = "@@@@@"

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
engine = pyttsx3.init()
engine.setProperty('rate',130)
engine.say(text_when_uploaded)
engine.runAndWait()
driver.quit()