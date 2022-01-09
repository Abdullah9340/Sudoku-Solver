
#Backtracking function
def solve(bo):
    find_pos = find_empty(bo)
    if not find_pos:
        return True

    row, col = find_pos
    for i in range(1, 10):
        if is_valid(bo, i, find_pos):
            bo[row][col] = i
            if solve(bo):
                return True
            bo[row][col] = 0

    return False

# Check if a certain position is valid
def is_valid(bo, num, pos):
    # check rows
    for i in range(len(bo)):
        if bo[pos[0]][i] == num and i != pos[1]:
            return False

    # check colms
    for i in range(len(bo[0])):
        if bo[i][pos[1]] == num and i != pos[0]:
            return False

    box_xpos = pos[1] // 3
    box_ypos = pos[0] // 3

    for i in range(box_ypos * 3, box_ypos * 3 + 3):
        for j in range(box_xpos * 3, box_xpos * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True

# Find the next empty square
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if bo[i][j] == 0:
                return (i, j)
    return None
