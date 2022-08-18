from nba_api.stats.static import players
import spark
import json
import pandas as pd

import urllib.request

def get_nba_stat():
    code = urllib.request.urlopen("https://www.nba.com/stats/").getcode() 
    print(code)
    return code

# Get all players.
def get_players():
    players_ = players.get_players()
    # count amount of players
    flat_people_list = [i for x in players_ for i in x]
    print(len(flat_people_list))
    return players_

def save_players(resposta):
    df = pd.DataFrame (resposta)
    df.to_csv("./output.csv")
    print(df)
    return

get_nba_stat()

save_players(get_players())