from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = '/Users/Daniel/Development/chromedriver'
TWITTER_EMAIL = 'AutomatingSpeed'
TWITTER_PASSWORD = '8Crosby7'

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0
    