from nba_api.stats.endpoints import playbyplayv2
pbp = playbyplayv2.PlayByPlayV2(game_id)
pbp = pbp.get_data_frames()[0]
pbp.head()