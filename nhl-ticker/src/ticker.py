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
        self.active = True

    def writeInitialScore(self):
        localStartTime = util.convertUtcDateTimeToLocal(self.game.getStartTime())

        gameDay = localStartTime.strftime("%A")[0:3]
        startTime = localStartTime.strftime("%H:%M")

        self.ledService.writeScore(self.game.getAwayTeam().getAbbreviation(), " ", self.game.getHomeTeam().getAbbreviation(), " ", gameDay, startTime)

    def processGameData(self):
        self.active = True

        isFirstLoop = True #Don't show goal animation on first loop
        while self.active is True:
            
            if util.isBeforeCurrentTime(self.game.getStartTime()):
                r = requests.get(self.game.getFeedUrl())
                gamedata = LiveGameData(r.json())
                    
                homeScore = gamedata.getHomeScore()
                awayScore = gamedata.getAwayScore()

                period = gamedata.getCurrentPeriod()
                periodTimeRemaining = gamedata.getPeriodTimeRemaining()

                refreshScore = False

                if (awayScore != self.game.getAwayTeam().getScore()):
                    self.game.getAwayTeam().setScore(awayScore)
                     refreshScore = True
                    if isFirstLoop is not true:
                        self.ledService.goalScored(self.game.getAwayTeam().getName())

                if (homeScore != self.game.getHomeTeam().getScore()):
                    self.game.getHomeTeam().setScore(homeScore)
                    refreshScore = True
                    if isFirstLoop is not true:
                        self.ledService.goalScored(self.game.getHomeTeam().getName())
                   
                
                if  refreshScore or (period is not None and self.game.getCurrentTime() != periodTimeRemaining):
                    self.game.setCurrentTime(periodTimeRemaining)
                    self.ledService.writeScore(self.game.getAwayTeam().getAbbreviation(), str(awayScore), self.game.getHomeTeam().getAbbreviation(), str(homeScore), period, periodTimeRemaining)
            
            time.sleep(3)

    def stopGame(self):
        self.active = False
        self.ledService.clearLed()


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

        self.game = Game(awayTeam, homeTeam, util.convertToUtcDatetime(utcStartTime), feedUrl)
        self.writeInitialScore()

        if (self.active is False):
            thread = Thread(target = self.processGameData)
            thread.start()

    def initGame(self, teamName):
        self.setGame(teamName)
        
        thread = Thread(target = self.processGameData)
        thread.start()

# Main function
if __name__ == "__main__":
    ticker = Ticker()
    ticker.initGame(str(team_constants.COL))