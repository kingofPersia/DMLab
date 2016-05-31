# -*- coding: utf-8 -*-
"""
Created on Sat May 14 00:31:14 2016

@author: avinashchandra
"""

import yaml
f = open('all_male.yaml', 'r')
for data in yaml.load_all(f):
    try:
        meta_data_version = str(data["meta"]["data_version"])
    except:
        meta_data_version = "NULL"
    try:
        meta_created = str(data["meta"]["created"])
    except:
        meta_created = "NULL"
    try:
        meta_revision = str(data["meta"]["revision"])
    except:
        meta_revision = "NULL"
    try:
        info_city = str(data["info"]["city"])
    except:
        info_city = "NULL"
    try:
        info_competition = str(data["info"]["competition"])
    except:
        info_competition = "NULL"
    try:
        info_dates = str(data["info"]["dates"][0])
    except:
        info_dates = "NULL"
    try:
        info_gender = str(data["info"]["gender"])
    except:
        info_gender = "NULL"
    try:
        info_match_type = str(data["info"]["match_type"])
    except:
        info_match_type = "NULL"
    try:
        info_by = str(data["info"]["outcome"]["by"])
    except:
        info_by = "NULL"
    try:
        info_match_winner = str(data["info"]["outcome"]["winner"])
    except:
        info_match_winner = "NULL"
    try:
        info_overs = str(data["info"]["overs"])
    except:
        info_overs = "NULL"
    try:
        info_player_of_match = str(data["info"]["player_of_match"][0])
    except:
        info_player_of_match = "NULL"
    try:
        info_teams1 = str(data["info"]["teams"][0])
    except:
        info_teams1 = "NULL"
    try:
        info_teams2 = str(data["info"]["teams"][1])
    except:
        info_teams2 = "NULL"
    try:
        info_decision = str(data["info"]["toss"]["decision"])
    except:
        info_decision = "NULL"
    try:
        info_toss_winner = str(data["info"]["toss"]["winner"])
    except:
        info_toss_winner = "NULL"
    try:
        info_umpires1 = str(data["info"]["umpires"][0])
    except:
        info_umpires1 = "NULL"
    try:
        info_umpires2 = str(data["info"]["umpires"][1])
    except:
        info_umpires2 = "NULL"
    try:
        info_venue = str(data["info"]["venue"])
    except:
        info_venue = "NULL"
    print(meta_data_version + "," +
          meta_created + "," +
          meta_revision + "," +
          info_city + "," +
          info_competition + "," +
          info_dates + "," +
          info_gender + "," +
          info_match_type + "," +
          info_by + "," +
          info_match_winner + "," +
          info_overs + "," +
          info_player_of_match + "," +
          info_teams1 + "," +
          info_teams2 + "," +
          info_decision + "," +
          info_toss_winner + "," +
          info_umpires1 + "," +
          info_umpires2 + "," +
          info_venue
          )
    # except:
    #    print("NULL")
    # for inning in data["innings"]:
    #    for key, data in inning.items():
    #        print(key, data["deliveries"][0])