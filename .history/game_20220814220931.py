from nba_api.stats.static import players

# Get all players.
players_ = players.get_players()

print(players_)