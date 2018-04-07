#!/usr/bin/env python
import urllib2
import json
import time
import requests
import platform

from common import util

from constants import url_constants
from constants import team_constants
from game_data import game_service
from game_data.team import Team
from led_service import LedService

from threading import Thread

class Ticker(object):
    def __init__(self):
        self.ledService = LedService()
        self.game = None
        self.active = False

    def writeInitialScore(self):
        localStartTime = util.convertUtcDateTimeToLocal(self.game.getStartTime())

        gameDay = localStartTime.strftime("%A")[0:3]
        startTime = localStartTime.strftime("%H:%M")

        self.ledService.writeScore(self.game.getAwayTeam().getAbbreviation(), " ", self.game.getHomeTeam().getAbbreviation(), " ", gameDay, startTime)

    def processGameData(self):
        self.active = True
        
        isFirstLoop = True #Don't show goal animation on first loop
        while self.active is True:
            
            # if util.isBeforeCurrentTime(self.game.getStartTime()):
            gamedata = self.game.getLiveGameData()
                
            homeScore = gamedata.getHomeScore()
            awayScore = gamedata.getAwayScore()

            period = gamedata.getCurrentPeriod()
            periodTimeRemaining = gamedata.getPeriodTimeRemaining()

            refreshScore = False

            if (awayScore != self.game.getAwayTeam().getScore()):
                self.game.getAwayTeam().setScore(awayScore)
                refreshScore = True
                if isFirstLoop is False:
                    self.ledService.goalScored(self.game.getAwayTeam().getName())

            if (homeScore != self.game.getHomeTeam().getScore()):
                self.game.getHomeTeam().setScore(homeScore)
                refreshScore = True
                if isFirstLoop is False:
                    self.ledService.goalScored(self.game.getHomeTeam().getName())
                
            
            if  refreshScore or (period is not None and self.game.getCurrentTime() != periodTimeRemaining):
                self.game.setCurrentTime(periodTimeRemaining)
                self.ledService.writeScore(self.game.getAwayTeam().getAbbreviation(), str(awayScore), self.game.getHomeTeam().getAbbreviation(), str(homeScore), period, periodTimeRemaining)
            
            isFirstLoop = False
            
            time.sleep(3)

    def stopGame(self):
        self.active = False
        self.ledService.clearLed()

    def activateGoalLight(self):
        self.ledService.goalScored(None)

    def setGame(self, teamName, league): 

        if (league == "MLB"):
            self.game = game_service.initMlbGame(teamName)              
        else:
            self.game = game_service.initNhlGame(teamName)    

        # self.writeInitialScore()

        if (self.active is False):
            thread = Thread(target = self.processGameData)
            thread.start()

    def initGame(self, teamName, league):
        self.setGame(teamName, league)
        
        thread = Thread(target = self.processGameData)
        thread.start()

# Main function
if __name__ == "__main__":
    ticker = Ticker()
    # ticker.initGame(str(team_constants.COL))
    ticker.initGame("Tigers", "MLB")
    #led = LedService()
