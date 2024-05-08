import random

def newBoard():
    board = [[None]*3 for i in range(3)]
    return board

def render(board):
    print("  0","1","2")
    print("  -----")
    for r in range(len(board)):
        print(r,"|",end="")
        for c in range(len(board[r])):
            if board[r][c] is None:
                print(" ",end="")
            else:
                print(board[r][c],end="")             
        print("|")
             
    print("  -----")

def getMove(name):
    print(f"{name}, What is your move's X co-ordinate(row no.) ?: ",end="")
    x = int(input())
    print(f"{name}, What is your move's Y co-ordinate(column no.) ?: ",end="")
    y = int(input())
    return (x, y)

def makeMove(board, coords, player):
    x, y = coords
    updatedBoard = board
    if updatedBoard[x][y]:
        raise Exception(f"Illegal move ({x}, {y}) square already taken")
    updatedBoard[x][y] = player
    return updatedBoard

def getWinner(board):
    lineCoords = getLines()
    for line in lineCoords:
        lineValues = [board[x][y] for (x, y) in line]
        if len(set(lineValues)) == 1 and lineValues[0]:
            return lineValues[0]
    return None
    
    
def getLines():
    cols = []
    for x in range(3):
        col = []
        for y in range(3):
            col.append((x, y))
        cols.append(col)
    
    rows = []
    for y in range(3):
        row = []
        for x in range(3):
            row.append((x, y))
        rows.append(row)
        
    diagonals = [[(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]
    
    return rows + cols + diagonals
    
def checkDraw(board):
    for x in range(3):
        for y in range(3):
            # There is atleast one None value inside the board
            if not board[x][y]: 
                return False
    return True


def randomAI(board, player):
    legalCoords = []
    for x in range(3):
        for y in range(3):
            if not board[x][y]:
                legalCoords.append((x, y))
    return random.choice(legalCoords)

def findsWinningMoveAI(board, player): # Returns the winning move if any else it will return none
    lineCoords = getLines()
    for line in lineCoords:
        nPlayer = 0 # number of cells occupied by current player
        nEmpty = 0 # number of empty cells in the current line
        lastEmpty = None # last empty coordinate in the line
        for (x, y) in line:
            if board[x][y] == player:
                nPlayer += 1
            elif not board[x][y]:
                nEmpty += 1
                lastEmpty = (x, y)
        if nPlayer == 2 and nEmpty == 1:
            return lastEmpty
    return None
        

players = [("X", "Player 1"), ("O", "Player 2")]
playerMap = {"X": "Player 1", "O" : "Player 2"}
turn = 0
board = newBoard()
while True:
    render(board)
    ID, name = players[turn % 2]
    # will try to find a winning move if it exists else random move is returned
    moveCoords = findsWinningMoveAI(board, ID) if findsWinningMoveAI(board, ID) else randomAI(board, name)
    makeMove(board, moveCoords, ID)
    if getWinner(board):
        render(board)
        print(f"{playerMap[getWinner(board)]} wins!!!")
        break
    if checkDraw(board):
        render(board)
        print("Game ends in a draw")
        break    
    turn += 1
    