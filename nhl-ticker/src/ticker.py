#!/usr/bin/env python
import urllib2
import json
import time
import requests
import platform

import util

from constants import url_constants
from constants import team_constants
from game_data.game import Game
from game_data.team import Team
from game_data.live_game_data import LiveGameData
from led_service import LedService

from threading import Thread

class Ticker(object):
    def __init__(self):
        self.ledService = LedService()
        self.game = None

    def writeInitialScore(self):
        gameDay = self.game.getStartTime().strftime("%A")[0:3]
        startTime = self.game.getStartTime().strftime("%H:%M")
        self.ledService.writeScore(self.game.getAwayTeam().getAbbreviation(), " ", self.game.getHomeTeam().getAbbreviation(), " ", gameDay, startTime)

    def getAndParseData(self):
        
        while True:
            if util.isBeforeCurrentTime(self.game.getStartTime()):
                r = requests.get(self.game.getFeedUrl())
                gamedata = LiveGameData(r.json())
                    
                homeScore = gamedata.getHomeScore()
                awayScore = gamedata.getAwayScore()

                period = gamedata.getCurrentPeriod
                periodTimeRemaining = gamedata.getPeriodTimeRemaining()

                refreshScore = False

                if (awayScore != self.game.getAwayTeam().getScore()):
                    self.game.getAwayTeam().setScore(awayScore)
                    self.ledService.goalScored(self.game.getAwayTeam().getName())
                    refreshScore = True

                if (homeScore != self.game.getHomeTeam().getScore()):
                    self.game.getHomeTeam().setScore(homeScore)
                    self.ledService.goalScored(self.game.getHomeTeam().getName())
                    refreshScore = True
                
                if  refreshScore or (period is not None and self.game.getCurrentTime() != periodTimeRemaining):
                    self.game.setCurrentTime(periodTimeRemaining)
                    self.ledService.writeScore(self.game.getAwayTeam().getAbbreviation(), str(awayScore), self.game.getHomeTeam().getAbbreviation(), str(homeScore), period, periodTimeRemaining)
            
            time.sleep(3)

    def setGame(self, teamName): 
        url = url_constants.NHL_API_BASE_URL + "api/v1/teams/" + teamName + "?expand=team.schedule.next"

        r = requests.get(url)
        nextGame = r.json()

        liveFeedUrl = nextGame['teams'][0]['nextGameSchedule']['dates'][0]['games'][0]['link']
        feedUrl = url_constants.NHL_API_BASE_URL + liveFeedUrl

        r = requests.get(feedUrl)
        gameData = r.json()

        awayTeam = Team(gameData['gameData']['teams']['away'])
        homeTeam = Team(gameData['gameData']['teams']['home'])
        utcStartTime = gameData['gameData']['datetime']['dateTime']

        startTime = util.convertUtcDateTimeToLocal(utcStartTime)

        self.game = Game(awayTeam, homeTeam, startTime, feedUrl)
        self.writeInitialScore()

    def initGame(self, teamName):
        self.setGame(teamName)
        
        thread = Thread(target = self.getAndParseData)
        thread.start()
        # thread.join()
        # self.getAndParseData()

# Main function
if __name__ == "__main__":
    ticker = Ticker()
    ticker.initGame(str(team_constants.TOR))