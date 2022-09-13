import datetime
import time

import os
import json
import pprint
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")





class UCCBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        #self.bot = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        self.bot = webdriver.Chrome()

    
    def login(self):
        try:
            bot = self.bot
            bot.get('http://appshtaa.moh.gov.my/bedwatch/ucc/index.php')
            time.sleep(5)
            email = bot.find_element_by_name('username')
            password = bot.find_element_by_name('password')
            email.clear()
            password.clear()
            email.send_keys(self.username)
            password.send_keys(self.password)
            password.send_keys(Keys.RETURN)
            time.sleep(5)
        except:
            bot.quit()


    def scrape(self):
        date_times = (datetime.now() + timedelta(hours=8)).strftime("%d/%m/%Y %H:%M:%S")
        bot = self.bot
        sukpa_available = int(bot.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[3]").text)
        time.sleep(5)
        sukpa_discharges = int(bot.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[7]").text)
        time.sleep(5)

        print("Success, SUKPA updated")
    

ucc = UCCBot('uccadmin', 'P@ssword.123')
ucc.login()
ucc.scrape()


