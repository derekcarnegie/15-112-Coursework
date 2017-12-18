#################################################\
# Derek Li (derekl1) Zhongyi (Sean) Gao zhongyig
# Lab3
#################################################

import cs112_f17_week3_linter
import math
import string
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

def longestCommonSubstring(s1, s2):
    commonStr = ""
    x=1
    y=1
    for x in range(len(s1)+1):
        lengths1 = len(s1)
        for y in range(len(s1)+1):
            if s1[x-1:(lengths1)] in s2:
                if len(s1[x-1:(lengths1)])>len(commonStr):
                    commonStr=s1[x-1:(lengths1)]
                elif commonStr!="" and len(s1[x-1:(lengths1)])==len(commonStr):
                    if ord(s1[x-1:x])<ord(commonStr[:1]):
                        commonStr=s1[x-1:(lengths1)]
            lengths1-=1
    return commonStr
            
            

def bestStudentAndAvg(gradebook):
    averageGrade  = -214748364 #lowest value for int
    bestName=""
    name = ""
    sumGrades = 0
    divisor = 0
    for lines in gradebook.splitlines():#split lines of gradebook
        #ignores lines that start with # or empty space
        if not(lines.startswith("#")) or not(lines.startswith(" ")):
            #splits individual element by commas
            for commas in lines.split(","):
                #separates out digits or - (negative numbers
                #do not pass .isdigit
                if commas.isdigit() or "-" in commas:
                    sumGrades+=int(commas)
                    divisor+=1
                #separates out each name
                if commas.isalpha():
                    name = commas
            #ensures higher average grade remains and gives 
            #bestName to the person with the highest average grade
            if divisor!=0 and roundHalfUp(sumGrades/divisor) >= averageGrade:
                averageGrade = roundHalfUp(sumGrades/divisor)
                bestName = name
        #reset variables
        sumGrades=0
        divisor=0
    return bestName + ":"+ str(averageGrade)
        

def encodeColumnShuffleCipher(message, key):
    initialGrid = ""
    newGrid = ""
    finalMessage  = ""
    #adds dashes to end of message string based off remainder
    message += "-"*(len(key)-(len(message)-1)%len(key)-1)
    #decides how many rows there are
    for row in range(math.ceil(len(message)/len(key))):
        newLine = message[row*len(key):(row+1)*len(key)]
        initialGrid += newLine
        initialGrid +="\n"
    #splits initialGrid into separate lines
    for newLines in initialGrid.splitlines():
        #decides which columns to rearrange
        for rearrange in range(len(key)):
            newGrid += newLines[int(key[rearrange])]
        newGrid+="\n"
    #retreives message from rearranged grid vertically
    for i in range(len(key)):
        for newLines2 in newGrid.splitlines():
            finalMessage+=newLines2[i]
    #returns the result
    return key + (finalMessage)

    
    
    

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

#################################################
# Test Functions
#################################################

def testLongestCommonSubstring():
    print("Testing longestCommonSubstring()...", end="")
    assert(longestCommonSubstring("abcdef", "abqrcdest") == "cde")
    assert(longestCommonSubstring("abcdef", "ghi") == "")
    assert(longestCommonSubstring("", "abqrcdest") == "")
    assert(longestCommonSubstring("abcdef", "") == "")
    assert(longestCommonSubstring("abcABC", "zzabZZAB") == "AB")
    print("Passed!")

def testBestStudentAndAvg():
    print("Testing bestStudentAndAvg()...", end="")
    gradebook = """
# ignore  blank lines and lines starting  with  #'s
wilma,91,93
fred,80,85,90,95,100
betty,88
"""
    assert(bestStudentAndAvg(gradebook) ==  "wilma:92")
    gradebook   =   """
#   ignore  blank   lines   and lines   starting    with    #'s
wilma,93,95

fred,80,85,90,95,100
betty,88
"""
    assert(bestStudentAndAvg(gradebook) ==  "wilma:94")
    gradebook = "fred,0"
    assert(bestStudentAndAvg(gradebook) ==  "fred:0")
    gradebook = "fred,-1\nwilma,-2"
    assert(bestStudentAndAvg(gradebook) ==  "fred:-1")
    gradebook = "fred,100"
    assert(bestStudentAndAvg(gradebook) ==  "fred:100")
    gradebook = "fred,100,110"
    assert(bestStudentAndAvg(gradebook) ==  "fred:105")
    gradebook = "fred,49\nwilma" + ",50"*50
    assert(bestStudentAndAvg(gradebook) ==  "wilma:50")
    

    
    print("Passed!")
    
    
def testEncodeColumnShuffleCipher():
    print("Testing encodeColumnShuffleCipher()...", end="")
    
    msg = "WEATTACKATDAWN"
    result = "0213WTAWACD-EATNTKA-"
    assert(encodeColumnShuffleCipher(msg, "0213") == result)
    
    msg = "SUDDENLYAWHITERABBITWITHPINKEYESRANCLOSEBYHER"
    result = "210DNAIRBWHNYRCSYRUEYHEBTTIESNOBESDLWTAIIPKEALEH"
    assert(encodeColumnShuffleCipher(msg,"210") == result)
    
   
    print("Passed!")
    


#################################################
# testAll and main
#################################################

def testAll():
    testLongestCommonSubstring()
    testBestStudentAndAvg()
    testEncodeColumnShuffleCipher()

def main():
    cs112_f17_week3_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
