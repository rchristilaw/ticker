#!/usr/bin/env python
# Display a runtext with double-buffering.
import runtext
import time
import json
import urllib2


def pollNhlApi():
    homeScore = 1 
    awayScore = 0
    url = "http://statsapi.web.nhl.com/api/v1/teams/10?expand=team.schedule.next"

    run_text = runtext.RunText()

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
            run_text.process()
            print "Leafs Scored"

        if (homescoreNew != homeScore):
            homeScore = homescoreNew
            run_text.process()
            print "Panthers Scored"
        time.sleep(5)


# Main function
if __name__ == "__main__":
    pollNhlApi()
