from nba_api.stats.static import players
import spark
import json
# Get all players.
players_ = players.get_players()


json_list = json.loads(players_)
df = spark.read.json(sc.parallelize(json_list))
# display(df)
