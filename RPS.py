# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

global markovMatrix

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
  #Implement the markov matrix method here:
  
#   R P S Last Turn
# R x x x
# P x x x
# S x x x
  if not opponent_history:
    markovMatrix = [[0,0,0],[0,0,0],[0,0,0]]
    if opponent_history[-2] == "R":
      
  
  


  
    guess = "R"
    #If the opponent keeps playing the same play again and again, play what beats that
    if len(opponent_history) > 2 and opponent_history[-1] == opponent_history[-2] == opponent_history[-3]:
      repeat = opponent_history[-1]
      if repeat == "R":
        guess = "P"
      elif repeat == "P":
        guess = "S"
      else:
        guess = "R"
    elif len(opponent_history) > 2: #This method beats Kris
        guess = opponent_history[-2]

    return guess
