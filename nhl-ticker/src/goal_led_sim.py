class GoalLed:
    def goalScored(self, teamName):
        print teamName + " score!"

    def writeScore(self, awayAbrv, awayScore, homeAbrv, homeScore, period, periodTime):
        print awayAbrv + " " + awayScore + "  " + period
        print homeAbrv + " " + homeScore + "  " + periodTime
