#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 14:28:58 2022

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

real_shots = real_data.loc[real_data['type_name'] == 'Shot']

from FCPython import createPitch
(fig,ax) = createPitch(pitchLengthX,pitchWidthY,'yards','gray')

for i,shots in real_shots.iterrows():
    x=shots['location'][0]
    y=shots['location'][1]
    
    circleSize=2
    circleSize=np.sqrt(shots['shot_statsbomb_xg'])*8
    
    if shots['player_name']== 'Gareth Frank Bale':
        if (shots['shot_outcome_name']=='Goal'):
            shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="red")
        else:
            shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="red")     
            shotCircle.set_alpha(.3)
        ax.add_patch(shotCircle)

fig.set_size_inches(10, 7)
#fig.savefig('Output/passes.pdf', dpi=100)
plt.show()