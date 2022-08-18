from nba_api.stats.static import players
import spark
# Get all players.
players_ = players.get_players()

# print(players_)

tsRDD = sc.parallelize([ts])
df = spark.read.option('multiline', "true").json(tsRDD)