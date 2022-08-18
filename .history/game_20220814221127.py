from nba_api.stats.static import players

# Get all players.
players_ = players.get_players()

print(players_)

# >>> data = [ { "a": "01", "b": "teste01" }, { "a": "02", "b": "teste02" } ]
df = spark.createDataFrame(players_)
>>> df.write.parquet("data.parquet")