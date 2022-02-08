#Function to draw the pitch
import matplotlib.pyplot as plt
import numpy as np
from pyrsistent import b
from pandas import json_normalize
from FCPython import createPitch

def generate_shots(m_id,t1,t2,e_data,l_data):
    #Size of the pitch in yards (!!!)
    pitchLengthX=120
    pitchWidthY=80

    # get the nested structure into a dataframe 
    # store the dataframe in a dictionary with the match id as key (remove '.json' from string)
    df = json_normalize(e_data, sep = "_").assign(match_id = m_id)

    t1_data =  df.loc[df['team_name'] == t1].set_index('id')
    t2_data =  df.loc[df['team_name'] == t2].set_index('id')

    t1_shots = t1_data.loc[t1_data['type_name'] == 'Shot']
    t2_shots = t2_data.loc[t2_data['type_name'] == 'Shot']

    (fig1,ax1) = createPitch(pitchLengthX,pitchWidthY,'yards','gray')
    for i,shots in t1_shots.iterrows():
        x=shots['location'][0]
        y=shots['location'][1]
        
        circleSize=2
        circleSize=np.sqrt(shots['shot_statsbomb_xg'])*8
        
        if (shots['shot_outcome_name']=='Goal'):
            shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="red")
        else:
            shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="red")     
            shotCircle.set_alpha(.3)
        ax1.add_patch(shotCircle)

    fig1.set_size_inches(10, 7)
    plt.show()

    (fig2,ax2) = createPitch(pitchLengthX,pitchWidthY,'yards','gray')
    for i,shots in t2_shots.iterrows():
        x=shots['location'][0]
        y=shots['location'][1]
        
        circleSize=2
        circleSize=np.sqrt(shots['shot_statsbomb_xg'])*8
        
        if (shots['shot_outcome_name']=='Goal'):
            shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="blue")
        else:
            shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="blue")     
            shotCircle.set_alpha(.3)
        ax2.add_patch(shotCircle)

    fig2.set_size_inches(10, 7)
    #fig.savefig('Output/passes.pdf', dpi=100)
    plt.show()