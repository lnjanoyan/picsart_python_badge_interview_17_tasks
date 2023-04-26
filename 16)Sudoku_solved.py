def sud_check():
    # input values check
    for line in board:
        for val in line:
            if val <= 0 or val > 9:
                return 'Numbers must be in range 1-9'

    # row check
    for line in board:
        for el in line:
            if line.count(el) != 1:
                return False
    # column check
    ls = []
    for i in range(9):
        for j in range(9):
            ls.append(board[j][i])
            if board.count(board[i]) != 1:
                return False
        ls = []

    # square check
    ls = []
    row = 0
    col = 0
    for i in range(3):
        for j in range(3):
            ls.append(board[row][col])
            if ls.count(board[row][col]) != 1:
                return False
            if row < 6 and col < 6:
                row += 3
                col += 3
            ls = []
    return True


# main program
board = []
print("Enter sudoku numbers to check: ")

for row in range(9):
    line = []
    for col in range(9):
        ip = input()
        if ip.isdecimal():
            line.append(int(ip))
        else:
            print('Non valid value founded! ,numbers must be in range 1-9 ')
    board.append(line)

for i in board:
    print(i)

print(sud_check())
