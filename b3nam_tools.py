# A program from B3nam
# Please Run this code on Python version 3 .x


import requests

a = requests.get('https://api64.ipify.org/')
print("Public IPV4/6 address is :"," ",a.text)
