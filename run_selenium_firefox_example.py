#Selenium lets you control web browsers, install it with      pip install selenium

#You need to install gecko driver first, here: https://github.com/mozilla/geckodriver/releases
#download it and put it somewhere for your path to find, add directory to path as path variable then reset your computer, sorry
#don't put it directly in the C drive because you most programs can't run directly there, it's like the root directory, instead put it in your users folder

#webDriver API here: 
#  https://selenium-python.readthedocs.io/api.html
#browser API starts after "Remote WebDriver" heading
#there is a lot in the API, positional data, cookie control, scripts
#web element API starts after "Remote WebDriver WebElement"

#Of course you have to have firefox installed!

from selenium import webdriver
import time

browser = webdriver.Firefox()  #note tha capital letter!!!!
#browser.set_page_load_timeout(10)

browser.get(r'https://automatetheboringstuff.com/')
elem = browser.find_element_by_css_selector('.main > div:nth-child(1) > ul:nth-child(23) > li:nth-child(12) > a:nth-child(1)') #can't be raw r'xxx'
elem.click()

#finding stuff on pages, element or elements:
elems = browser.find_elements_by_css_selector('p')
print(len(elems))
elem = browser.find_element_by_css_selector('.main > div:nth-child(1) > p:nth-child(10)')
print(elem.text)
elem = browser.find_element_by_css_selector('http') #the whole page
print(elem.text)

elems = browser.find_elements_by_id('no idea')
elems = browser.find_elements_by_link_text('text')
elems = browser.find_elements_by_partial_link_text('text')
elems = browser.find_elements_by_name('name')
elems = browser.find_elements_by_tag_name('tag name')

time.sleep(3)

browser.get(r'https://www.eventfinda.co.nz/')
searchElem = browser.find_element_by_css_selector('#mastheadSearchInput')
searchElem.send_keys('Auckland') #submits text to a field
searchElem.submit() #finds the enter button for the field or sends it a carraige return, who knows
time.sleep(3)
searchElem = browser.find_element_by_css_selector('#mastheadSearchInput')
searchElem.clear()
time.sleep(3)

browser.back() #back button
time.sleep(3)
browser.forward()
time.sleep(3)
browser.fullscreen_window()
browser.get_screenshot_as_png() #gets screenshot as png in memory
browser.save_screenshot(r'C:\Users\Public\screenshot.png')
browser.refresh()


browser.close() 