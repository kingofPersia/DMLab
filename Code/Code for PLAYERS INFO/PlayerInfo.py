# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup as bs
import urllib.request
import csv, sys

def get_basic_player(url):
    with urllib.request.urlopen(url) as response:
        html = response.read()

    soup = bs(html, "lxml")
    li=[]
    for r in soup.find_all('h3'):
        for s in r.find_all('b'):
            team = s.string.replace('\n', "")
            li.append(team)
    for p in soup.findAll(attrs={"class": "ciPlayerinformationtxt"}):
        value_p = ""
        for value in p.findAll('span'):
            try:
                value_p += value.string.replace('\n', "").replace(',', '|')
            except:
                value_p = "NULL"
        li.append(value_p)

    with open("player/player_basic.csv", "a") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(li)

get_basic_player(str(sys.argv[1]))