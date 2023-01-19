import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
# from matplotlib import pyplot as plt
# from pandas.plotting import scatter_matrix


MyInternationalData = pd.read_csv('international_matches.csv')


def createList():
    global MyInternationalData
    Teams = MyInternationalData['home_team']
    FIFARank = MyInternationalData['home_team_fifa_rank']
    FIFAPoints = MyInternationalData['home_team_total_fifa_points']
    TeamsForProcess = list(zip(Teams , FIFARank , FIFAPoints))
    TeamsForProcess.reverse()
    return TeamsForProcess
TeamsForProcess = createList()

def Versus(home , away , Teams):
    homebool = 0
    awaybool = 0
    hometeam = ()
    awayteam = ()
    for i in Teams:
        if(homebool == 0):
            if(i[0] == home):
                homebool = 1
                hometeam = i
        if(awaybool == 0):
             if(i[0] == away):
                awaybool = 1
                awayteam = i
        if(awaybool and homebool == 1 ):
            return hometeam , awayteam
def Predict(Home , Away ,Teams):
    global MyInternationalData
    x = MyInternationalData.drop(columns=['home_team_continent' ,'away_team_continent', 
    'home_team' , 'away_team' ,'home_team_score' ,	'away_team_score' , 'home_team_result' , 'date' , 'tournament' ,	'city' ,
    'country' , 'neutral_location' ,	'shoot_out' , 'home_team_goalkeeper_score'	,'away_team_goalkeeper_score'	,
    'home_team_mean_defense_score'	,'home_team_mean_offense_score'	,'home_team_mean_midfield_score'	,'away_team_mean_defense_score'	,
    'away_team_mean_offense_score',	'away_team_mean_midfield_score'])
    y = MyInternationalData['home_team_result']

    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    model = KNeighborsClassifier(n_neighbors=42)
    fit = model.fit(X_train, Y_train)
    result = model.predict(X_test)
    accuracyScore = accuracy_score(Y_test , result)
    home , away = Versus(Home , Away , Teams)
    result = model.predict(
    [[
    home[1] , away[1] , home[2] ,away[2]
    ]]
    )
    return result
    # print(accuracyScore)

# MyInternationalData =  MyInternationalData.drop(columns=['home_team_continent' ,'away_team_continent', 
#     'home_team' , 'away_team' ,'home_team_score' ,	'away_team_score' , 'home_team_result' , 'date' , 'tournament' ,	'city' ,
#     'country' , 'neutral_location' ,	'shoot_out' , 'home_team_goalkeeper_score'	,'away_team_goalkeeper_score'	,
#     'home_team_mean_defense_score'	,'home_team_mean_offense_score'	,'home_team_mean_midfield_score'	,'away_team_mean_defense_score'	,
#     'away_team_mean_offense_score',	'away_team_mean_midfield_score'])
# scatter_matrix(MyInternationalData, figsize=(12, 8))
# MyInternationalData.plot()
# plt.show()

#print Accuracy
# Predict("" , "" , TeamsForProcess )


