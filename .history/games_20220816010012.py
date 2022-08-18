from nba_api.stats.endpoints import playbyplayv2
game_id = "0021701171"
pbp = playbyplayv2.PlayByPlayV2(game_id)
pbp = pbp.get_data_frames()[0]
print(pbp.head())

from nba_api.stats.static import teams

nba_teams = teams.get_teams()

from nba_api.stats.static import teams
# get_teams returns a list of 30 dictionaries, each an NBA team.

print(12*"-----")
ids_ = [ sub['id'] for sub in nba_teams ]

print(ids_)

# Query for the last regular season game where the Pacers were playing
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.library.parameters import Season
from nba_api.stats.library.parameters import SeasonType
