from tkinter import *
from tkinter import filedialog, StringVar
from tkinter.constants import X
import string
import time
import tkinter as tk
import sys
from PIL import Image, ImageTk


root= tk.Tk()
root.title("Lab QR reader")

image_scan = Image.open("image1.png")
size = (150, 70)
image_scan = image_scan.resize(size)
image_png = ImageTk.PhotoImage(image_scan)

def answer():
    if input() == "mom":
        print('success')
    else:
        print('failed')

def process_id(e):
    print(e)

id_text = tk.StringVar()

canvas1 = tk.Canvas(root, width = 500, height = 400, bg = 'lightsteelblue')
canvas1.pack()

label1 = tk.Label(text='Lab QR reader', bg='lightsteelblue', fg='black', font=('helvetica', 40, 'bold'))
canvas1.create_window(250, 90, window=label1)

label2 = tk.Label(text='Display QR code at QR scanner', bg='lightsteelblue', fg='black', font=('helvetica', 20, 'bold'))
canvas1.create_window(250, 200, window=label2)

label3 = tk.Label(image=image_png)
canvas1.create_window(250, 280, window=label3)

id_entry = tk.Entry(textvariable=id_text, font=( 'helvetica', 15), width=20)
id_area = canvas1.create_window(250, 350, window=id_entry)

id_entry.bind("<Return>", (lambda event: process_id(id_entry.get())))

#answer()


root.mainloop()