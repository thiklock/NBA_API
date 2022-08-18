from nba_api.stats.static import players
import spark
import json
# Get all players.
players_ = players.get_players()


flat_people_list = [i for x in players_ for i in x]

print(flat_people_list)
# for i in players_:
#     i = i+i
#     print(i)

# print(type(players_))
# json_list = json.loads(players_)
# df = spark.read.json(sc.parallelize(players_))
# display(df)
