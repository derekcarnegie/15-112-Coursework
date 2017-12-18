#Derek Li (derekl1) Phil Johnson (phjohnso)
# Lab5
#################################################

import cs112_f17_week5_linter
import math, string, copy

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def isPerfectSquare(n):
    if almostEqual(n**0.5%1, 0 , 10**-7):
        return True

#################################################
# Problems
#################################################



def isKingsTour(board):
    rows = len(board)
    cols = len(board[0])
    for row in range(rows):
        for col in range(cols):
            if board[row][col]<1 or board[row][col]>(rows*cols):
                #checks to make sure every element is between 1 and rows*cols
                return False
            else:
                for i in range(1,(rows*cols),1):    
                #iterates with i being the range of values on the board
                    if board[row][col]==i:
                        #iterates through board looking for designated value
                        indexRow = row
                        indexCols = col
                        #sets index's to be found later
                        found = False
                        for k in range(-1,2,1):
                            for j in range(-1,2,1):
                                #all possible combinations are in 3x3 list
                                if (indexRow + k)>=rows or (indexCols+j)>=cols:
                                    continue
                                #if not in list range it skips the value
                                if (indexRow+k)<0 or (indexCols+j)<0:
                                    continue
                                #if not in list range it skips the value
                                elif board[indexRow+k][indexCols+j]==i+1:
                                    found = True
                                #looks for the next value of i 
                                #within the elements next to it
                        if found == False:
                            #if the value is never found the KingsBoard fails
                            return False
    return True        

def isLegalSudoku(board):
    #calls all previously made helper function
    #ensures that they all pass and that the sudoku board is legal
    for i in range(len(board)):
        if not isLegalCol(board,i):
            return False
        if not isLegalRow(board, i):
            return False
        if not isLegalBlock(board,i):
            return False
    return True

def areLegalValues(Values):
    nSquared = len(Values)
    if not isPerfectSquare(nSquared):
        return False
        #if the value is not a perfect square
        #the list cannot be square and thus fails
    for i in Values:
        if i == 0:
            continue
        if i not in range(0,nSquared+1):
            #if out of range it fails
            return False
        if Values.count(i)>1:
            #if the values are repeated it fails
            return False
    return True

def isLegalRow(board,row):
    if areLegalValues(board[row]) == True:
        #checks the legality of the rows
        return True
    else:
        #if the values of the rows are not legal
        #it does not pass
        return False

def isLegalCol(board, col):
    colList = []
    for row in board:
        #holds the values of the columns
        colList.append(row[col])
    if areLegalValues(colList):
        #checks to make sure the values of the columns are legal
        return True
    else:
        return False

def isLegalBlock(board,block):
    nSquared = len(board)
    n = int(nSquared**0.5)
    blockList = []
    #list for blocks to be put in
    startRow = (block//n)*n
    finalRow = startRow + n
    startCol = (block%n) * n
    finalCol = startCol+n
    #determines the start and end for the rows and columns
    for row in range(startRow, finalRow):
        for col in range(startCol, finalCol):
            #adds all of the elements from the block to the list
            blockList.append(board[row][col])
    if not areLegalValues(blockList):
        #ensures that all the values of the blockList are legal
        return False
    return True

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################


#################################################
# Test Functions
#################################################

def testIsKingsTour():
    print("Testing isKingsTour(board)...", end="")
    assert(isKingsTour([[ 3, 2, 1 ],
                        [ 6, 4, 9 ],
                        [ 4, 5, 1,]])==False)
    assert(isKingsTour([[ 3, 2, 1 ],
                        [ 6, 4, 9 ],
                        [ 5, 7, 8 ]])==True)
    print("Passed!")

                        
def testIsLegalSudoku():
    print("Testing testisLegalSudoku...()", end="")
    assert(isLegalSudoku([[1, 2, 3, 4, 5, 6, 7, 8, 9], 
    [5, 2, 8, 1, 3, 9, 6, 2, 4], [4, 9, 6, 8, 7, 2, 1, 5, 3], 
    [9, 5, 2, 3, 8, 1, 4, 6, 7], [6, 4, 1, 2, 9, 7, 8, 3, 5], 
    [3, 8, 7, 5, 6, 4, 0, 9, 1], [7, 1, 9, 6, 2, 3, 5, 4, 8], 
    [8, 6, 4, 9, 1, 5, 3, 7, 2], [2, 3, 5, 7, 4, 8, 9, 1, 6]])==False)
                        
    print("passed")


#################################################
# testAll and main
#################################################

def testAll():
    testIsKingsTour()
    testIsLegalSudoku()
    

def main():
    cs112_f17_week5_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
