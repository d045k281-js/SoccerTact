#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 13:03:53 2022

@author: 
"""

#Function to draw the pitch
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import dataframe_image as dfi

#Size of the pitch in yards (!!!)
pitchLengthX=120
pitchWidthY=80

#ID for England vs Sweden Womens World Cup
match_id_required = 18245
home_team_required ="Real Madrid"
away_team_required ="Liverpool"

file_name=str(match_id_required)+'.json'

import json
with open('C:/Users/fares/OneDrive/Documentos/eecs 582/project/SoccerTact/'+file_name) as data_file:
    #print (mypath+'events/'+file)
    data = json.load(data_file)
    
#get the nested structure into a dataframe 
#store the dataframe in a dictionary with the match id as key (remove '.json' from string)
from pandas.io.json import json_normalize
df = json_normalize(data, sep = "_").assign(match_id = file_name[:-5])
gdp_dict = {home_team_required : [],
                'Match details': ['total_shots','total_passes','penalty_box_entry','shots_from_penalty_area','total_corners','total_freekicks'],
                away_team_required: []}

Liv_data =  df.loc[df['team_name'] == 'Liverpool'].set_index('id')
real_data =  df.loc[df['team_name'] == 'Real Madrid'].set_index('id')

new_df = real_data[real_data['location'].notna()]

def RealteamKPI():
    
    total_shots = 0
    total_passes = 0
    shots_from_penalty_area = 0; 
    penalty_box_entry = 0; 
    actions_PB = 0
    total_corners = 0
    total_freekicks = 0
    
    
    for i, events in new_df.iterrows():
         x = events['location'][0]
         y = events['location'][1]
   
         if(x > 102.0 and (y > 18.0 and y < 62.0)): 
            penalty_box_entry = penalty_box_entry + 1
            
            
            if (events['type_name'] == 'Shot'):
                shots_from_penalty_area = shots_from_penalty_area + 1
                
    
    for i, events in real_data.iterrows():
        
        if (events['type_name'] == "Shot"):
            total_shots = total_shots + 1
        elif (events['type_name'] == "Pass"):
            total_passes = total_passes + 1
            if (events['pass_type_name'] == "Corner"):
                total_corners = total_corners + 1
            if (events['pass_type_name'] == 'Free Kick'):
                total_freekicks = total_freekicks + 1
            
                
            
    gdp_dict[home_team_required].extend([total_shots,total_passes,penalty_box_entry,shots_from_penalty_area,total_corners,total_freekicks]) 
    print("=================")
    print("Real Madrid Stats")
    print("Total Shots " + str(total_shots))
    print("Total Passes " + str(total_passes))
    print("Penalty Box Entries " + str(penalty_box_entry))
    print("Shots from penalty area " + str(shots_from_penalty_area))
    print("Total Corners " + str(total_corners))
    print("Total Free Kicks " + str(total_freekicks))
    print("=================")

def LivteamKPI():
    
    total_shots = 0
    total_passes = 0
    shots_from_penalty_area = 0; 
    penalty_box_entry = 0; 
    actions_PB = 0
    total_corners = 0
    total_freekicks = 0
    
    for i, events in new_df.iterrows():
         x = events['location'][0]
         y = events['location'][1]
   
         if(x < 18 and (y > 18.0 and y < 62.0)): 
            penalty_box_entry = penalty_box_entry + 1
            if (events['type_name'] == 'Shot'):
                shots_from_penalty_area = shots_from_penalty_area + 1
                
    for i, events in Liv_data.iterrows():
        if (events['type_name'] == "Shot"):
            total_shots = total_shots + 1
        elif (events['type_name'] == "Pass"):
            total_passes = total_passes + 1
            if (events['pass_type_name'] == "Corner"):
                total_corners = total_corners + 1
            if (events['pass_type_name'] == 'Free Kick'):
                total_freekicks = total_freekicks + 1
    gdp_dict[away_team_required].extend([total_shots,total_passes,penalty_box_entry,shots_from_penalty_area,total_corners,total_freekicks])
    print("=================")
    print("Liverpool Stats")
    print("Total Shots " + str(total_shots))
    print("Total Passes " + str(total_passes))
    print("Penalty Box Entries " + str(penalty_box_entry))
    print("Shots from penalty area " + str(shots_from_penalty_area))
    print("Total Corners " + str(total_corners))
    print("Total Free Kicks " + str(total_freekicks))
    print("=================")

RealteamKPI()    
LivteamKPI()
data = pd.DataFrame(gdp_dict)
data = data. set_index([ home_team_required ,'Match details', away_team_required])
dfi.export(data, 'dataframe.png')