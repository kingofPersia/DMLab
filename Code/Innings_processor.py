# -*- coding: utf-8 -*-
"""
Created on Sat May 14 17:06:56 2016

@author: avinashchandra
"""

import yaml
with open('/Users/raveekiat/Desktop/SS2016/DMLAB/DATA/NEW/interested_all.yaml', 'r') as stream:
    data = yaml.load_all(stream)
    for x in data:
​
        try:
            info_dates = str(x["info"]["dates"][0])
        except:
            info_dates = "NULL"
​
        try:
            info_teams1 = str(x["info"]["teams"][0])
        except:
            info_teams1 = "NULL"
​
        try:
            info_teams2 = str(x["info"]["teams"][1])
        except:
            info_teams2 = "NULL"
​
        for y in x['innings']:
            for k, v in y.items():
                for delvry in v['deliveries']:
                    for key, value in delvry.items():
                        # print(" batsman is %s with bowler %s and nonstriker %s " %(value['batsman'], value['bowler'], value['non_striker']))
                        # print(" run scored is %d " % (value['runs']['total']))
                        try:
                            innings_number = str(k)
                        except:
                            innings_number = "NULL"
​
                        try:
                            innings_team = v["team"]
                        except:
                            innings_team = "NULL"
​
                        try:
                            deliveries = str(key)
                        except:
                            deliveries = "NULL"
​
                        try:
                            batsman = value['batsman']
                        except:
                            batsman = "NULL"
​
                        try:
                            bowler = value['bowler']
                        except:
                            bowler = "NULL"
​
                        try:
                            non_striker = value['non_striker']
                        except:
                            non_striker = "NULL"
​
                        try:
                            for k_e, v_e in value['extras'].items():
                                extras_type = k_e
                                extras_value = str(v_e)
                        except:
                            extras_type = "NULL"
                            extras_value = "NULL"
​
                        try:
                            runs_batsman = str(value['runs']['batsman'])
                        except:
                            runs_batsman = "NULL"
​
                        try:
                            runs_extras = str(value['runs']['extras'])
                        except:
                            runs_extras = "NULL"
​
                        try:
                            runs_total = str(value['runs']['total'])
                        except:
                            runs_total = "NULL"
​
                        try:
                            wicket_fielders = str(value['wicket']['fielders'])
                        except:
                            wicket_fielders = "NULL"
​
                        try:
                            wicket_kind = value['wicket']['kind']
                        except:
                            wicket_kind = "NULL"
​
                        try:
                            wicket_player_out = value['wicket']['player_out']
                        except:
                            wicket_player_out = "NULL"
​
                        print("\"" +
                              info_dates + "\",\"" +
                              info_teams1 + "\",\"" +
                              info_teams2 + "\",\"" +
                              innings_number + "\",\"" +
                              innings_team + "\",\"" +
                              deliveries + "\",\"" +
                              batsman + "\",\"" +
                              bowler + "\",\"" +
                              non_striker + "\",\"" +
                              extras_type + "\",\"" +
                              extras_value + "\",\"" +
                              runs_batsman + "\",\"" +
                              runs_extras + "\",\"" +
                              runs_total + "\",\"" +
                              wicket_fielders + "\",\"" +
                              wicket_kind + "\",\"" +
                              wicket_player_out
                              + "\""
                              )