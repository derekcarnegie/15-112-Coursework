#################################################
# Hw4
#################################################

import cs112_f17_week10_linter
import math, string, copy, os

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

#HERE TO END COMMENT IS FROM LAB 5
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

#HERE IS END OF CODE FROM LAB 5

def isFull(board):
    for i in range(len(board)):
        for k in range(len(board[0])):
            if board[i][k]==0:
                return False
    return True

#################################################
# Problems
#################################################


def findLargestFile(path):
    if (os.path.isdir(path) == False):#if there is no path to go further down
        return path
    else:#recursive case: it is a folder and has more paths to go down
        largestSize = 0
        largestPath = ""
        # recursive case: it's a folder, return list of all paths
        for filename in os.listdir(path):
            #current location
            currentPath = findLargestFile(path + "/" + filename)
            currentPathSize = 0
            if len(currentPath)!=0:
                currentPathSize = os.path.getsize(currentPath)
            #compares current size to previous largest size
            if(currentPathSize > largestSize):
                largestSize = currentPathSize
                largestPath = currentPath
        return largestPath

def solveSudoku(board):
    #solves sudoku recursively
    if isFull(board) and isLegalSudoku(board):#base case when board is full
        return (board)
    else:
        #recursive case when board still needs to be solved
        for i in range(len(board)):
            for k in range(len(board[0])):
                #finds empty spots on board
                if board[i][k]==0:
                    for j in range(1,10):
                        board[i][k]=j
                        #checks values can go into board and then see's 
                        #if they are legal
                        if isLegalSudoku(board):
                            if solveSudoku(board)!=None:
                                #if the board continues to work return the board
                                return board
                    #backtracks if the previous checked value is wrong
                    board[i][k]=0
                    return None

def runTeddyFractalViewer(width=600, height=600):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

from tkinter import *
import math

def init(data):
    data.level=0

def teddyFace(canvas, xc, yc, r):
    canvas.create_oval(xc-0.5*r,yc+0.5*r,xc+0.5*r,yc-0.5*r,fill="#a32b2e",
    width=r/8)
    canvas.create_oval(xc-0.2*r,yc,xc+0.2*r,yc+0.4*r,fill="#d1b48e",
    width=r/12)
    canvas.create_oval(xc-0.075*r,yc+0.05*r,xc+0.075*r,yc+0.2*r,fill="black")
    canvas.create_oval(xc-0.25*r,yc-0.25*r,xc-0.1*r,yc-0.1*r,fill="black")
    canvas.create_oval(xc+0.1*r,yc-0.25*r,xc+0.25*r,yc-0.1*r,fill="black")
    canvas.create_arc(xc-0.08*r,yc+0.2*r,xc,yc+0.25*r,
    style="arc",start=180,extent=180,width=r/20)
    canvas.create_arc(xc,yc+0.2*r,xc+0.08*r,yc+0.25*r,
    style="arc",start=180,extent=180,width=r/20)
    
    
def fractalTeddy(canvas,xc,yc,r,level):
    teddyFace(canvas, xc,yc,r)
    if (level == 0):
        teddyFace(canvas, xc, yc, r)
    else:
        teddyFace(canvas, xc,yc,r)
        fractalTeddy(canvas, xc-r/2,yc-r/2,r/2, level-1)
        fractalTeddy(canvas, xc+r/2,yc-r/2, r/2, level-1)

def keyPressed(event, data):
    if (event.keysym in ["Up", "Right"]):
        data.level += 1
    elif ((event.keysym in ["Down", "Left"]) and (data.level > 0)):
        data.level -= 1

def mousePressed(event, data): pass

def timerFired(data): pass

def redrawAll(canvas,data):
    fractalTeddy(canvas,300,300,200,data.level)

#################################################
# Test Functions
#################################################

def testFindLargestFile():
    print ("Testing findLargestFile()...",end="")
    assert(findLargestFile("sampleFiles/folderA") ==
                        "sampleFiles/folderA/folderC/giftwrap.txt")
    assert(findLargestFile("sampleFiles/folderB") ==
                        "sampleFiles/folderB/folderH/driving.txt")
    assert(findLargestFile("sampleFiles/folderB/folderF") == "")
    print ('Done!')
    
    
def testSolveSudoku():
    print('Testing solveSudoku()...', end='')
    board = [
              [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
              [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
              [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
              [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
              [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
              [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
              [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
              [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
              [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
            ]
    solved = solveSudoku(board)
    solution = [
                [5, 3, 4, 6, 7, 8, 9, 1, 2], 
                [6, 7, 2, 1, 9, 5, 3, 4, 8], 
                [1, 9, 8, 3, 4, 2, 5, 6, 7], 
                [8, 5, 9, 7, 6, 1, 4, 2, 3], 
                [4, 2, 6, 8, 5, 3, 7, 9, 1], 
                [7, 1, 3, 9, 2, 4, 8, 5, 6], 
                [9, 6, 1, 5, 3, 7, 2, 8, 4], 
                [2, 8, 7, 4, 1, 9, 6, 3, 5], 
                [3, 4, 5, 2, 8, 6, 1, 7, 9]
               ]
    assert(solved == solution)
    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    #testFindLargestFile()
    runTeddyFractalViewer()
    testSolveSudoku()

def main():
    cs112_f17_week10_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
