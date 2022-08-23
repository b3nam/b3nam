# A program from B3nam
# Please Run this code on Python version 3 .x
from tkinter import filedialog

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
