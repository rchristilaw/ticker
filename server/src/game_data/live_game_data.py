class LiveGameData(object):
    def __init__(self, homeScore, awayScore, currentPeriod, periodTimeRemaining):
        self.homeScore = homeScore
        self.awayScore = awayScore
        self.currentPeriod = currentPeriod
        self.periodTimeRemaining = periodTimeRemaining

    def getHomeScore(self):
        return self.homeScore

    def getAwayScore(self):
        return self.awayScore

    def getCurrentPeriod(self):
        return self.currentPeriod

    def getPeriodTimeRemaining(self):
        return self.periodTimeRemaining  