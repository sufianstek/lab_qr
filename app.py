import datetime
import time

import os
import json
import gspread
import pprint
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from oauth2client.service_account import ServiceAccountCredentials


#LIVE TEST#
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

scopes = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
json_creds = os.getenv("GOOGLE_SHEETS_CREDS_JSON")

creds_dict = json.loads(json_creds)
creds_dict["private_key"] = creds_dict["private_key"].replace("\\\\n", "\n")
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scopes)
client = gspread.authorize(creds)
#LIVE TEST#
'''



#LOCAL TEST#
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('ucc-pahang.json', scope)
client = gspread.authorize(creds)
#LOCAL TEST#
'''


spreadsheet = client.open_by_url("https://docs.google.com/spreadsheets/d/14vFutdJuHcszQKIpAcqyQ106AtBSebeghrRxTp9ittQ")
sheet = spreadsheet.sheet1


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

        sheet.update('D20', sukpa_available)
        sheet.update('G20', sukpa_discharges)
        sheet.update('F20', date_times)

        print("Success, SUKPA updated")
    

ucc = UCCBot('uccadmin', 'P@ssword.123')
ucc.login()
ucc.scrape()


