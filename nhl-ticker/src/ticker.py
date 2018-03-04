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
        
    homescoreNew = gamedata['liveData']['linescore']['teams']['away']['goals']
    awayscoreNew = gamedata['liveData']['linescore']['teams']['home']['goals']
        
    score = "Score: %d - %d" % (homescoreNew, awayscoreNew)
        
    print score

    if (awayscoreNew != game.getAwayTeam().getScore()):
       game.getAwayTeam().setScore(awayscoreNew)
       goal_led.process(game.getAwayTeam().getName())

    if (homescoreNew != game.getHomeTeam().getScore()):
       game.getHomeTeam().setScore(homescoreNew)
       goal_led.process(game.getHomeTeam().getName())

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

    while True:
        getAndParseData(game, goal_led)
        time.sleep(3)

def initGame():

    url = url_constants.NHL_API_BASE_URL + "api/v1/teams/" + str(team_constants.NSH) + "?expand=team.schedule.next"
    r = requests.get(url)
    nextGame = r.json()

    liveFeedUrl = nextGame['teams'][0]['nextGameSchedule']['dates'][0]['games'][0]['link']

    #print liveFeedUrl

    pollLiveFeed(liveFeedUrl)

# Main function
if __name__ == "__main__":
    initGame() #pollNhlApi()
