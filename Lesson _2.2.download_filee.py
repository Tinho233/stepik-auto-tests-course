import os

from selenium import webdriver
import time

from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)


input1 = browser.find_element_by_name("firstname")
input1.send_keys("Ivan")
input2 = browser.find_element_by_name("lastname")
input2.send_keys("Химен")
input3 = browser.find_element_by_name("email")
input3.send_keys("ad@mail.ru")


current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "Newbi.txt"
file_path = os.path.join(current_dir, file_name)
element = browser.find_element_by_id("file")
element.send_keys(file_path)


btn_click = browser.find_element_by_class_name("btn.btn-primary").click()


time.sleep(10)

browser.quit()