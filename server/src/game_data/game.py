import requests
from live_game_data import LiveGameData

class Game(object):
    def __init__(self, awayTeam, homeTeam, startTime):
        self.awayTeam = awayTeam
        self.homeTeam = homeTeam
        self.startTime = startTime
        self.currentTime = "20:00"

    def getHomeTeam(self):
        return self.homeTeam

    def getAwayTeam(self):
        return self.awayTeam

    def getStartTime(self):
        return self.startTime

    def getCurrentTime(self):
        return self.currentTime

    def setCurrentTime(self, time):
        self.currentTime = time