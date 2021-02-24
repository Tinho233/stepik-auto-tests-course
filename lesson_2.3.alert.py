import math
import time


from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)


btn_click = browser.find_element_by_class_name("btn.btn-primary").click()


alert = browser.switch_to.alert
alert.accept()


valued_tr = browser.find_element_by_id("input_value").text
x = int(valued_tr)
y = calc(x)


input1 = browser.find_element_by_id("answer")
input1.send_keys(str(y))


btn_click = browser.find_element_by_class_name("btn.btn-primary").click()


time.sleep(15)


browser.quit()







