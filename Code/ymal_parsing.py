# -*- coding: utf-8 -*-
"""
Created on Mon May 09 14:00:32 2016

@author: avinashchandra
"""

import yaml

with open("all_male.yaml", 'r') as stream:
    
    data=yaml.load_all(stream)
    for x in data:
        for y in x['innings']:
            print "============================================================"
            for k,v in y.iteritems():
                for delvry in v['deliveries']:
                    for key, value in delvry.iteritems():
                        print " batsman is %s with bowler %s and nonstriker %s " %(value['batsman'], value['bowler'], value['non_striker'])
                        print " run scored is %d " % (value['runs']['total'])
        
        
                
        
         
         
         
        
        
    