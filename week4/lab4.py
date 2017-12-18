#Derek Li (derekl1) Zhongyi Gao (Sean) (zhongyig)
# Lab4
#################################################

import cs112_f17_week4_linter
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

#################################################
# Problems
#################################################



def lookAndSay(a):
    firstValue = ()
    result = [ ]
    if a == []:
        #edge case
        return a
    counter =1
    for y in range(len(a)):
        if y == (len(a)-1):
            #last value in the string has to be the 
            #last showing of that value
            firstValue = (counter,a[y])
            result.append(firstValue)
        elif a[y]==a[y+1]:
            counter+=1
        else:
            firstValue = (counter,a[y])
            result.append(firstValue)
            counter = 1
    return result

def inverseLookAndSay(a):
    result = []
    for tuple in range(len(a)):
        firstNum = a[tuple]
        #gives first Num each tuple inside of list a
        count = firstNum[0]
        #archives count value from the zero'th index 
        secondNum = firstNum[1]
        #archives what the number value is from the first index
        for i in range(count):
            result.append(secondNum)
    return result

def puzzleInSolution(puzzle, solution):
    #checks to make sure that every letter in the puzzle 
    #is in the solution
    for i in puzzle:
        if i == "-":
            continue
        if i.isalpha() and i not in solution:
            return False
    return True


def changeToNumber(x,solution):
    #changes the letters of what is sent over
    #to the numbers allocated by the solution
    numLetter=""
    for letter in x:
        if letter in solution:
            numLetter += str(solution.index(letter))
    return numLetter
            

def solvesCryptarithm(puzzle, solution):
    if puzzleInSolution(puzzle, solution):        
        added = puzzle.split('=')[0]
        final = puzzle.split('=')[1]
        #splits the puzzle into the two parts that
        #at the end should be the same value
        firstTerm = int(changeToNumber(added.split("+")[0],solution))
        secondTerm = int(changeToNumber(added.split("+")[1],solution))
        finalTerm = int(changeToNumber(final,solution))
    else:
        return False
    return firstTerm + secondTerm == finalTerm
        

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

from tkinter import *
import math

def drawStar(canvas, centerX, centerY, diameter, numPoints, color):
    points = []
    if numPoints %2 ==1:
        #checks the number of points to ensure that the first side
        #is always pointing vertically
        for i in range(numPoints*2):
            radPerSide = (2 * math.pi * i)/(numPoints*2)
            #finds the change in radians per side
            if i%2==1:
                #for the outer circle
                x = centerX + diameter/2 * math.sin(radPerSide)
                y = centerY + diameter/2 * math.cos(radPerSide)
                #finds the x and y coordinates for each change 
                #in radians
                points.append((x,y))
            else:
                #inner circle
                x = centerX + diameter*(3/16) * math.sin(radPerSide)
                y = centerY + diameter*(3/16) * math.cos(radPerSide)
                points.append((x,y))
    else:
        #same thing as above just rotated 
        #based on even number of sides
        for i in range(numPoints*2):
            radPerSide = (2 * math.pi * i)/(numPoints*2)
            if i%2==0:
                x = centerX + diameter/2 * math.sin(radPerSide)
                y = centerY + diameter/2 * math.cos(radPerSide)
                points.append((x,y))
            else:
                x = centerX + diameter*(3/16) * math.sin(radPerSide)
                y = centerY + diameter*(3/16) * math.cos(radPerSide)
                points.append((x,y))
    canvas.create_polygon(points, fill = color)


def drawStarHelper(centerX, centerY, diameter, numPoints, color, 
                   winWidth=500, winHeight=500):
    root = Tk()
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.pack()

    drawStar(canvas, centerX, centerY, diameter, numPoints, color)

    root.mainloop()

