def makeBoard(gb):
    rows = len(gb)
    cols = len(gb[0])
    
    topline = ' ---'
    boxes = '|   '
    
    print(cols*topline)
    
    for row in range(rows):
        for col in range(cols):
            print(f'| {gb[row][col]} ', end='')
        print('|')
        print(cols*topline)

def checkWin(gb):
    cols= [[],[],[]]
    diags = [[],[]]
    win = False
    winner = None
    
    for row in range(len(gb)):
        if len(set(gb[row])) == 1 and gb[row][0] != '_':
            win = True
            winner = gb[row][0]
            
        for i in range(3):
            cols[i].append(gb[row][i])

        diags[0].append(gb[row][row])
        diags[1].append(gb[row][::-1][row])
        

    for col in cols:
        if len(set(col)) == 1 and col[0] != '_':
            win = True
            winner = col[0]

    for diag in diags:
        if len(set(diag)) == 1 and diag[0] != '_':
            win = True
            winner = diag[0]

    return(win, winner)


def playMove(coord, player, board):
    if player == 1:
        move = 'X'
    elif player == 2:
        move = 'O'

    board[coord[1]-1][coord[0]-1] = move

    return board

def valid(board, move):

    if move[0] <= 3 and move[1] <= 3:
            
        if board[move[1]-1][move[0]-1] == '_':
                
            return True
        
    return False

if __name__ == '__main__':
    plrs = {'X':1, 'O':2}
    gb = [['_','_','_'],
          ['_','_','_'],
          ['_','_','_']]

    moves = 1
    while moves < 10:
        if moves % 2 == 1:
            player = 1
        elif moves % 2 == 0:
            player = 2
            
        makeBoard(gb)

        move = list(map(int, input(f'Player {player} what move would you like to play? (respond with x,y)').strip().split(',')))

        if valid(gb, move):
            playMove(move, player, gb)
            moves += 1
        else:
            print('Please choose a valid move, remember 1,1 is the upper left...')

        if checkWin(gb)[0] == True:
            makeBoard(gb)
            print(f'Congratulations player {plrs[checkWin(gb)[1]]}! You Win!')
            break

    if checkWin(gb)[0] == False:
        makeBoard(bg)
        print('Draw')
