from nba_api.stats.static import players
import spark
# Get all players.
players_ = players.get_players()

# print(players_)

import spark.implicits._
# val jsonStr = """{ "metadata": { "key": 84896, "value": 54 }}"""
df = spark.read.json(Seq(players_).toDS)