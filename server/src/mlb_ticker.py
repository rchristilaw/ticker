#!/usr/bin/env python
import urllib2
import json
import time
import requests
import platform
import mlbgame

from common import util

from constants import url_constants
from constants import team_constants
from game_data.game import Game
from game_data.team import Team
from game_data.live_game_data import LiveGameData
from led_service import LedService

from threading import Thread

class Ticker(object):
    def __init__(self):
        self.ledService = LedService()
        self.game = None
        self.active = False



    def getData(self):
        # url = "http://gd2.mlb.com/components/game/mlb/year_2018/month_04/day_07/master_scoreboard.json"
        # r = requests.get(url)
        # scoreboard = r.json()

        # print scoreboard

        # month = mlbgame.games(2018, 4, home='Blue Jays')
        # games = mlbgame.combine_games(month)
        # for game in games:
        #     print(game)

        # day = mlbgame.day(2015, 4, 12, home='Royals', away='Royals')
        # game = day[0]
        # output = 'Winning pitcher: %s (%s) - Losing Pitcher: %s (%s)'
        # print(output % (game.w_pitcher, game.w_team, game.l_pitcher, game.l_team))

        # teams = mlbgame.teams()

        # for team in teams:
        #     print team

        game = mlbgame.day(2018, 4, 7, "Yankees", "Yankees")

        print game[0].game_id

        print game[0].game_start_time

        overview = mlbgame.overview(game[0].game_id)

        print overview.inning_state + " " + str(overview.inning)

        print str(overview.outs) + " OUTS"

        


# Main function
if __name__ == "__main__":
    ticker = Ticker()
    ticker.getData()
    # ticker.initGame(str(team_constants.COL))
    #led = LedService()
