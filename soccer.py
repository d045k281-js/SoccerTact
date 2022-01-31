import imp
from flask import Flask, render_template
from flask import request
import TAApasses
app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        import matplotlib.pyplot as plt
        import numpy as np

#Size of the pitch in yards (!!!)
        pitchLengthX=120
        pitchWidthY=80

#ID for England vs Sweden Womens World Cup
#automation needed!!!!!
        match_id_required = 18245
        home_team_required ="Real Madrid"
        away_team_required ="Liverpool"

        file_name=str(match_id_required)+'.json'

        import json
        with open('/Users/deepak/Documents/SoccerTact/data/events/'+file_name) as data_file:
    #print (mypath+'events/'+file)
            data = json.load(data_file)
    
#get the nested structure into a dataframe 
#store the dataframe in a dictionary with the match id as key (remove '.json' from string)
            from pandas.io.json import json_normalize
            df = json_normalize(data, sep = "_").assign(match_id = file_name[:-5])

#Find the passes
            passes = df.loc[df['type_name'] == 'Pass'].set_index('id')

            from FCPython import createPitch
            (fig,ax) = createPitch(pitchLengthX,pitchWidthY,'yards','gray')
            for i,thepass in passes.iterrows():
    #if thepass['team_name']==away_team_required: automation here!!!!!!!!!#
                if thepass['player_name']=='Trent Alexander-Arnold':
                    x=thepass['location'][0]
                    y=thepass['location'][1]
                    passCircle=plt.Circle((x,pitchWidthY-y),2,color="blue")      
                    passCircle.set_alpha(.2)   
                    ax.add_patch(passCircle)
                    dx=thepass['pass_end_location'][0]-x
                    dy=thepass['pass_end_location'][1]-y

                    passArrow=plt.Arrow(x,pitchWidthY-y,dx,-dy,width=3,color="blue")
                    ax.add_patch(passArrow)

                fig.set_size_inches(10, 7)
##fig.savefig('Output/passes.pdf', dpi=100)
                fig.savefig('static/passes.png')
    return render_template('home.html')
if __name__ == '__main__':
    app.run(debug=True)