#!/usr/bin/env python
import urllib2
import json
import time
import requests
import platform

import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/../../../nhlapi/data'))
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/../../../nhlapi/nhlapi'))
from nhlapi import NhlApi

from common import util

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
        self.active = False
        self.nhl = NhlApi()

    def writeInitialScore(self):
        localStartTime = util.convertUtcDateTimeToLocal(self.game.getStartTime())

        gameDay = localStartTime.strftime("%A")[0:3]
        startTime = localStartTime.strftime("%H:%M")

        self.ledService.writeScore(self.game.getAwayTeam().getAbbreviation(), " ", self.game.getHomeTeam().getAbbreviation(), " ", gameDay, startTime)

    def processGameData(self):
        self.active = True
        
        isFirstLoop = True #Don't show goal animation on first loop
        while self.active is True:
            self.game = self.nhl.getUpdatedGame(self.game)

            if (self.game.getHasChanges() is True):
                self.ledService.writeScore(self.game.getAwayTeam().getAbbreviation(), str(self.game.getAwayTeam().getScore()), self.game.getHomeTeam().getAbbreviation(), str(self.game.getHomeTeam().getScore()), self.game.getPeriod(), self.game.getCurrentTime())
                
                # isFirstLoop = False
            
            time.sleep(3)

    def stopGame(self):
        self.active = False
        self.ledService.clearLed()

    def activateGoalLight(self):
        self.ledService.goalScored(None)

    def setGame(self, teamName): 
        self.game = self.nhl.getNextGameForTeam(teamName)
        self.writeInitialScore()

        if (self.active is False):
            thread = Thread(target = self.processGameData)
            thread.daemon = True
            thread.start()

    def initGame(self, teamName):
        self.setGame(teamName)
#        thread = Thread(target = self.processGameData)
#        thread.start()

# Main function
if __name__ == "__main__":
    ticker = Ticker()
<<<<<<< HEAD
    ticker.initGame("TOR")
    # led = LedService()
    # led.happyStPats()
    # print sys.path
    
    # print nhl.getTeamsList()
=======
    ticker.initGame(str(team_constants.TOR))
    #led = LedService()
    #led.happyStPats()
>>>>>>> Ticker mods for broken board panel
