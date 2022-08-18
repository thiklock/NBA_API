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

# Query for the last regular season game where the Pacers were playing
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.library.parameters import Season
from nba_api.stats.library.parameters import SeasonType

pacers_id = "1610612737"

gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=pacers_id,
                            season_nullable=Season.default,
                            season_type_nullable=SeasonType.regular)  

games_dict = gamefinder.get_normalized_dict()
games = games_dict['LeagueGameFinderResults']
game = games[0]
game_id = game['GAME_ID']
game_matchup = game['MATCHUP']

print(f'Searching through {len(games)} game(s) for the game_id of {game_id} where {game_matchup}')

# Query for the play by play of that most recent regular season game
from nba_api.stats.endpoints import playbyplay
df = playbyplay.PlayByPlay(game_id).get_data_frames()[0]
df.to_csv("./output.csv")
print(df.head()) #just looking at the head of the data