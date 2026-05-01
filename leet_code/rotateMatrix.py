def rotate_matrix(matrix):
    newMatrix = [] 

    cntRow = len(matrix)
    cntCol = len(matrix[0])
    

    for j in range(cntCol):
        tmpList = []
        for i in range(cntRow):
            # print(f"{i},{j} -- {matrix[i][j]}")
            # newMatrix[j].append(matrix[i][j])
            tmpList.append(matrix[i][j])
        newMatrix.insert(j, tmpList)
    

    return newMatrix


def printMatrix(matrix):
    print("====================")
    for row in matrix:
        print(row)

if __name__ == "__main__":
    myMatrx = [[1,2,3,9],[4,5,6,8],[11,12,23,34]]
    printMatrix(myMatrx)
    newMatrix = rotate_matrix(myMatrx)
    printMatrix(newMatrix)
