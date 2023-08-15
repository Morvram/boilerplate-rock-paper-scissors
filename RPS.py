# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random


def player(prev_play, opponent_history=[], my_history=[]):
  opponent_history.append(prev_play)
  guess = random.choice(["R", "P", "S"])  #Default guess is random.
  ideal_response = {
    "P": "S",
    "R": "P",
    "S": "R"
  }  #The correct way to respond to each throw.

  target = guess_opponent(opponent_history, my_history)

  #Strategy 1 "kris": Scissors, Paper, Rock, Scissors, Paper, Rock
  #Use if you have a case where the opponent repeatedly guesses the option that will beat your last guess.
  if target == "kris":
    guess = ideal_response[ideal_response[
      my_history[-1]]]  #Ideal response to the ideal response to my last guess.

  #Strategy "Abbey": Abbey is using a markov matrix to predict what I will follow each move with.
  elif target == "abbey":
    if not len(my_history):
      guess = "R"
    else:
      guess = ideal_response[my_history[-1]]  #sequence of RPS

  my_history.append(guess)
  return guess


def guess_opponent(opponent_history, my_history):
  ideal_response = {
    "P": "S",
    "R": "P",
    "S": "R"
  }  #The correct way to respond to each throw.
  if len(my_history) > 10 and len(opponent_history) > 10:
    #kris?
    last_moves = my_history[-11:-1]
    for i in range(10):
      move = last_moves[-10 + i]
      if move == "":
        move = "R"
      if ideal_response[move] != opponent_history[-10 + i]:
        break
      else:
        return "kris"

  return "abbey"
