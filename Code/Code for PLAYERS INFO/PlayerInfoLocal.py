import glob
from bs4 import BeautifulSoup as bs

# attribute_list = ['Team', 'Full name', 'Born', 'Current age', 'Major teams', 'Nickname', 'Playing role',
#                 'Batting style', 'Bowling style', 'Height', 'Education', 'Relation', 'Fielding position',
#                 'Also known as', 'Died', 'Other', 'In a nutshell']

li = glob.glob("fullsite/*.html")
for link in li:
    with open(link, "r") as f:
        soup = bs(f, "lxml")
        try:
            name_i = soup.find("meta", property="og:title").attrs['content']
        except:
            name_i = '-'
        for r in soup.find_all('h3'):
            for s in r.find_all('b'):
                try:
                    team = s.string.replace('\n', "")
                except:
                    team = '-'
                result = {"name": name_i.encode('utf-8'), "team": team.encode("utf-8")}

        for r in soup.findAll(attrs={"class": "ciPlayerinformationtxt"}):
            for s in r.find_all('b'):
                try:
                    attr_i = s.string.replace('\n', "")
                    attr = attr_i.replace(' ', "_")
                except:
                    attr = '-'
            for s in r.find_all('span'):
                try:
                    value_i = s.string.replace('\n', "")
                    value = value_i.replace(',', "|")
                except:
                    value = '-'
                result.update({attr.encode("utf-8"): value.encode("utf-8")})

        # attribute_list = ['Team', 'Full name', 'Born', 'Current age', 'Major teams', 'Nickname', 'Playing role',
        #                 'Batting style', 'Bowling style', 'Height', 'Education', 'Relation', 'Fielding position',
        #                 'Also known as', 'Died', 'Other', 'In a nutshell']
        basic_info = ""
        try:
            name = result['name']
        except:
            name = "-"
        try:
            fullname = result['Full_name']
        except:
            fullname = "-"
        try:
            team = result['team']
        except:
            team = "-"
        try:
            playingrole = result['Playing_role']
        except:
            playingrole = "-"
        try:
            battingstyle = result['Batting_style']
        except:
            battingstyle = "-"
        try:
            bowlingstyle = result['Bowling_style']
        except:
            bowlingstyle = "-"
        try:
            fieldingposition = result['Fielding_position']
        except:
            fieldingposition = "-"

        basic_info = "\"" + name + "\",\"" + fullname + "\",\"" + team + "\",\"" + playingrole + "\",\"" \
                     + battingstyle + "\",\"" + bowlingstyle + "\",\"" + fieldingposition + "\","

        tables = soup.find_all("table", class_="engineTable")
        rows1 = []

        for row in tables[0].find_all('tr'):
            rows1.append([val.text.encode('utf8').rstrip() for val in row.find_all(['td', 'th'])])

        to_Append = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
        try:
            if rows1[1][0] == 'Tests':
                pass
            else:
                rows1.insert(1, to_Append)
        except:
            rows1.insert(1, to_Append)

        try:
            if rows1[2][0] == 'ODIs':
                pass
            else:
                rows1.insert(2, to_Append)
        except:
            rows1.insert(2, to_Append)

        try:
            if rows1[3][0] == 'T20Is':
                pass
            else:
                rows1.insert(3, to_Append)
        except:
            rows1.insert(3, to_Append)

        try:
            if rows1[4][0] == 'First-class':
                pass
            else:
                rows1.insert(4, to_Append)
        except:
            rows1.insert(4, to_Append)

        try:
            if rows1[5][0] == 'List A':
                pass
            else:
                rows1.insert(5, to_Append)
        except:
            rows1.insert(5, to_Append)

        try:
            if rows1[6][0] == 'Twenty20':
                pass
            else:
                rows1.insert(6, to_Append)
        except:
            rows1.insert(6, to_Append)

        data1 = ""
        for i in range(1,7):
            for j in range(1, 15):
                try:
                    data1 += "\"" + rows1[i][j] + "\","
                except:
                    data1 += "\"-\","


        rows2 = []
        for row in tables[1].find_all('tr'):
            rows2.append([val.text.encode('utf8').rstrip() for val in row.find_all(['td', 'th'])])

        to_Append = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',]
        try:
            if rows2[1][0] == 'Tests':
                pass
            else:
                rows2.insert(1, to_Append)
        except:
            rows2.insert(1, to_Append)

        try:
            if rows2[2][0] == 'ODIs':
                pass
            else:
                rows2.insert(2, to_Append)
        except:
            rows2.insert(2, to_Append)

        try:
            if rows2[3][0] == 'T20Is':
                pass
            else:
                rows2.insert(3, to_Append)
        except:
            rows2.insert(3, to_Append)

        try:
            if rows2[4][0] == 'First-class':
                pass
            else:
                rows2.insert(4, to_Append)
        except:
            rows2.insert(4, to_Append)

        try:
            if rows2[5][0] == 'List A':
                pass
            else:
                rows2.insert(5, to_Append)
        except:
            rows2.insert(5, to_Append)
        try:
            if rows2[6][0] == 'Twenty20':
                pass
            else:
                rows2.insert(6, to_Append)
        except:
            rows2.insert(6, to_Append)

        data2 = ''
        for i in range(1, 7):
            for j in range(1, 14):
                try:
                    data2 += "\"" + rows2[i][j] + "\","
                except:
                    data2 += "\"-\","

    print basic_info + data1 + data2
