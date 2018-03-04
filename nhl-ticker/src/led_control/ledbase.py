import argparse
import time
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/..'))
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from ledoptions import LedOptions


class LedBase(object):
    def usleep(self, value):
        time.sleep(value / 1000000.0)

    def run(selfm teamName):
        print("Running")

    def process(self, teamName):
        ledOptions = LedOptions()
        options = ledOptions.getOptions()

        self.matrix = RGBMatrix(options = options)

        try:
            # Start loop
            print("Press CTRL-C to stop sample")
            self.run(teamName)
        except KeyboardInterrupt:
            print("Exiting\n")
            sys.exit(0)

        return True
