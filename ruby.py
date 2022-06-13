import requests
import json
import sys
import argparse
from colorama import Fore, Back, Style, init
import csv
import os.path
from scripts.bitchute import *
from scripts.rumble import *
from scripts.youtube import *
import time

init(autoreset=True)

ruby = Fore.RED + r"""
   ▄████████ ███    █▄  ▀█████████▄  ▄██   ▄
  ███    ███ ███    ███   ███    ███ ███   ██▄
  ███    ███ ███    ███   ███    ███ ███▄▄▄███
 ▄███▄▄▄▄██▀ ███    ███  ▄███▄▄▄██▀  ▀▀▀▀▀▀███
▀▀███▀▀▀▀▀   ███    ███ ▀▀███▀▀▀██▄  ▄██   ███
▀███████████ ███    ███   ███    ██▄ ███   ███
  ███    ███ ███    ███   ███    ███ ███   ███
  ███    ███ ████████▀  ▄█████████▀   ▀█████▀
  ███    ███
"""

print(ruby)
print(" A Rumble, Bitchute, and YouTube scraper and search engine \n")
print(Fore.RED + " Ruby is searching... \n")
time.sleep(2)

print(Fore.RED + " [!] -- Rumble results -- [!] \n")
rumble()
print(Fore.RED + " [!] -- BitChute results -- [!] \n")
bitchute()
print(Fore.RED + " [!] -- YouTube results -- [!] \n")
youtube()

with open('search.csv',"r") as f:
    reader = csv.reader(f,delimiter = ",")
    data = list(reader)
    row_count = len(data)

print(Fore.RED + " [!] -- Search complete. Check search.csv -- [!]\n")

print(Fore.RED + " [#] -- Ruby has collected " + str(row_count) + " total videos -- [#]\n")
