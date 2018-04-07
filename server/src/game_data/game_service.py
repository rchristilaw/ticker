import requests
import mlbgame

from nhl_game import NhlGame
from mlb_game import MlbGame
from game_data.team import Team

from common import util

from constants import url_constants
from constants import team_constants


def initMlbGame(teamName):
    game = mlbgame.day(2018, 4, 7, teamName, teamName)

    startTime = game[0].game_start_time
    gameId = game[0].game_id

    overview = mlbgame.overview(gameId)

    awayTeam = Team(overview.away_team_id, overview.away_team_name, overview.away_name_abbrev)
    homeTeam = Team(overview.home_team_id, overview.home_team_name, overview.home_name_abbrev)

    return MlbGame(awayTeam, homeTeam, startTime, gameId)

def initNhlGame(teamName):
    url = url_constants.NHL_API_BASE_URL + "api/v1/teams/" + teamName + "?expand=team.schedule.next"

    r = requests.get(url)
    nextGame = r.json()

    liveFeedUrl = nextGame['teams'][0]['nextGameSchedule']['dates'][0]['games'][0]['link']
    feedUrl = url_constants.NHL_API_BASE_URL + liveFeedUrl

    r = requests.get(feedUrl)
    gameData = r.json()

    awayTeam = createTeamFromNhlJson(gameData['gameData']['teams']['away'])
    homeTeam = createTeamFromNhlJson(gameData['gameData']['teams']['home'])
    utcStartTime = gameData['gameData']['datetime']['dateTime']

    return NhlGame(awayTeam, homeTeam, util.convertToUtcDatetime(utcStartTime), feedUrl)

def createTeamFromNhlJson(jsonData):
    teamId = jsonData['id']
    name = jsonData['teamName']
    abbreviation = jsonData['abbreviation']
    return Team(teamId, name, abbreviation)
            