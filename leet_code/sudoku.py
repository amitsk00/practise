
def solve_sudoku(board , attempt):

    def is_valid(row, col, num):
        # print("~~ ")
        if num in board[row]:
            # print(f"found in row {row}")
            return False
        
        for r in range(9):
            if num == board[r][col]:
                # print(f"found in row {r} and column {col}")
                return False
            
        # print("=============")
        for r in range((row // 3)*3 , (row // 3)*3 + 3):
            for c in range((col // 3)*3 , (col // 3)*3 + 3):
                # print(f"{r},{c}")
                if board[r][c] == num:
                    return False
        return True



    def add_numbers():
        nonlocal attempt
        for i in range(9):
            for j in range(9):

                if board[i][j] == 0:
                        for num in range(1,10):
                            
                            if is_valid(i,j,num):
                                # print(f"Trying to fix {num} - after valid position of {i},{j} - in attempt {attempt}")
                                board[i][j] = num 

                                if add_numbers():
                                    # print(f"{num} number added fine")
                                    return True
                                
                                board[i][j] = 0
                            attempt += 1

                        return False
        return True
                
    add_numbers()




board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
attempt = 0
solve_sudoku(board, attempt)

print(f"************* after {attempt} attempts ")
for row1 in board:
    print(row1)