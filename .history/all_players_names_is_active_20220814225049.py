from nba_api.stats.static import players
import spark
import json
import pandas as pd

import urllib.request

print(urllib.request.urlopen("nba.com").getcode())

def is_nba_up():

# Get all players.
players_ = players.get_players()

flat_people_list = [i for x in players_ for i in x]

print(len(flat_people_list))

df = pd.DataFrame (players_)

df.to_csv("./output.csv")

print(df)
