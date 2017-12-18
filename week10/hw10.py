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

def flat(L,i):
    #delves deeper into the list to see if it works
    if i == len(L):
        return L
    if isinstance(L[i],list):
        return flat(L[:i]+L[i]+L[i+1:],i)
    return flat(L,i+1)

def isFull(board):
    for i in range(len(board)):
        for k in range(len(board[0])):
            if board[i][k]==0:
                return False
    return True
    
def isAdjacent(board):
    for i in range(len(board)):
        for k in range(len(board[0])):
            if board[i][k]=="A":
                a = ord('A')
                for x in range(x-1,x+2):
                    for y in range(y-1,y+2):
                        if board[i+x][k+y]==chr(ord(a)+1):
                            a+=1
                        else:
                            return False
    return True

def isLegalABC(board):
    #checks adjacent and constraint
    if isAdjacent(board) and checkConstraint:
        return True
    return False
            
def checkConstraint(board,constraints):
    firstDiag = constraints[0]
    secondDiag = contraints[6]
    thirdDiag=constraints[12]
    fourthDiag=constraints[18]
    for i in range(len(board)):
        if board[i][i]==firstDiag:
            continue
        if board[len(board)-1-i][i]==secondDiag:
            continue
        if board[len(board)-1-i][i]==thirdDiag:
            continue
        if board[i][len(board)-1-i]==fourthDiag:
            continue
    verticalConstraints1 = constraints[1:6]
    verticalConstraints2=constraints[12:17:-1]
    verticalList = []
    for j in range(len(board[0])):
        col = ""
        for k in range(len(board)):
            col += board[k][j]
            if (verticalConstraints1[j] not in col and 
            verticalConstraints2[j] not in col):
                 return False
    return True
    horizontalConstraints1= constraints[6:12]
    horizontalConstraints2= contrainsts[18:23:-1]
    for k in range(len(board)):
            if (horizontalConstraints1[j] not in board[k] and 
             horizontalConstraints2[j] not in board[k]):
                 return False
    return True
 
    
#################################################
# Problems
#################################################


def flatten(L):
    #flattens lists
    if not isinstance(L,list):
        return L
    if len(L) == 0:
        return []
    return flat(L,0)
 
def noError(f):
    #uses try and exception so there is no fails
    def g(*args):
        try:
            return f(*args)
        except:
            return None
    return g
 
def solveABC(constraints, aLocation):
    #solves ABC puzzle
    board = [[0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    board[aLocation[0]][aLocation[1]]='A'
    if isFull(board) and isLegalABC(board):
        return board
    else:
        for i in range(len(board)):
            for k in range(len(board[0])):
                if board[i][k]==0:
                    #checks if board has anything in it
                    for j in range(2,26):
                        board[i][k]=string.ascii_uppercase[j]
                        if isLegalABC(board):
                            if solveABC(board)!=None:
                                return board
                    board[i][k]=0
                    return None

def hFractal(width=600, height=600):
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

def drawH(canvas,widthH,heightH,centerX,centerY):
    canvas.create_line(centerX-widthH/4,centerY,
    centerX+widthH/4,centerY,width=2)#draws horizontal line
    canvas.create_line(centerX-widthH/4,centerY-heightH/4,
    centerX-widthH/4,centerY+heightH/4,width=2)#draws left vertical line
    canvas.create_line(centerX+widthH/4,centerY-heightH/4,
    centerX+widthH/4,centerY+heightH/4,width=2)#draws right vertical line
    
def fractalH(canvas,widthH,heightH,centerX,centerY,level):
    drawH(canvas, widthH, heightH,centerX,centerY)
    if (level == 0):
        drawH(canvas, widthH, heightH,centerX,centerY)
    else:
        fractalH(canvas,widthH/2,heightH/2,centerX-widthH/4,
        centerY-heightH/4,level-1)#top left redrawn H
        fractalH(canvas,widthH/2,heightH/2,centerX+widthH/4,
        centerY-heightH/4,level-1)#top right redrawn H
        fractalH(canvas,widthH/2,heightH/2,centerX+widthH/4,
        centerY+heightH/4,level-1)#bottom right redrawn H
        fractalH(canvas,widthH/2,heightH/2,centerX-widthH/4,
        centerY+heightH/4,level-1)#bottom left redrawn H

def keyPressed(event, data):
    if (event.keysym in ["Up", "Right"]):
        data.level += 1
    elif ((event.keysym in ["Down", "Left"]) and (data.level > 0)):
        data.level -= 1

def mousePressed(event, data): pass

def timerFired(data): pass

def redrawAll(canvas,data):
    #draws fractalH
    fractalH(canvas,data.width,data.height,
    data.width/2,data.height/2,data.level)

#################################################
# Test Functions
#################################################

def testflatten():
    print ("Testing flatten(L)...", end="")
    assert (flatten([1,[2]])==[1,2])
    assert (flatten([1,2,[3,[4,5],6],7])==[1,2,3,4,5,6,7])
    assert (flatten(['wow', [2,[[]]], [True]])==['wow', 2, True])
    assert (flatten([])==[])
    assert (flatten([[]])==[])
    assert (flatten(3)==3)
    print ("Done!")

def testNoErrorDecorator():
    print("Testing @noError decorator...", end="")
    @noError
    def f(x, y): return x/y
    assert(f(1, 5) == 1/5)
    assert(f(1, 0) == None)

    @noError
    def g(): return 1/0
    assert(g() == None)

    @noError
    def h(n):
        if (n == 0): return 1
        else: return h(n+1)
    assert(h(0) == 1)
    assert(h(-1) == 1)
    assert(h(1) == None)

    print("Passed!")
    
def testSolveABC():
    print('Testing solveABC()...', end='')
    constraints = "CHJXBOVLFNURGPEKWTSQDYMI"
    aLocation = (0,4)
    board = solveABC(constraints, aLocation)
    solution = [['I', 'J', 'K', 'L', 'A'],
                ['H', 'G', 'F', 'B', 'M'],
                ['T', 'Y', 'C', 'E', 'N'],
                ['U', 'S', 'X', 'D', 'O'],
                ['V', 'W', 'R', 'Q', 'P']
               ]
    assert(board == solution)
    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    testflatten()
    testNoErrorDecorator()
    hFractal()
    testSolveABC()
    

def main():
    cs112_f17_week10_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
