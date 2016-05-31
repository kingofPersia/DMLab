# -*- coding: utf-8 -*-
"""
Created on Sat May 14 19:57:32 2016

@author: avinashchandra
"""

import pandas as pd
from sqlalchemy import create_engine
import datetime as dt
import plotly.plotly as py
from plotly.graph_objs import Bar, Scatter, Marker,Layout


start = dt.datetime.now()
chunksize = 20000
j = 0
index_start = 1

disk_engine = create_engine('sqlite:///test_database.db')
for df in pd.read_csv('info_meta_2.csv',chunksize=chunksize,iterator=True,encoding='utf-8'):
    df['info_dates'] = pd.to_datetime(df['info_dates'])
    df.index +=index_start
    columns=['info_city','info_competition','info_dates','info_gender','info_match_type','info_by	','info_by_score','info_match_winner','info_overs',
    'info_player_of_match','info_teams1','info_teams2','info_decision','info_toss_winner','info_umpires1','info_umpires2','info_venue']
    
    for c in df.columns:
        if c not in columns:
            df = df.drop(c, axis=1)
    j+=1
    print '{} seconds: completed {} rows'.format((dt.datetime.now() - start).seconds, j*chunksize)

    df.to_sql('data', disk_engine, if_exists='append')
    index_start = df.index[-1] + 1
df = pd.read_sql_query('Select info_match_winner, Count(*) as `no_of_win`' 'from data' 'group by info_match_winner',disk_engine)