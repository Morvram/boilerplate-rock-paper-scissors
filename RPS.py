# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

markovMatrix = [[0,0,0],[0,0,0]]

def player(prev_play, opponent_history=[]):
  opponent_history.append(prev_play)
  #Implement the markov matrix method here:
  global markovMatrix
  if not opponent_history:
    markovMatrix = [[0,0,0],[0,0,0]]
  if opponent_history[-2] == "R":
    if opponent_history[-1] == "R":
      markovMatrix[0][0] += 1
    elif opponent_history[-1] == "P":
      markovMatrix[0][1] += 1
    else:
      markovMatrix[0][2] += 1
  elif opponent_history[2] == "P":
    if opponent_history[-1] == "R":
      markovMatrix[1][0] += 1
    elif opponent_history[-1] == "P":
      markovMatrix[1][1] += 1
    else:
      markovMatrix[1][2] += 1
  else:
    if opponent_history[-1] == "R":
      markovMatrix[2][0] += 1
    elif opponent_history[-1] == "P":
      markovMatrix[2][1] += 1
    else:
      markovMatrix[2][2] += 1
  
  #Try to decide on a guess based on the previous move.
  if opponent_history[-1] == "R":
    if (markovMatrix[0][0] > markovMatrix[0][1] and markovMatrix[0][0] > markovMatrix[0][2]) or (markovMatrix[0][0] == markovMatrix[0][1] == markovMatrix[0][2]): #Rock is most often followed with rock, or they're all even so we will assume rock will be followed by another rock.
      guess = "P"
    elif markovMatrix[0][2] > markovMatrix[0][0] and markovMatrix[0][2] > markovMatrix[0][1]: #Rock is most often followed with scissors.
      guess = "R"
    else: #Rock is most often followed by Paper.
      guess = "S"
      
  if opponent_history[-1] == "P":
    if (markovMatrix[1][0] > markovMatrix[1][1] and markovMatrix[1][0] > markovMatrix[1][2]) or (markovMatrix[1][0] == markovMatrix[1][1] == markovMatrix[1][2]): #Paper is most often followed with Rock.
      guess = "P"
    elif (markovMatrix[1][1] > markovMatrix[1][0] and markovMatrix[1][1] > markovMatrix[1][2]) or (markovMatrix[1][0] == markovMatrix[1][1] == markovMatrix[1][2]): #Paper is most often followed by paper, or they're all even so we will assume this.
      guess = "S"
    else: #Paper is most often followed by scissors.
      guess = "R"

  else:
    if (markovMatrix[2][2] > markovMatrix[2][1] and markovMatrix[2][2] > markovMatrix[2]0]) or (markovMatrix[2][0] == markovMatrix[2][1] == markovMatrix[2][2]): #Scissors are most often followed by scissors.
      guess = "R"
    elif markovMatrix[2][0] > markovMatrix[2][1] and markovMatrix[2][0] > markovMatrix[2][2]: #Scissors are most often followed by Rock.
      guess = "P"
    else: #Scissors are most often followed by paper.
      guess = "S"
    
  return guess
    
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