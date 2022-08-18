#Get the Pacers team_id
from nba_api.stats.static import teams

nba_teams = teams.get_teams()

# Select the dictionary for the Pacers, which contains their team ID
pacers = [team for team in nba_teams if team['abbreviation'] == 'IND'][0]
pacers_id = pacers['id']
print(f'pacers_id: {pacers_id}')