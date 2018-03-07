class Team(object):
    def __init__(self, teamData):
        self.teamId = teamData['id']
        self.name = teamData['teamName']
        self.abbreviation = teamData['abbreviation']
        self.score = 0

    def setScore(self, score):
        self.score = score

    def getScore(self):
        return self.score

    def getName(self):
        return self.name

    def getAbbreviation(self):
        return self.abbreviation
