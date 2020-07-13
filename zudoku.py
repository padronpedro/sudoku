from os import system, name 

mainBboard = [
    [0,0,0,0,0,4,0,9,0],
    [8,0,2,9,7,0,0,0,0],
    [9,0,1,2,0,0,3,0,0],

    [0,0,0,0,4,9,1,5,7],
    [0,1,3,0,5,0,9,2,0],
    [5,7,9,1,2,0,0,0,0],

    [0,0,7,0,0,2,6,0,3],
    [0,0,0,0,3,8,2,0,5],
    [0,2,0,5,0,0,0,0,0],
]

def clear(): 
      # for windows 
    if name == 'nt': 
        _ = system('cls') 
      # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

def printBoard(auxBoard):
    for cell in auxBoard: 
        print(cell) 

def allFound(auxBoard):
    for row in auxBoard:
        for cell in row:
            if(cell==0):
                return False
    return True

def subTable(auxBoard,i,j,item):

    rowInit = 0
    rowEnd = 2
    colInit = 0
    colEnd = 2

    if(i>=3 and i<=5):
        colInit = 3
        colEnd = 5
    if(i>=6 and i<=8):
        colInit = 6
        colEnd = 8
    if(j>=3 and j<=5):
        rowInit = 3
        rowEnd = 5
    if(j>=6 and j<=8):
        rowInit = 6
        rowEnd = 8       

    for row in range(colInit,colEnd+1):
        for cell in range(rowInit,rowEnd+1):
            if((row!= i) and (cell!=j)):
                if(auxBoard[row][cell]==item):
                    return False
    return True

def checkRow(auxBoard,i,j,item):
    for aux in range(0,9):
        if(aux!=j):
            if(auxBoard[i][aux]==item):
                return False
    return True

def checkColumn(auxBoard,i,j,item):
    for aux in range(0,9):
        if(aux!=i):
            if(auxBoard[aux][j]==item):
                return False
    return True

def isValid(auxBoard,i,j,item):

    if(subTable(auxBoard,i,j,item) == True):
        if(checkRow(auxBoard,i,j,item)):
            if(checkColumn(auxBoard,i,j,item)):
                return True

    return False

def solve(board,i,j):

    if(isValid(board,i,j,board[i][j]) or board[i][j]==0):

        if(allFound(board)):
            print('Solved Board\n')
            printBoard(board)
            return True

        if(board[i][j]!=0):
            while mainBboard[i][j]!=0:
                if(j+1)<len(board):
                    j = j + 1
                else:
                    i = i + 1
                    j = 0

        for item in range(1,10):
            board[i][j] = item

            clear()
            printBoard(board)
            if(solve(board,i,j)):
                return True
            else:
                board[i][j] = 0
        
    return False


def main():
    clear()
    print('Original Board\n')

    printBoard(mainBboard)

    #solve game
    solve(mainBboard,0,0)

    print('\n')

if(__name__ == "__main__"):
    main()