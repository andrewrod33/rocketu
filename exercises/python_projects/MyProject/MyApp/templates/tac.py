board =['1','2','3','4','5','6','7','8','9']
row1 = board[0], board[1], board[2]
row2 = board[3], board[4], board[5]
row3 = board[6], board[7], board[8]


player1 = 'X'
player2 = 'O'
win = False
turns = 0

def checkwin(player):
  for c in range(0,3):
    if board[0] == player and board[1] == player and board[2] == player:
      print "%s wins" % player
      playerwin = True
      return playerwin
    elif board[0] == player and board[3] == player and board[6] == player:
      print "%s wins" % player
      playerwin = True
      return playerwin
    elif board[0] == player and board[4] == player and board[8] == player:
      print "%s wins" % player
      playerwin = True
      return playerwin
    elif board[2] == player and board[4] == player and board[6] == player:
      print "%s wins" % player
      playerwin = True
      return playerwin
  else:
    playerwin = False
    return playerwin

def playerturn(player):
  print "%s's turn" % player
  turn = 1
  while(turn):
      print "Select number ",
      col = int(raw_input()) - 1
      if board[col] == 'X' or board[col] == 'O':
        print "Already taken!"
      else:
        board[col] = player
        turn = 0

def printboard():
    print row1
    print row2
    print row3

printboard()
while(win == False):
  playerturn(player1)
  turns += 1
  printboard()
  if checkwin(player1) == True: break
  if turns == 9:
      print "This game is a draw!"
      break

  playerturn(player2)
  turns += 1
  printboard()
  checkwin(player2)
  if checkwin(player2) == True: break

