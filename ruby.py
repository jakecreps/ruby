import requests
import json
import sys
import argparse
from colorama import Fore, Back, Style, init
import csv
import os.path
from bitchute import *
from rumble import *
from youtube import *

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
print(" A Rumble, Bitchute, and YouTube scraper\n")
print(" By: Jake Creps \n")

print(" [!] -- Search complete. Check search.csv -- [!]\n")

with open('search.csv',"r") as f:
    reader = csv.reader(f,delimiter = ",")
    data = list(reader)
    row_count = len(data)

print(" [#] -- Ruby has collected " + str(row_count) + " videos -- [#]\n")
