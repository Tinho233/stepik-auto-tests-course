import math
import time


from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)


valued_treasure = browser.find_element_by_id("treasure")
valued_checked = valued_treasure.get_attribute("valuex")


x_element = valued_checked
x = int(valued_checked)
y = calc(x)


input1 = browser.find_element_by_id("answer")
input1.send_keys(str(y))
input2 = browser.find_element_by_id("robotCheckbox")
input2.click()
input3 = browser.find_element_by_id("robotsRule")
input3.click()
input4 = browser.find_element_by_class_name("btn.btn-default").click()



time.sleep(30)

browser.quit()
