from nba_api.stats.static import players
import spark
# Get all players.
players_ = players.get_players()


json_list = []

df = spark.read.json(sc.parallelize(json_list))
display(df)
