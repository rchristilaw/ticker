#!/usr/bin/env python

from flask import Flask, request
from flask_cors import CORS, cross_origin
from ticker import Ticker

app = Flask(__name__)
cors = CORS(app)

ticker = Ticker()

@app.route("/setGame", methods=['POST'])
def setGame():
    ticker.setGame(request.data)
    return "OK"

@app.route("/turnOff", methods=['POST'])
def turnOff():
    ticker.stopGame()
    return "OK"

@app.route("/activateGoalLight", methods=['POST'])
def activateGoalLight():
    ticker.activateGoalLight()
    return "OK"

if __name__ == "__main__":
    # ticker.initGame("10") 
    app.run(debug=True, host='0.0.0.0', port=8080)
