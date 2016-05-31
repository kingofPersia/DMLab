import urllib2
from bs4 import BeautifulSoup
import csv

linksFile = open("LinkSource.txt")
lines = list(linksFile.readlines())
for url in lines: 
    try:
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page,"lxml")
        name=soup.find("meta", property="og:title").attrs['content']
        tables=soup.find_all("table", class_="engineTable")
        headers = [header.text.strip() for header in tables[0].find_all('th',{'scope' :'col'})]
        rows = []
        for row in tables[0].find_all('tr'):
            rows.append([val.text.encode('utf8').rstrip() for val in row.find_all(['td', 'th'])])

        with open(str(name)+"_"+"Batting.csv", 'wb') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(row for row in rows if row)

        rows = []
        for row in tables[1].find_all('tr'):
            rows.append([val.text.encode('utf8').rstrip() for val in row.find_all(['td', 'th'])])

        with open(str(name)+"_"+"Bowling.csv", 'wb') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(row for row in rows if row)
    except:
        print "u r_fucked"