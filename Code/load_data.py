# -*- coding: utf-8 -*-
"""
Created on Thu May 12 11:51:59 2016

@author: avinashchandra
"""

import sqlite3
import json 

def load_data(json_file):
    conn=sqlite3.connect('Car_sharing.sqlite')
    cur=conn.cursor()
    cur.execute(''' CREATE TABLE IF NOT EXISTS Car_daily_data ( Car_lic_Nn TEXT, Location_X TEXT,Location_Y	TEXT, Date	NUMERIC, Time NUMERIC, Car_provider TEXT, Car_id	INTERGER, Car_type NUMERIC, Zone_id INTEGER,
    Car_model TEXT)''')

    fh=json.loads('json_file')
    
    