#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import json
import urllib2

class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="LEAFS SCORE!")

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../../fonts/9x15.bdf")
        textColor = graphics.Color(0, 0, 255)
        pos = offscreen_canvas.width
        my_text = self.args.text
        print "Before While Loop"

        loopCount = 0

        while (loopCount < 2):
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, 12, textColor, my_text)
            pos -= 1
            if (pos + len < 0):
                pos = offscreen_canvas.width
                loopCount += 1

            time.sleep(0.025)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


def pollNhlApi():
    homeScore = 1 
    awayScore = 0
    url = "http://statsapi.web.nhl.com/api/v1/teams/10?expand=team.schedule.next"

    run_text = RunText()

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
