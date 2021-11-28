"""leak.py: Data leak ? NO, it's OPEN SOURCE AKWOAWKAWO."""

__author__      = "greycat"
__copyright__   = "Copyright 2021"

import requests
from bs4 import BeautifulSoup
import csv
import sys

if (len(sys.argv)<2):
    print('Masukkan nama file mu ex: python3 leak.py namafile.txt')
else: 
    arg = sys.argv[1]
    filename = arg
    with open('res.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        header = ['Nama Lengkap', 'Jenis Kelamin', 'NIK', 'Tempat Lahir', 'Tgl Lahir']
        writer.writerow(header)

        with open(filename) as file:
            for line in file:
                url = line.rstrip()
                page  = requests.get(url)
                soup_expatistan = BeautifulSoup(page.text, "html.parser")
                cards = soup_expatistan.findAll("div", class_="profile-alumni")
                print(url + " - leaked !")

                for i, leak in enumerate(cards):
                    # write the header
                    item = leak.get_text().splitlines()
                    clean = list(filter(str.strip, item))
                    
                    # # write the data
                    data = [clean[1], clean[5], clean[3], clean[7], clean[9]]
                    writer.writerow(data)
                    # print(data)
