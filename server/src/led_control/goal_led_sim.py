class GoalLed:
    def goalScored(self, teamName):
        if teamName is not None:
            print teamName + " score!"
        else:
            print "GOAL!"

    def writeScore(self, awayAbrv, awayScore, homeAbrv, homeScore, period, periodTime):
        print awayAbrv + " " + awayScore + "  " + period
        print homeAbrv + " " + homeScore + "  " + periodTime

    def clearLed(self):
        print "Clear LED Screen"

    def happyStPats(self):
        print "Happy St Pats"
