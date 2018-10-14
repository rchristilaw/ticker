#!/usr/bin/env python

from led_service import LedService



# Main function
if __name__ == "__main__":
    #ticker = Ticker()
    # ticker.initGame(str(team_constants.COL))
    #ticker.initGame("Tigers", "MLB")
    led = LedService()
    led.clearLed()
