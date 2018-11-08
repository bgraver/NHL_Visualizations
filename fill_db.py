from helper_functions import load_nhl_teams_csv, load_nhl_csv, load_urls, load_nhl_shots_csv, delete_tables, load_credentials
import mysql.connector as mariadb


#Useful URLs to use later
TeamList = "http://www.nhl.com/stats/rest/team?isAggregate=false&reportType=basic&isGame=false&reportName=teamsummary&sort=[{%22property%22:%22points%22,%22direction%22:%22DESC%22},{%22property%22:%22wins%22,%22direction%22:%22DESC%22}]&cayenneExp=gameTypeId=2%20and%20seasonId%3E=20182019%20and%20seasonId%3C=20182019"
HawksRoster = "https://statsapi.web.nhl.com/api/v1/teams/16/roster" #examples
HawksStats = "https://statsapi.web.nhl.com/api/v1/teams/16/stats" #examples
HawksInDepthRoster = "http://www.nhl.com/stats/rest/skaters?isAggregate=false&reportType=basic&isGame=false&reportName=skatersummary&sort=[{%22property%22:%22points%22,%22direction%22:%22DESC%22},{%22property%22:%22goals%22,%22direction%22:%22DESC%22},{%22property%22:%22assists%22,%22direction%22:%22DESC%22}]&factCayenneExp=gamesPlayed%3E=1&cayenneExp=gameTypeId=%222%22%20and%20seasonId%3E=20172018%20and%20seasonId%3C=20172018%20and%20teamId=16"
PlayerList = "http://www.nhl.com/stats/rest/skaters?isAggregate=false&reportType=basic&isGame=false&reportName=skatersummary&sort=[{%22property%22:%22points%22,%22direction%22:%22DESC%22},{%22property%22:%22goals%22,%22direction%22:%22DESC%22},{%22property%22:%22assists%22,%22direction%22:%22DESC%22}]&cayenneExp=gameTypeId=2%20and%20seasonId%3E=20182019%20and%20seasonId%3C=20182019"
PlayerShotsList = "http://www.nhl.com/stats/rest/skaters?isAggregate=false&reportType=shooting&isGame=false&reportName=skatersummaryshooting&sort=[{%22property%22:%22shotAttempts%22,%22direction%22:%22DESC%22}]&cayenneExp=gameTypeId=2%20and%20seasonId%3E=20182019%20and%20seasonId%3C=20182019"
#need to change the teamId at the very end to change what team it is
GoalieList = "http://www.nhl.com/stats/rest/goalies?isAggregate=false&reportType=goalie_basic&isGame=false&reportName=goaliesummary&sort=[{%22property%22:%22wins%22,%22direction%22:%22DESC%22}]&cayenneExp=gameTypeId=%222%22%20and%20seasonId%3E=20172018%20and%20seasonId%3C=20172018"
#95 total goalies in the list


# print(player_list)
'''
with urllib.request.urlopen(GoalieList) as url:  # getting the info into a dictionary
    goalie_data = json.loads(url.read().decode())
'''
credentials = load_credentials('.gitignore')

mariadb_connection = mariadb.connect(user=credentials[0], password=credentials[1], database=credentials[2])
cursor = mariadb_connection.cursor()

delete_tables(cursor)
d = load_urls(PlayerList, PlayerShotsList, TeamList)
load_nhl_csv(cursor, d['players'])
load_nhl_shots_csv(cursor, d['shots'])
load_nhl_teams_csv(cursor, d['teams'])

mariadb_connection.commit()
mariadb_connection.close()
