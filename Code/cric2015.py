from bs4 import BeautifulSoup
import urllib.requests
import re
import time

match_url=[]


def match_urls():
    urls=match_result.findAll('ul', {"class": "reports-list content_link"})
    for i in range(len(urls)):
        try:
            match_url.append (r"http://www.espncricinfo.com"+ urls[i].contents[1].next.get('href')+"? ")
        except Exception as e:
            print (e)



result_site=r'http://www.espncricinfo.com/indian-premier-league-2016/engine/series/968923.html'
results_file = urllib.requests.urlopen(result_site).read()
#results_file = open("ipl2015results.txt" ,"r")
match_result = BeautifulSoup( results_file, 'html.parser')
match_urls()
print (len(match_url))

#web_file = open("sc.txt", "r")
# match_url = [r'http://www.espncricinfo.com/indian-premier-league-2016/engine/match/980901.html?',
#              r'http://www.espncricinfo.com/indian-premier-league-2016/engine/match/980903.html?',
#              r'http://www.espncricinfo.com/indian-premier-league-2016/engine/match/980905.html?',
#              r'http://www.espncricinfo.com/indian-premier-league-2016/engine/match/980907.html?',
#              r'http://www.espncricinfo.com/indian-premier-league-2016/engine/match/980909.html?',
#              ]




def scorecard_extract(match_id):
    try:
        team = soup.findAll('th', {"class": "th-innings-heading"})
        ground = soup.findAll('div', {"class": "large-7 medium-7 columns text-right match-information"})
        match_status = soup.findAll('div', {"class": "innings-requirement"})
        grnd_extract = pattern_extract(str(ground[0]), r'view the ground profile for (.*?)"')
        toss_dtl = pattern_extract(str(soup), r"Toss  - <span class=.*?>(.*?)</span")
        mom_extract = pattern_extract(str(soup), r'Player of the match.*?>(.*?)\(')
        file_write(str(match_id) + ";;" + team[0].contents[0] + ";;" + team[2].contents[0] + ";;" + grnd_extract + ";;" +match_status[0].contents[0] + ";;" + mom_extract + ";;"+toss_dtl+";;" + "\n", "ipl2015_summary")
        # Retrieving player dismissal information
        team_batting_dtl = soup.findAll('table', {'class': 'batting-table innings'})
        innings_id = 1
        for team_batting in team_batting_dtl:
            playerinfo = BeautifulSoup(str(team_batting), 'html.parser')
            # team_name = team.findAll('th', {"class": "th-innings-heading"})
            player = playerinfo.findAll('td', {"class": "batsman-name"})
            playerDismissal = playerinfo.findAll('td', {"class": "dismissal-info"})
            for x in range(len(player)):
                file_write(str(match_id) + ";;" + "Innings " + str(innings_id) + ";;" + player[x].next.next + ";;" +
                           playerDismissal[x].next + "\n", "ipl2015dtl")
            innings_id = innings_id + 1
    except Exception as e:
        print(e)


def item_extract(classname, innings,match_id):
    x = soup.findAll('div', {"class": classname})
    z = lambda inp, rep="\n": str.replace(inp, rep, "", 1)
    for i in x:
       try:
            overs = str(i.contents[1])
            commentary = str(i.contents[3])
            over = pattern_extract(overs, r'"commentary-overs">(.*?)</div>')
            b2b = pattern_extract(commentary, r'<p>(.*?),')
            hghlt = pattern_extract(commentary, r',(.*?),')
            dtl = pattern_extract(commentary, r',.*?,(.*?)</p>')
            file_write(over + ";;" + b2b + ";;" + z(z(z(hghlt), '<span class="commsImportant">'), '</span>') + ";;" + z(dtl) + ";;" + innings + ";;" +str(match_id)+";;" + "\n", "ipl2015")
       except Exception as e:
            print(e)


def file_write(content,file_nm):
    out_file = open(file_nm+".csv", "w")
    out_file.write(content)
    out_file.close()


def pattern_extract(in_txt, pattern):
    extract = re.compile(pattern, flags=re.DOTALL)
    x= extract.findall(in_txt)[0]
    return x


match_id=0
for match in match_url:
    match_id=match_id+1
    print (match_id)
    if match_id>0:
        innings = "1"
        sites = [match.strip() + r'innings=1;view=commentary', match.strip() + r'innings=2;view=commentary']
        for site in sites:
            site_txt = urllib.request.urlopen(site).read()
            soup = BeautifulSoup(site_txt, 'html.parser')
            item_extract('commentary-event', "Innings " + innings, match_id)
            innings = "2"
        scorecard = match + r'view=scorecard'
        site_txt=urllib.request.urlopen(scorecard).read()
        soup = BeautifulSoup(site_txt,'html.parser')
        scorecard_extract(match_id)
        time.sleep(10)

# Once tested replace web_file with site_text
# site_txt=urllib.urlopen(scorecard).read()
# soup = BeautifulSoup(site_txt,'html.parser')

#soup = BeautifulSoup(web_file, 'html.parser')
#scorecard_extract()

#web_file.close()
