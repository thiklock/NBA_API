from nba_api.stats.endpoints import playbyplayv2
game_id = "0021701171"
pbp = playbyplayv2.PlayByPlayV2(game_id)
pbp = pbp.get_data_frames()[0]
print(pbp.head())

from nba_api.stats.static import teams

nba_teams = teams.get_teams()
# Select the dictionary for the Celtics, which contains their team ID
celtics = [team for team in nba_teams if team['abbreviation'] == 'BOS'][0]
celtics_id = celtics['id']

from nba_api.stats.static import teams
# get_teams returns a list of 30 dictionaries, each an NBA team.

print(12*"-----")
ids_ = [ sub['id'] for sub in nba_teams ]