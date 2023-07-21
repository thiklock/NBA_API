import pandas as pd
from nba_api.stats.static import teams

# Get the list of NBA teams
nba_teams = teams.get_teams()

# Create a list of teams with the team name and team_id
team_list = []
for team in nba_teams:
    team_list.append({
        "name": team["full_name"],
        "team_id": team["id"],
    })
    print(team["full_name"] , team["id"] )

# Convert the team list to a Pandas DataFrame
df = pd.DataFrame(team_list)

# Save the DataFrame to a Parquet file
df.to_parquet('landing_area/team_list.parquet', index=False)
 # Save the DataFrame to a JSON file
df.to_json(r'landing_area/team_list.json')
