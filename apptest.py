import smtplib 
import string
import datetime
import time

import os
import json
import gspread
import pprint

from flask import Flask, render_template, jsonify, request, abort, redirect, url_for
from oauth2client.service_account import ServiceAccountCredentials

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('ucc-pahang.json', scope)
client = gspread.authorize(creds)

spreadsheet = client.open_by_url("https://docs.google.com/spreadsheets/d/14vFutdJuHcszQKIpAcqyQ106AtBSebeghrRxTp9ittQ")
sheet = spreadsheet.sheet1


hoshas_cap=[]
hoshas_ava=[]

class WhatsappBot:
    def __init__(self):
        self.bot = webdriver.Firefox()

    def url(self):
        bot = self.bot
        bot.get('http://appshoshas.moh.gov.my/bedwatcher/view/index.php')
        #startup = WebDriverWait(bot,50).until(lambda bot: )
        #try:
        total_hoshas= int(bot.find_element_by_xpath("//table[@id='dataTable']/tbody/tr[6]/td[4]").text)
        time.sleep(3)
        icu_hoshas= int(bot.find_element_by_xpath("//table[@id='dataTable']/tbody/tr[4]/td[4]").text)
        gen_hoshas=total_hoshas-icu_hoshas
        time.sleep(3)

        totalcap_hoshas=int(bot.find_element_by_xpath("//table[@id='dataTable']/tbody/tr[6]/td[2]").text)
        time.sleep(3)
        icu_cap_hoshas=int(bot.find_element_by_xpath("//table[@id='dataTable']/tbody/tr[4]/td[2]").text)
        gencap_hoshas=totalcap_hoshas-icu_hoshas

        bot.quit()
        
        hoshas_cap.append([icu_cap_hoshas])
        hoshas_cap.append([gencap_hoshas])
        hoshas_ava.append([icu_hoshas])
        hoshas_ava.append([gen_hoshas])
        #print(hoshas_cap)
        #except:
         #   bot.quit()

sufian = WhatsappBot()
sufian.url()

#update HOSHAS
def hoshas():
    sheet.update('B4:B5', hoshas_cap)
    sheet.update('E4:E5', hoshas_ava)

hoshas()

