#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 13:51:55 2022

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

def player_KPI():
    
    player_total_shots = 0
    player_total_passes = 0
    total_goals = 0
    
    
    for i, events in df.iterrows():
        if events['player_name']=='Gareth Frank Bale':
            if (events['type_name'] == "Shot"):
                if(events['shot_outcome_name'] == "Goal"):
                    total_goals = total_goals + 1
                player_total_shots = player_total_shots + 1
            elif (events['type_name'] == "Pass"):
                player_total_passes = player_total_passes + 1
         
                
    print("=================")
    print("Gareth Bale Stats")
    print("Total Shots " + str(player_total_shots))
    print("Total Passes " + str(player_total_passes))
    print("Total Goals " + str(total_goals))
    print("=================")

player_KPI()