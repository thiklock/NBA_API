from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder


def main():
    nba_teams = teams.get_teams()
    # Select the dictionary for the San Antonio Spurs, which contains their team ID
    spurs = [team for team in nba_teams if team['abbreviation'] == 'SAS'][0]
    spurs_id = spurs['id']
    # Query for games where the Celtics were playing
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=spurs_id)
    # The first DataFrame of those returned is what we want.
    games = gamefinder.get_data_frames()[0]
    print(games.head())
    print(spurs_id)

if __name__ == '__main__':
    main()