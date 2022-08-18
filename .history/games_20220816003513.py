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
nba_teams = teams.get_teams()
print('Number of teams fetched: {}'.format(len(nba_teams)))
nba_teams[:3]
print(type(nba_teams))

for i in nba_teams:
    print(i)
print(12*"-----")
print(nba_teams[1])
print(12*"-----")
for key, val in nba_teams[1].items():
    print("{} : {}".format(key, val))
print(12*"-----")
for i in nba_teams:
    for key in i.keys():
        print(key)
print(12*"-----")

print(*[key for i in nba_teams for key in i.keys()], sep = "\n")

print(12*"-----")
print(nba_teams)

for i in range(len(nba_teams)):
    print(i.values)