def drawUnitedStatesFlag(winWidth=950, winHeight=500):
    root = Tk()
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.pack()
    # create the stripes
    for i in range(13):
        start = winHeight*i/13
        end = winHeight*(i+1)/13
        if i%2 == 0:
            canvas.create_rectangle(0,start,winWidth, end, fill = '#bf0a30', 
            width = 0)
        else:
            canvas.create_rectangle(0,start,winWidth, end, fill = 'white', 
            width = 0)
    #create blue box in top left
    canvas.create_rectangle(0,0,winWidth/2.5,\
     winHeight*7/13, fill = "#002868", 
    width = 0)
    
    recWidth = winWidth/2.5
    recHeight = winHeight*7/13
    #create the stars
    for i in range(6):
        drawStar(canvas,recWidth/12 + recWidth*i/6,winHeight*1/26, \
        winHeight*4/(5*13), 5, "white")
    for i in range(6):
        drawStar(canvas,recWidth/12 + recWidth*i/6,\
        winHeight/9 + winHeight*1/26, winHeight*4/(5*13), 5, "white")
    for i in range(5):
        drawStar(canvas,recWidth/6 + recWidth*i/6,\
        winHeight/18 + winHeight*1/26, winHeight*4/(5*13), 5, "white")
    for i in range(6):
        drawStar(canvas,recWidth/12 + recWidth*i/6,\
        winHeight*2/9 + winHeight*1/26, winHeight*4/(5*13), 5, "white")
    for i in range(5):
        drawStar(canvas,recWidth/6 + recWidth*i/6,\
        winHeight*3/18 + winHeight*1/26, winHeight*4/(5*13), 5, "white")
    for i in range(6):
        drawStar(canvas,recWidth/12 + recWidth*i/6,\
        winHeight*3/9 + winHeight*1/26, winHeight*4/(5*13), 5, "white")
    for i in range(5):
        drawStar(canvas,recWidth/6 + recWidth*i/6,\
        winHeight*5/18 + winHeight*1/26, winHeight*4/(5*13), 5, "white")
    for i in range(6):
        drawStar(canvas,recWidth/12 + recWidth*i/6,\
        winHeight*4/9 + winHeight*1/26, winHeight*4/(5*13), 5, "white")
    for i in range(5):
        drawStar(canvas,recWidth/6 + recWidth*i/6,\
        winHeight*7/18 + winHeight*1/26, winHeight*4/(5*13), 5, "white")
    root.mainloop()

def testDrawStar():
    print("Testing drawStar()...")
    print("Since this is graphics, this test is not interactive.")
    print("Inspect each of these results manually to verify them.")
    drawStarHelper(250, 250, 500, 5, "gold")
    drawStarHelper(300, 400, 100, 4, "blue")
    drawStarHelper(300, 200, 300, 9, "red")
    print("Done!")

def testDrawUnitedStatesFlag():
    print("Testing drawUnitedStatesFlag()...")
    print("Since this is graphics, this test is not interactive.")
    print("Inspect each of these results manually to verify them.")
    drawUnitedStatesFlag()
    drawUnitedStatesFlag(winWidth=570, winHeight=300)
    print("Done!")

#################################################
# Test Functions
#################################################

def _verifyLookAndSayIsNondestructive():
    a = [1,2,3]
    b = copy.copy(a)
    lookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testLookAndSay():
    print("Testing lookAndSay()...", end="")
    assert(_verifyLookAndSayIsNondestructive() == True)
    assert(lookAndSay([]) == [])
    assert(lookAndSay([1,1,1]) ==  [(3,1)])
    assert(lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)])
    assert(lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)])
    assert(lookAndSay([2]*5 + [5]*2) == [(5,2), (2,5)])
    assert(lookAndSay([5]*2 + [2]*5) == [(2,5), (5,2)])
    print("Passed!")

def _verifyInverseLookAndSayIsNondestructive():
    a = [(1,2), (2,3)]
    b = copy.copy(a)
    inverseLookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testInverseLookAndSay():
    print("Testing inverseLookAndSay()...", end="")
    assert(_verifyInverseLookAndSayIsNondestructive() == True)
    assert(inverseLookAndSay([]) == [])
    assert(inverseLookAndSay([(3,1)]) == [1,1,1])
    assert(inverseLookAndSay([(1,-1),(1,2),(1,7)]) == [-1,2,7])
    assert(inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10])
    assert(inverseLookAndSay([(5,2), (2,5)]) == [2]*5 + [5]*2)
    assert(inverseLookAndSay([(2,5), (5,2)]) == [5]*2 + [2]*5)
    print("Passed!")

def testSolvesCryptarithm():
    print("Testing solvesCryptarithm()...", end="")
    assert(solvesCryptarithm("SEND+MORE=MONEY","OMY--ENDRS"))
    # from http://www.cryptarithms.com/default.asp?pg=1
    assert(solvesCryptarithm("NUMBER+NUMBER=PUZZLE", "UMNZP-BLER"))
    assert(solvesCryptarithm("TILES+PUZZLES=PICTURE", "UISPELCZRT"))
    assert(solvesCryptarithm("COCA+COLA=OASIS", "LOS---A-CI"))
    assert(solvesCryptarithm("CROSS+ROADS=DANGER", "-DOSEARGNC"))

    assert(solvesCryptarithm("SEND+MORE=MONEY","OMY--ENDR-") == False)
    assert(solvesCryptarithm("SEND+MORE=MONEY","OMY-ENDRS") == False)
    assert(solvesCryptarithm("SEND+MORE=MONY","OMY--ENDRS") == False)
    assert(solvesCryptarithm("SEND+MORE=MONEY","MOY--ENDRS") == False)
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testLookAndSay()
    testInverseLookAndSay()
    testSolvesCryptarithm()
    testDrawStar()
    testDrawUnitedStatesFlag()

def main():
    cs112_f17_week4_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
