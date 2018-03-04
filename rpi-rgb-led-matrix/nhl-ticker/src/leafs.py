#!/usr/bin/env python
# Display a runtext with double-buffering.
#from goalLed import GoalLed
import urllib2
import json
import time
import requests


#def goalScored(teamId):




def getAndParseData(url, goal_led):

    r = requests.get(url)
    teamdata = r.json()
    # content = urllib2.urlopen(url)

    #with open(content) as data:
            
    #teamdata = json.load(data)
    #content.close()

    leafdata = teamdata['teams'][0]
    gamedata = leafdata['nextGameSchedule']['dates'][0]['games'][0]
        
    homescoreNew = gamedata['teams']['away']['score']
    awayscoreNew = gamedata['teams']['home']['score']
        
    score = "Score: %d - %d" % (homescoreNew, awayscoreNew)
        
    print score


    if (awayscoreNew != awayScore):
       awayScore = awayscoreNew
       #goal_led.process()
       print "Pens Scored"

    if (homescoreNew != homeScore):
       homeScore = homescoreNew
       #goal_led.process()
       print "Bruins Scored"



def pollNhlApi():
    homeScore = 1 
    awayScore = 3
    url = "http://statsapi.web.nhl.com/api/v1/teams/5?expand=team.schedule.next"

    goal_led = "TEST" #GoalLed()

    print "Starting NHL API Poll"

    while True:
        getAndParseData(url, goal_led)
        time.sleep(3)


# Main function
if __name__ == "__main__":
    pollNhlApi()
