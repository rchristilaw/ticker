import mlbgame
from live_game_data import LiveGameData
from game import Game

class MlbGame(Game):
    def __init__(self, awayTeam, homeTeam, startTime, gameId):
        Game.__init__(self, awayTeam, homeTeam, startTime)
        self.currentTime = "TOP 1"
        self.gameId = gameId

    def getLiveGameData(self):

        game = mlbgame.overview(self.gameId)
            # (2018, 4, 6, "Blue Jays", "Blue Jays")

        homeScore = game.home_team_runs
        awayScore = game.away_team_runs

        currentPeriod = game.inning_state + " " + str(game.inning)

        periodTimeRemaining = str(game.outs) +  " OUTS"

        return LiveGameData(homeScore, awayScore, currentPeriod, periodTimeRemaining)
