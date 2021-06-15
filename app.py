import datetime
import time

import os
import json
import gspread
import pprint
from datetime import datetime, timedelta
from selenium import webdriver
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

hoshas_cap=[]
hoshas_ava=[]

class WhatsappBot:
    def __init__(self):
        self.bot = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        #self.bot = webdriver.Chrome()

    def url(self):
        bot = self.bot
        bot.get('http://appshoshas.moh.gov.my/bedwatcher/view/index.php')
        #startup = WebDriverWait(bot,50).until(lambda bot: )
        #try:
        total_hoshas= int(bot.find_element_by_xpath("//table[@id='dataTable']/tbody/tr[7]/td[4]").text)
        time.sleep(3)
        icu2A_hoshas= int(bot.find_element_by_xpath("//table[@id='dataTable']/tbody/tr[1]/td[4]").text)
        time.sleep(3)
        icu2B_hoshas= int(bot.find_element_by_xpath("//table[@id='dataTable']/tbody/tr[2]/td[4]").text)
        time.sleep(3)
        icu_hoshas = icu2A_hoshas+icu2B_hoshas
        gen_hoshas=total_hoshas-icu_hoshas
        time.sleep(3)

        totalcap_hoshas=int(bot.find_element_by_xpath("//table[@id='dataTable']/tbody/tr[7]/td[2]").text)
        time.sleep(3)
        icu2A_cap_hoshas=int(bot.find_element_by_xpath("//table[@id='dataTable']/tbody/tr[1]/td[2]").text)
        time.sleep(3)
        icu2B_cap_hoshas=int(bot.find_element_by_xpath("//table[@id='dataTable']/tbody/tr[2]/td[2]").text)
        time.sleep(3)
        icu_cap_hoshas = icu2A_cap_hoshas+icu2B_cap_hoshas
        gencap_hoshas=totalcap_hoshas-icu_cap_hoshas

        bot.quit()
        
        hoshas_cap.append([icu_cap_hoshas])
        hoshas_cap.append([gencap_hoshas])
        hoshas_ava.append([icu_hoshas])
        hoshas_ava.append([gen_hoshas])
        #except:
         #   bot.quit()

sufian = WhatsappBot()
sufian.url()



#update HOSHAS
def hoshas():
    date_times = (datetime.now() + timedelta(hours=8)).strftime("%d/%m/%Y %H:%M:%S")
    sheet.update('B26:B27', hoshas_cap)
    sheet.update('E26:E27', hoshas_ava)
    sheet.update('F26:F27', [[date_times],[date_times]])
    print("Success, HOSHAS updated")

hoshas()


