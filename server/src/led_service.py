import platform

if (platform.system() != "Linux"):
    from led_control.goal_led_sim import GoalLed 
else:
    from led_control.goal_led import GoalLed

class LedService(object):
    def __init__(self):
        self.goalLed = GoalLed()
    
    def writeScore(self, awayAbrv, awayScore, homeAbrv, homeScore, period, periodTime):
        self.goalLed.writeScore(awayAbrv, awayScore, homeAbrv, homeScore, period, periodTime)

    def goalScored(self, teamName):
        self.goalLed.goalScored(teamName)

    def clearLed(self):
        self.goalLed.clearLed()

    def happyStPats(self):
        self.goalLed.happyStPats()
