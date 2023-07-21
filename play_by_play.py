#Get the Pacers team_id
from nba_api.stats.static import teams

nba_teams = teams.get_teams()

# Query for the last regular season game where the Pacers were playing
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.library.parameters import Season
from nba_api.stats.library.parameters import SeasonType

gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=1610612737,
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
df.to_csv("landing_areagame_details.csv")
print(df.head()) #just looking at the head of the data