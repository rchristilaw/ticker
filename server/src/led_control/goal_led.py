#!/usr/bin/env python
# Display a runtext with double-buffering.

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/..'))
from rgbmatrix import graphics, RGBMatrix
from ledoptions import LedOptions


class GoalLed(object):
    def __init__(self):
        ledOptions = LedOptions()
        options = ledOptions.getOptions()
        self.matrix = RGBMatrix(options = options)

    def goalScored(self, teamName):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../rgblibrary/fonts/9x15.bdf")
        textColor = graphics.Color(0, 0, 255)
        pos = offscreen_canvas.width
        

        max_brightness = self.matrix.brightness
        count = 0

        while count < 3:
            self.matrix.Fill(255, 0, 0)
            time.sleep(.01)

            if self.matrix.brightness < 1:
                self.matrix.brightness = max_brightness
                count += 1
            else:
                self.matrix.brightness -= 1
        
        if teamName is not None:
            goalText = teamName + " Score!"
        else:
            goalText = "GOAL!"

        textCount = 0
        while textCount < 2:
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, 13, textColor, goalText)
            pos -= 1
            if (pos + len < 0):
                pos = offscreen_canvas.width
                textCount += 1

            time.sleep(0.02)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
    
    def writeScore(self, awayAbrv, awayScore, homeAbrv, homeScore, time, period):
        font = graphics.Font()
        font.LoadFont("../rgblibrary/fonts/5x8.bdf")
        canvas = self.matrix
        canvas.Clear()
        color = graphics.Color(255, 0, 0)
        graphics.DrawText(canvas, font, 1, 7, color, awayAbrv + " " + awayScore)
        graphics.DrawText(canvas, font, 1, 15, color, homeAbrv + " " + homeScore)

    def clearLed(self):
        canvas = self.matrix
        canvas.Clear()

        
    def happyStPats(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../rgblibrary/fonts/9x15.bdf")
        textColor = graphics.Color(0, 255, 0)
        pos = offscreen_canvas.width
        
        max_brightness = self.matrix.brightness
        count = 0

        while count < 4:
            self.matrix.Fill(0, 255, 0)
            time.sleep(.01)

            if self.matrix.brightness < 1:
                self.matrix.brightness = max_brightness
                count += 1
            else:
                self.matrix.brightness -= 1
        
        goalText = "Happy St. Patrick's Day!"

        textCount = 0
        while textCount < 2:
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, 13, textColor, goalText)
            pos -= 1
            if (pos + len < 0):
                pos = offscreen_canvas.width
                textCount += 1

            time.sleep(0.02)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
   
        count = 0

        while count < 4:
            self.matrix.Fill(0, 255, 0)
            time.sleep(.01)

            if self.matrix.brightness < 1:
                self.matrix.brightness = max_brightness
                count += 1
            else:
                self.matrix.brightness -= 1
