from selenium import webdriver
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#binary = FirefoxBinary('C:/Program Files/Mozilla Firefox/firefox.exe')

#driver = webdriver.Firefox(firefox_binary=binary)

browser = webdriver.Chrome()
browser.get('http://localhost:8000')

assert 'Django' in browser.title