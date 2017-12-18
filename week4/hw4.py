#################################################
# Hw4
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

# This is supposed to remove blank lines and comments.
# It has some bugs though...

def buggyCleanUpCode(code):
    lines = code.splitlines()
    print(code)
    g=0

    for h in range(len(lines)+20):
        test = g
        if g < (len(lines)):
            codeLine = lines[g]
            if codeLine.find("#")==-1:
                lenCodeLine = len(codeLine)
            else:
                lenCodeLine= codeLine.find("#")    
            for k in range(lenCodeLine):
                if codeLine[k] !=" ":
                    break
                elif k==lenCodeLine-1: 
                    lines[g] = ""
            commentIndex = codeLine.find("#")
            if commentIndex !=-1:
                print (lines[7])
                print (codeLine, "dsfjkldjkslf")
                lines[g] = codeLine[:commentIndex]
            if lines[g] in string.whitespace:
                print ("SDF")
                lines.pop(g)
                g=g-2
        if g<(test-1):
            g+=1
        g=g+1
    print ("\n".join(lines))
    return "\n".join(lines)

def possibleHands(dictionary, hand):
    return 42
    # possibleHands = []
    # for i in range(len(dictionary)):
    #     for k in range(len(dictionary[i])):
    #         if hand[k] in dictionary[i]:
    #             hand[k]- hand[k]
    #             possibleHands += hand[k]
                
                
    

def bestScrabbleScore(dictionary, letterScores, hand):
    return 42
    #allPossibleHands = possibleHands(dictionary, hand)
    

###### Autograded Bonus ########
# (place non-autograded bonus below #ignore-rest line!) #

def runSimpleProgram(program, args):
    return 42

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

from tkinter import *
import math

def runSimpleTortoiseProgram(program, winWidth=500, winHeight=500):
    root = Tk()
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.pack()
    canvas.create_text(winWidth/2, winHeight/2,
                       text='Go Tortoise Go!')
    root.mainloop()

def testRunSimpleTortoiseProgram1():
    runSimpleTortoiseProgram("""
# This is a simple tortoise program
color blue
move 50

left 90

color red
move 100

color none # turns off drawing
move 50

right 45

color green # drawing is on again
move 50

right 45

color orange
move 50

right 90

color purple
move 100
""", 300, 400)

def testRunSimpleTortoiseProgram2():
    runSimpleTortoiseProgram("""
# Y
color red
right 45
move 50
right 45
move 50
right 180
move 50
right 45
move 50
color none # space
right 45
move 25

# E
color green
right 90
move 85
left 90
move 50
right 180
move 50
right 90
move 42
right 90
move 50
right 180
move 50
right 90
move 43
right 90
move 50  # space
color none
move 25

# S
color blue
move 50
left 180
move 50
left 90
move 43
left 90
move 50
right 90
move 42
right 90
move 50
""")

def testRunSimpleTortoiseProgram():
    print("Testing runSimpleTortoiseProgram()...")
    print("Since this is graphics, this test is not interactive.")
    print("Inspect each of these results manually to verify them.")
    testRunSimpleTortoiseProgram1()
    testRunSimpleTortoiseProgram2()
    print("Done!")

#################################################
# Test Functions
#################################################


def testbuggyCleanUpCode():
    print("Testing buggyCleanUpCode()...", end="")
    code = '''# Y
color red
right 45
move 50
right 45
move 50
right 180
move 50
right 45
move 50
color none # space
right 45
move 25

# E
color green
right 90
move 85
left 90
move 50
right 180
move 50
right 90
move 42
right 90
move 50
right 180
move 50
right 90
move 43
right 90
move 50  # space
color none
move 25

# S
color blue
move 50
left 180
move 50
left 90
move 43
left 90
move 50
        right 90
move 42
                right 90
move 50'''
    assert(buggyCleanUpCode(code) == '''color red
right 45
move 50
right 45
move 50
right 180
move 50
right 45
move 50
color none 
right 45
move 25
color green
right 90
move 85
left 90
move 50
right 180
move 50
right 90
move 42
right 90
move 50
right 180
move 50
right 90
move 43
right 90
move 50  
color none
move 25
color blue
move 50
left 180
move 50
left 90
move 43
left 90
move 50
        right 90
move 42
                right 90
move 50''')
    
    
    
    
    
    
    code = """def buggyCleanUpCode(code):
    lines = code.splitlines()

    for i in range(len(lines)):
        codeLine = lines[i]
        else:
            lines.pop(i)
        else:
            # Get rid of comments
            commentIndex = codeLine.find
            lines[i] = codeLine[:commentIndex]
    """
    assert(buggyCleanUpCode(code) == """def buggyCleanUpCode(code):
    lines = code.splitlines()
    for i in range(len(lines)):
        codeLine = lines[i]
        else:
            lines.pop(i)
        else:
            commentIndex = codeLine.find
            lines[i] = codeLine[:commentIndex]""")
    print ("Passed!")

def testBestScrabbleScore():
    print("Testing bestScrabbleScore()...", end="")
    def dictionary1(): return ["a", "b", "c"]
    def letterScores1(): return [1] * 26
    def dictionary2(): return ["xyz", "zxy", "zzy", "yy", "yx", "wow"] 
    def letterScores2(): return [1+(i%5) for i in range(26)]
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("ace")) ==
                                        (["a", "c"], 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("z")) ==
                                        None)
    # x = 4, y = 5, z = 1
    # ["xyz", "zxy", "zzy", "yy", "yx", "wow"]
    #    10     10     7     10    9      -
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyz")) ==
                                         (["xyz", "zxy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyzy")) ==
                                        (["xyz", "zxy", "yy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyq")) ==
                                        ("yx", 9))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("yzz")) ==
                                        ("zzy", 7))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("wxz")) ==
                                        None)
    print("Passed!")

def testRunSimpleProgram():
    print("Testing runSimpleProgram()...", end="")
    largest = """! largest: Returns max(A0, A1)
                   L0 - A0 A1
                   JMP+ L0 a0
                   RTN A1
                   a0:
                   RTN A0"""
    assert(runSimpleProgram(largest, [5, 6]) == 6)
    assert(runSimpleProgram(largest, [6, 5]) == 6)

    sumToN = """! SumToN: Returns 1 + ... + A0
                ! L0 is a counter, L1 is the result
                L0 0
                L1 0
                loop:
                L2 - L0 A0
                JMP0 L2 done
                L0 + L0 1
                L1 + L1 L0
                JMP loop
                done:
                RTN L1"""
    assert(runSimpleProgram(sumToN, [5]) == 1+2+3+4+5)
    assert(runSimpleProgram(sumToN, [10]) == 10*11//2)
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testbuggyCleanUpCode()
    testBestScrabbleScore()
    testRunSimpleTortoiseProgram()
    testRunSimpleProgram()

def main():
    cs112_f17_week4_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
