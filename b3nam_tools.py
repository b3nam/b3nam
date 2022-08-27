# A program by B3nam
# !/usr/bin/python3
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import requests

root = Tk()
root.title('B3nam_Tools')
root.geometry("500x200")
a = requests.get('https://api64.ipify.org/')
def IP():
   messagebox.showinfo("Your Public IP ", a.text)
def cryption():
   tf = filedialog.askopenfilename(
        title="Open Text file", 
        filetypes=(("Encrypted Files", "*"),)
        )
   fw = filedialog.asksaveasfile(
        title="Save to", 
        filetypes=(("Decrypted Files", "*.txt"),)
        )
   fr = open(tf, "rb")
   content = fr.read()
   decrypted = ""
   key = 0x5a
   for c in content:
       decrypted += chr(int(c) ^ key)
   fw.write(decrypted)
   fw.close()
   fr.close()

B1 = Button(root, text = "What is My Public IP", command = IP)
B1.place(x = 60,y = 50)

B2 = Button(root, text = "Decrypt Files", command = cryption)
B2.place(x = 300,y = 50)
