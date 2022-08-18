from nba_api.stats.endpoints import playbyplayv2
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.library.parameters import Season
from nba_api.stats.library.parameters import SeasonType

import time
import logging

logging.basicConfig(filename='games.log', level=logging.INFO,datefmt='%Y-%m-%d %H:%M:%S', format='%(asctime)s %(levelname)-8s %(message)s' )
logging.info('Started')



logging.log(logging.WARNING, "another warning")

nba_teams = teams.get_teams()
# get_teams returns a list of 30 dictionaries, each an NBA team.
print(12*"-----")
ids_ = [ sub['id'] for sub in nba_teams ]

logging.log(logging.INFO, len(ids_))
logging.log(logging.INFO, ids_)

# Query for the last regular season game where the Pacers were playing
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.library.parameters import Season
from nba_api.stats.library.parameters import SeasonType

def main():
    logging.info('Started')
    for i in ids_:
        gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=i,
                                season_nullable=Season.default,
                                season_type_nullable=SeasonType.regular
                                )
        games_dict = gamefinder.get_normalized_dict()
        games = games_dict['LeagueGameFinderResults']
        game = games[0]
        game_id = game['GAME_ID']
        game_matchup = game['MATCHUP']
        time.sleep(1)
        # df.to_csv("./output_play_by_play.csv")
        logging.info(i)
        logging.info(f'Searching through {len(games)} game(s) for the game_id of {game_id} where {game_matchup}')

if __name__ == '__main__':
    main()