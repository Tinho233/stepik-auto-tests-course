from selenium import webdriver
import time
import math

from selenium.webdriver.support.select import Select


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

valued_tr = browser.find_element_by_id("input_value").text


x = int(valued_tr)
y = calc(x)


input1 = browser.find_element_by_id("answer")
input1.send_keys(str(y))
input2 = browser.find_element_by_id("robotCheckbox").click()


radio_btn = browser.find_element_by_id("robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", radio_btn)
radio_btn.click()


button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()


time.sleep (10)


browser.quit()








print(y)

