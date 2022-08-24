# A program by B3nam
# !/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import requests

root = Tk()
root.title('B3nam_Tools')
root.geometry("500x200")
a = requests.get('https://api64.ipify.org/')
def IP():
   messagebox.showinfo("My IP ", a.text)

B1 = Button(root, text = "What is My Public IP", command = IP)
B1.place(x = 60,y = 50)
