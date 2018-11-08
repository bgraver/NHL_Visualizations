import json, urllib.request
import pandas as pd


def load_nhl_csv(cursor, p_list):
    result = pd.io.json.json_normalize(p_list, 'data')
    result.to_csv('players_reg_season_2018.csv', sep=',', header=False, index=False)
    result.to_csv('players_reg_season_2018_header.csv', sep=',', index=False)
    cursor.execute("LOAD DATA LOCAL INFILE 'players_reg_season_2018.csv' INTO TABLE player_reg_season_2018 FIELDS TERMINATED BY ',' LINES TERMINATED BY '\r\n'")
    # print(type(result))


def load_nhl_shots_csv(cursor, shot_list):
    result = pd.io.json.json_normalize(shot_list, 'data')
    result.to_csv('shots_reg_season_2018.csv', sep=',', header=False, index=False)
    result.to_csv('shots_reg_season_2018_header.csv', sep=',', index=False)
    cursor.execute("LOAD DATA LOCAL INFILE 'shots_reg_season_2018.csv' INTO TABLE shots_reg_season_2018 FIELDS TERMINATED BY ',' LINES TERMINATED BY '\r\n'")


def load_nhl_teams_csv(cursor, team_list):
    result = pd.io.json.json_normalize(team_list, 'data')
    result.to_csv('team_reg_season_2018.csv', sep=',', header=False, index=False)
    result.to_csv('team_reg_season_2018_header.csv', sep=',', index=False)
    cursor.execute("LOAD DATA LOCAL INFILE 'team_reg_season_2018.csv' INTO TABLE teams_reg_season_2018 FIELDS TERMINATED BY ',' LINES TERMINATED BY '\r\n'")


def delete_tables(cursor):
    cursor.execute("DELETE FROM player_reg_season_2018")
    cursor.execute("DELETE FROM shots_reg_season_2018")
    cursor.execute("DELETE FROM teams_reg_season_2018")


def load_urls(PlayerList, PlayerShotsList, TeamList):
    with urllib.request.urlopen(PlayerList) as url:
        player_list = json.loads(url.read().decode())

    with urllib.request.urlopen(PlayerShotsList) as url:
        shot_list = json.loads(url.read().decode())

    with urllib.request.urlopen(TeamList) as url:
        team_list = json.loads(url.read().decode())

    return {'players': player_list, 'shots': shot_list, 'teams': team_list}


def load_credentials(file_name):
    f = open(file_name, 'r')
    l = f.readlines()
    f.close()
    return l
