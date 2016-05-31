# -*- coding: utf-8 -*-
"""
Created on Tue May 17 11:30:50 2016

@author: avinashchandra
"""

from bs4 import BeautifulSoup
import requests
#from collections import namedtuple
import csv


player_list_tupled = []
match_type_dict = dict(test=1, odi = 2, t20 = 3,)
country_dict = dict(india = 6, england = 1, australia = 2, south_africa = 3, west_indies = 4, new_zealand = 5, pakistan = 7, sri_lanka = 8, 
                    zimbabwe = 9,afganistan=40,Ireland=29, Hong_Kong=29, Papua_New_Guinea=29, Scotland=30, UAE=27,)

#build player list
resulting_player_list = []
for k,v in country_dict.items():
    country_code = v
    country_name = k
    for m_k,m_v in match_type_dict.items():
        match_type_str = m_k
        play_format = m_v
        url_format = 'http://www.espncricinfo.com/ci/content/player/caps.html?country={country_code};class={play_format}'
        url = url_format.format(country_code=country_code, play_format = play_format)
        print "getting data from "  + url
        player_list_html = requests.get(url).content
        soup = BeautifulSoup(player_list_html,"lxml")
        player_class_dict = {'class': 'ciPlayername'}
        player_list_raw = soup.find_all('li',attrs=player_class_dict)
        for p in player_list_raw:
            name = p.text
            link_a = p.find('a')
            link_ref=link_a.get('href')
            link='http://www.espncricinfo.com/'+link_ref
            player_list=[name,link]
            with open ("players_profile_link2_update_with_new_country.csv","a") as f:
                writer=csv.writer(f,quoting=csv.QUOTE_ALL)
                writer.writerow(player_list)
            
            
            