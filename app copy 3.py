from email.policy import default
from tkinter import *
from tkinter import filedialog, StringVar
from tkinter.constants import X
import string
import time
import tkinter as tk
import sys
import os
import json
from PIL import Image, ImageTk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

root= tk.Tk()
root.title("Lab QR reader")

image_scan = Image.open("image1.png")
size = (150, 70)
image_scan = image_scan.resize(size)
image_png = ImageTk.PhotoImage(image_scan)

def loading():
    canvas1.itemconfig(label_4, state='normal')

def unloading():
    canvas1.itemconfig(label_4, state='hidden')


def process_id(e):
    loading()
    if len(e) == 12:
        json_id = e
        print('ic')
    else:
        e = json.loads(e)
        json_id = e['id']
        print('qr')
    browser = webdriver.Firefox()
    browser.get('http://192.168.14.21:8080/apex/f?p=100:101:14910514305442::::')
    time.sleep(3)
    username = browser.find_element(By.ID, 'P101_USERNAME')
    password = browser.find_element(By.ID, 'P101_PASSWORD')
    username.clear()
    password.clear()
    username.send_keys('ANE3')
    password.send_keys('ane3123')
    password.send_keys(Keys.RETURN)
    time.sleep(3)

    result_btn = browser.find_element(By.XPATH, "/html/body/form/table[2]/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[1]/td/a")
    result_btn.click()

    time.sleep(3)
    pt_id = browser.find_element(By.ID, 'P30101_PID')
    pt_id.send_keys(json_id)
    
    search_btn = browser.find_element(By.XPATH, "/html/body/form/table[2]/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table[1]/tbody/tr/td[2]/a")
    search_btn.send_keys(Keys.RETURN)
    time.sleep(5)
    browser.quit()

def clear_text():
   id_entry.delete(0, END)



id_text = tk.StringVar()

canvas1 = tk.Canvas(root, width = 500, height = 400, bg = 'lightsteelblue')
canvas1.pack()

label1 = tk.Label(text='Lab QR reader', bg='lightsteelblue', fg='black', font=('helvetica', 40, 'bold'))
canvas1.create_window(250, 90, window=label1)

label2 = tk.Label(text='Display QR code at QR scanner', bg='lightsteelblue', fg='black', font=('helvetica', 20, 'bold'))
canvas1.create_window(250, 160, window=label2)

label3 = tk.Label(image=image_png)
canvas1.create_window(250, 240, window=label3)

id_entry = tk.Entry(textvariable=id_text, font=( 'helvetica', 18), width=15)
id_area = canvas1.create_window(180, 310, window=id_entry)

clear_btn = tk.Button(text='Clear', command= lambda : [clear_text(), unloading()],bg='blue', fg='white', font=('helvetica', 12), width=10)
clearbtn = canvas1.create_window(350, 310, window=clear_btn)

label4 = tk.Label(text='   SUCCESS   ', bg='green', fg='white', font=('helvetica', 12, 'bold'))
label_4 = canvas1.create_window(250, 350, window=label4, state='normal')

id_entry.bind("<Return>", lambda event: process_id(id_entry.get()))

id_entry.focus_set()
root.mainloop()
