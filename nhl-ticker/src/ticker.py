#!/usr/bin/env python
import urllib2
import json
import time
import requests
import platform
#from dateutil.parser import parse

from constants import url_constants
from constants import team_constants
from game_data.game import Game
from game_data.team import Team


if (platform.system() == "Windows"):
    from goal_led_sim import GoalLed 
else:
    from led_control.goalLed import GoalLed


#def goalScored(teamId):




def getAndParseData(game, goal_led):

    r = requests.get(game.getFeedUrl())
    gamedata = r.json()
        
    homeScore = gamedata['liveData']['linescore']['teams']['home']['goals']
    awayScore = gamedata['liveData']['linescore']['teams']['away']['goals']
    

    periodData = gamedata['liveData']['linescore']
    period = periodData['currentPeriodOrdinal']
    periodTime = periodData['currentPeriodTimeRemaining']

    #score = "Score: %d - %d" % (homescoreNew, awayscoreNew)
        
    #print score

    refreshScore = False

    if (awayScore != game.getAwayTeam().getScore()):
        game.getAwayTeam().setScore(awayScore)
        goal_led.goalScored(game.getAwayTeam().getName())
        refreshScore = True

    if (homeScore != game.getHomeTeam().getScore()):
        game.getHomeTeam().setScore(homeScore)
        goal_led.goalScored(game.getHomeTeam().getName())
        refreshScore = True
    
    if (refreshScore or game.getCurrentTime() != periodTime):
        game.setCurrentTime(periodTime)
        goal_led.writeScore(game.getAwayTeam().getAbbreviation(), str(awayScore), game.getHomeTeam().getAbbreviation(), str(homeScore), period, periodTime)

def createTeam(teamData):
    teamId = teamData['id']
    teamName = teamData['teamName']
    teamAbbreviation = teamData['abbreviation']

    return Team(teamId, teamName, teamAbbreviation)

def pollLiveFeed(liveFeedUrl):
    feedUrl = url_constants.NHL_API_BASE_URL + liveFeedUrl

    r = requests.get(feedUrl)
    gameData = r.json()


    awayTeam = createTeam(gameData['gameData']['teams']['away'])
    homeTeam = createTeam(gameData['gameData']['teams']['home'])

    startTime = gameData['gameData']['datetime']['dateTime']

    #print parse(startTime)

    game = Game(awayTeam, homeTeam, startTime, feedUrl)

    goal_led = GoalLed()

    print "Starting NHL API Poll"
    
    #goal_led.writeScore(str(5), str(3))

    while True:
        getAndParseData(game, goal_led)
        time.sleep(3)

def initGame():

    url = url_constants.NHL_API_BASE_URL + "api/v1/teams/" + str(team_constants.WPG) + "?expand=team.schedule.next"
    r = requests.get(url)
    nextGame = r.json()

    liveFeedUrl = nextGame['teams'][0]['nextGameSchedule']['dates'][0]['games'][0]['link']

    #print liveFeedUrl

    pollLiveFeed(liveFeedUrl)

# Main function
if __name__ == "__main__":
    initGame() #pollNhlApi()
