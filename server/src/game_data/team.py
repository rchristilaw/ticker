class Team(object):
    def __init__(self, teamId, name, abbrev):
        self.teamId = teamId
        self.name = name
        self.abbreviation = abbrev
        self.score = 0

    def setScore(self, score):
        self.score = score

    def getScore(self):
        return self.score

    def getName(self):
        return self.name

    def getAbbreviation(self):
        return self.abbreviation
