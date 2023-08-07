# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.


def player(prev_play, opponent_history=[]):
  opponent_history.append(prev_play)
  #Implement the markov matrix method here:

  guess = "R"  #Default guess from boilerplate. Plays rock every time.

  # 1. Counting R/P/S most used by opponent
  # opponent_history = ["P","P","P","S","S","R"]
  # dori-min solution, idk how well this works but attempting it for reference.
  countdict = {
    "R": opponent_history.count("R"),
    "P": opponent_history.count("P"),
    "S": opponent_history.count("S")
  }
  countdict = dict(sorted(countdict.items(), key=lambda x: x[1], reverse=True))
  guess = [key for key in countdict.keys()][0]

  return guess
