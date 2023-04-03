from selenium.webdriver.chrome.options import Options
from selenium import webdriver

def setup():
    options = Options()
    options.headless = False
    return webdriver.Chrome(options=options)
    

