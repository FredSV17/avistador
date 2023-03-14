from selenium.webdriver.chrome.options import Options
from selenium import webdriver

def setup():
    options = Options()
    options.headless = True
    return webdriver.Chrome(options=options)
    

