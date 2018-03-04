class Game:
    def __init__(self, awayTeam, homeTeam, startTime, feedUrl):
        self.awayTeam = awayTeam
        self.homeTeam = homeTeam
        self.startTime = startTime
        self.feedUrl = feedUrl

    def getHomeTeam(self):
        return self.homeTeam

    def getAwayTeam(self):
        return self.awayTeam

    def getStartTime(self):
        return self.startTime

    def getFeedUrl(self):
        return self.feedUrl