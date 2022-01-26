#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 13:03:53 2022

@author: atifsiddiqui
"""

#Function to draw the pitch
import matplotlib.pyplot as plt
import numpy as np

#Size of the pitch in yards (!!!)
pitchLengthX=120
pitchWidthY=80

#ID for England vs Sweden Womens World Cup
match_id_required = 18245
home_team_required ="Real Madrid"
away_team_required ="Liverpool"

file_name=str(match_id_required)+'.json'

import json
with open('/Users/atifsiddiqui/Documents/SoccerTact/open-data-master/data/events/'+file_name) as data_file:
    #print (mypath+'events/'+file)
    data = json.load(data_file)
    
#get the nested structure into a dataframe 
#store the dataframe in a dictionary with the match id as key (remove '.json' from string)
from pandas.io.json import json_normalize
df = json_normalize(data, sep = "_").assign(match_id = file_name[:-5])

Liv_data =  df.loc[df['team_name'] == 'Liverpool'].set_index('id')
real_data =  df.loc[df['team_name'] == 'Real Madrid'].set_index('id')

def RealteamKPI():
    
    total_shots = 0
    total_passes = 0
    
    
    for i, events in real_data.iterrows():
        if (events['type_name'] == "Shot"):
            total_shots = total_shots + 1
        elif (events['type_name'] == "Pass"):
            total_passes = total_passes + 1
    print("=================")
    print("Real Madrid Stats")
    print("Total Shots " + str(total_shots))
    print("Total Passes " + str(total_passes))
    print("=================")

def LivteamKPI():
    
    total_shots = 0
    total_passes = 0
    
    
    for i, events in Liv_data.iterrows():
        if (events['type_name'] == "Shot"):
            total_shots = total_shots + 1
        elif (events['type_name'] == "Pass"):
            total_passes = total_passes + 1
    print("=================")
    print("Liverpool Stats")
    print("Total Shots " + str(total_shots))
    print("Total Passes " + str(total_passes))
    print("=================")

RealteamKPI()    
LivteamKPI()