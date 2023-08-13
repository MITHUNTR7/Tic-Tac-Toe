
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

board = newBoard()
board[0][2] = "X"
board[1][0] = "O"
board[1][1] = "O"
board[1][2] = "X"
board[2][2] = "X"
render(board)
    