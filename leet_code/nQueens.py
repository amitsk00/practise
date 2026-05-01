def place_queens(board):    

    def is_valid(row, col):
        if "Q" in board[row]:
            return False
        
        for i in range(8):
            if board[i][col] == "Q":
                return False
            
        iDiff = abs(row - col)
        iSum = row + col 
        for i in range(8):
            currCol = i + iDiff 
            if currCol >= 0 and currCol < 8:
                if board[i][currCol] == "Q":
                    return False
            
            
            currCol = iSum - i
            # print(f">{i},{currCol}")
            if currCol >= 0 and currCol < 8:
                if board[i][currCol] == "Q":
                    return False
        
        return True 
    

    def place_queens():

        for r in range(8):
            for c in range(8):

                # print(f"{r} {c}")
                if board[r][c] == "0":
                    if is_valid(r,c):
                        print(f"placing queen at {r} {c}")


                        board[r][c] = "Q" 

                        # print("^^^^^^^^^^")
                        # for xx in board:
                        #     print(xx)
                        # print("^^^^^^^^^^")

                        if place_queens():
                            return True
                        board[r][c] = "0"


        return True 

    place_queens()




def printChessBoard(board):
    print("_____________________________")
    for row in board:
        print(row)

if __name__ == "__main__":
    board = [["0" for _ in range(8)] for _ in range(8) ]
    

    printChessBoard(board)
    place_queens(board)
    printChessBoard(board)
