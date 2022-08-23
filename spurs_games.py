from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder

import time
import logging

logging.basicConfig(filename='spurs_games.log', level=logging.INFO,datefmt='%Y-%m-%d %H:%M:%S', format='%(asctime)s %(levelname)-8s %(message)s' )

def main():
    nba_teams = teams.get_teams()
    # Select the dictionary for the San Antonio Spurs, which contains their team ID
    spurs = [team for team in nba_teams if team['abbreviation'] == 'SAS'][0]
    spurs_id = spurs['id']
    # Query for games where the Celtics were playing
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=spurs_id)
    # The first DataFrame of those returned is what we want.
    games = gamefinder.get_data_frames()[0]
    games_in_request = len(games)
    logging.info(f'Games read: {games_in_request}')
    games.to_csv("./spurs_games.csv")




if __name__ == '__main__':
    main()