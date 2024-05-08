def getOpponent(player):
    if player == "X":
        return "O"
    elif player == "O":
        return "X"


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
