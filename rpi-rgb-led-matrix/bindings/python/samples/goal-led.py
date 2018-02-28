#!/usr/bin/env python
# Display a runtext with double-buffering.
from ledbase import LedBase
from rgbmatrix import graphics
import time


class GoalLed(LedBase):

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../../fonts/9x15.bdf")
        textColor = graphics.Color(0, 0, 255)
        pos = offscreen_canvas.width
        my_text = "Leafs Score"
        print "Before While Loop"
        while True:
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, 12, textColor, my_text)
            pos -= 1
            if (pos + len < 0):
                pos = offscreen_canvas.width

            time.sleep(0.025)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = GoalLed()
    run_text.process()
