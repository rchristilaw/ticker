import requests
from live_game_data import LiveGameData
from game import Game

class NhlGame(Game):
    def __init__(self, awayTeam, homeTeam, startTime, feedUrl):
        self.feedUrl = feedUrl
        self.currentTime = "20:00"
        Game.__init__(self, awayTeam, homeTeam, startTime)

    def getLiveGameData(self):
        r = requests.get(self.feedUrl)

        gameJson = r.json()

        homeScore = gameJson['liveData']['linescore']['teams']['home']['goals']
        awayScore = gameJson['liveData']['linescore']['teams']['away']['goals']
        
        periodData = gameJson['liveData']['linescore']

        currentPeriod = None
        if 'currentPeriodOrdinal' in periodData:
            currentPeriod = periodData['currentPeriodOrdinal']

        periodTimeRemaining = None
        if 'currentPeriodTimeRemaining' in periodData:
            periodTimeRemaining = periodData['currentPeriodTimeRemaining']

        return LiveGameData(homeScore, awayScore, currentPeriod, periodTimeRemaining)
