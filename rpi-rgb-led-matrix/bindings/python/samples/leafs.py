#!/usr/bin/env python
# Display a runtext with double-buffering.
from goalLed import GoalLed

def pollNhlApi():
    homeScore = 1 
    awayScore = 0
    url = "http://statsapi.web.nhl.com/api/v1/teams/5?expand=team.schedule.next"

    goal_led = GoalLed()
    goal_led.process()

    print "Starting NHL API Poll"

    while True:
        content = urllib2.urlopen(url)
        teamdata = json.load(content)
        leafdata = teamdata['teams'][0]
        gamedata = leafdata['nextGameSchedule']['dates'][0]['games'][0]
        
        homescoreNew = gamedata['teams']['away']['score']
        awayscoreNew = gamedata['teams']['home']['score']

        if (awayscoreNew != awayScore):
            awayScore = awayscoreNew
            goal_led.process()
            print "Pens Scored"

        if (homescoreNew != homeScore):
            homeScore = homescoreNew
            goal_led.process()
            print "Bruins Scored"
        time.sleep(5)


# Main function
if __name__ == "__main__":
    pollNhlApi()
