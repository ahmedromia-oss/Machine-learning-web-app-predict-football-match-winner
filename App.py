import flask
import requests
import pandas as pd
from Models.HomeAwayModel import HomeAwayModel
from predict import createList , Predict

MyInternationalData = pd.read_csv('international_matches.csv')

Teams = createList()

app = flask.Flask(__name__)

teams = ['Egypt' ,'Qatar', 'Ecuador', 'Senegal', 'Netherlands',
'Italy', 'Algeria',
'Argentina', 'Saudi Arabia', 'Mexico', 'Poland',
'France', 'Denmark', 'Tunisia',
'Spain', 'Costa Rica', 'Germany', 'Japan',
'Belgium', 'Canada', 'Morocco', 'Croatia',
'Brazil', 'Serbia', 'Switzerland', 'Cameroon',
'Portugal', 'Ghana', 'Uruguay']
@app.route("/Match/<HomeTeam>-<AwayTeam>" , methods=['GET', 'POST'])
def Match(HomeTeam , AwayTeam):
            if(flask.request.method == "POST"):
                homeAwayModel=HomeAwayModel()
                homeAwayModel.HomeTeam = HomeTeam
                homeAwayModel.AwayTeam = AwayTeam
                
                try:
                    HomeFlag = requests.get(f"https://restcountries.com/v3.1/name/{HomeTeam}?fullText=true").json()
                    HomeFlag =   "https://flagcdn.com/192x144/" + (HomeFlag[0]['flags']['png']).split("w320/")[1]

                except:
                    HomeFlag = "static/Images/NotFound.jpg"
        
                try:
                    AwayFlag = requests.get(f"https://restcountries.com/v3.1/name/{AwayTeam}?fullText=true").json()
                    AwayFlag ="https://flagcdn.com/192x144/" + (AwayFlag[0]['flags']['png']).split("w320/")[1]     

                except:
                    AwayFlag = "static/Images/NotFound.jpg"

                homeAwayModel.HomeFlag = HomeFlag
                homeAwayModel.AwayFlag = AwayFlag
                
            return {
                    "homeTeam":homeAwayModel.HomeTeam,
                    "AwayTeam":homeAwayModel.AwayTeam,
                    "homeFlag":homeAwayModel.HomeFlag,
                    "AwayFlag":homeAwayModel.AwayFlag
            }
        
@app.route("/predict/<HomeTeam>-<AwayTeam>" , methods=['GET', 'POST'])
def predict(HomeTeam , AwayTeam):
        if(flask.request.method == "POST"):
            result = Predict(HomeTeam , AwayTeam , Teams)
            if(result == ["Win"]):
                return "Home"
            else:
                return "Away"
                
@app.route("/")
def index():
    
        HomeTeam = "Egypt"
        AwayTeam = "Egypt"
        try:
            HomeFlag = requests.get(f"https://restcountries.com/v3.1/name/{HomeTeam}?fullText=true").json()
            HomeFlag =   "https://flagcdn.com/192x144/" + (HomeFlag[0]['flags']['png']).split("w320/")[1]

        except:
            HomeFlag = "static/Images/NotFound.jpg"
        
        try:
            AwayFlag = requests.get(f"https://restcountries.com/v3.1/name/{AwayTeam}?fullText=true").json()
            AwayFlag ="https://flagcdn.com/192x144/" + (AwayFlag[0]['flags']['png']).split("w320/")[1]     

        except:
            AwayFlag = "static/Images/NotFound.jpg"
        return flask.render_template("index.html" ,
            HomeTeam =HomeTeam,
            AwayTeam = AwayTeam,
            HomeFlag = HomeFlag,
            AwayFlag = AwayFlag,
            teams = teams
        )
