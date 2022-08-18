from nba_api.stats.static import players
import spark
# Get all players.
players_ = players.get_players()

# print(players_)

# newJson = '{"Name":"something","Url":"https://stackoverflow.com","Author":"jangcy","BlogEntries":100,"Caller":"jangcy"}'
df = spark.read.json(sc.parallelize([players_]))
df.show(truncate=False)