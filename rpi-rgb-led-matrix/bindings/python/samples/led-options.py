import argparse
import time
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/..'))
from rgbmatrix import RGBMatrix, RGBMatrixOptions


class LedOptions(object):
    def getOptions():
        options = RGBMatrixOptions()

        options.hardware_mapping = "regular"
        options.rows = 16
        options.cols = 32
        options.chain_length = 2
        options.parallel = 1
        options.row_address_type = 0
        options.multiplexing = 0
        options.pwm_bits = 11
        options.brightness = 100
        options.pwm_lsb_nanoseconds = 130
        options.led_rgb_sequence = "RGB"
        options.show_refresh_rate = 0
        options.gpio_slowdown = 2
        options.disable_hardware_pulsing = False

        return options
