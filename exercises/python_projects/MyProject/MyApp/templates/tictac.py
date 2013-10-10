board =['1','2','3','4','5','6','7','8','9']

player1 = 'X'
player2 = 'O'
win = False
turns = 0


def printboard():
    row1 = board[0], board[1], board[2]
    row2 = board[3], board[4], board[5]
    row3 = board[6], board[7], board[8]
    print row1
    print row2
    print row3


def check_win(player):
    global win
    winning_patterns = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    for p in winning_patterns:
        if check_win_helper(*p):
            print "%s wins" % player
            win = True
            return win
    return False


def check_win_helper(a, b, c):
    return board[a] == board[b] == board[c]


def playerturn(player):
    print "%s's turn" % player
    print "Select number ",
    col = int(raw_input()) - 1
    if col >= 0 and col <=8:
        if board[col] == 'X' or board[col] == 'O':
            print "Already taken"
            playerturn(player)
        else:
            board[col] = player
    else:
        print "Not a valid move please try again"
        playerturn(player)


printboard()
while(win == False):
    playerturn(player1)
    turns += 1
    printboard()
    if check_win(player1) == True: break
    if turns == 9:
        print "This game is a draw!"
        break

    playerturn(player2)
    turns += 1
    printboard()
    check_win(player2)
    if check_win(player2) == True: break