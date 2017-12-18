#Derek Li (derekl1) Zhongyi (Sean) Gao (zhongyig) Ray Boppana (rbopanna)
#################################################
# Lab2
#################################################

import cs112_f17_week2_linter
import math

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

# Put your solution to getKthDigit here!

# See if you can rewrite isPrime from lecture here!

#################################################

def numberLength(x):
    n = 0
    while x>0:
        x=(x//10)
        n+=1
    return n
    
def getKthDigit(n, k):
    kDigit = (abs(n)//(10**k))%10
    return kDigit
    
def countMatchingDigits(x, y):
    xLength = numberLength(x)
    yLength = numberLength(y)
    i = 0
    matchingDigits = 0
    while (i<xLength):
        x1 = getKthDigit(x,i)
        k=0
        while (k<yLength):
            y1 = getKthDigit(y,k)
            if x1==y1:
                matchingDigits+=1 
            k+=1 
        i+=1
    return matchingDigits

def isPrime(n):
    if (n < 2):
        return False
    for factor in range(2,n):
        if (n % factor == 0):
            return False
    return True
    

def rotateNumber(x):
    num1 = getKthDigit(x,0)
    xLength = numberLength(x)
    rotateNumber = (x//10)+num1*10**(xLength-1)
    return rotateNumber

def isCircularPrime(x):
    if isPrime(x) == False:
        return False
    xLength = numberLength(x)
    for counter in (0,xLength+1):
        x=rotateNumber(x)
        y = isPrime(x)
        if y == False:
            return False
        counter+=1
    return True

def nthCircularPrime(n):
    found = 0
    guess = 0
    while (found <= n):
        guess += 1
        if (isCircularPrime(guess)):
            found += 1
    return guess

def flipNumber(x):
    flippedNumber=0
    numLength = numberLength(x)
    if x<=11:
        return False
    if isPrime(x)==True:
        for counter in range(numLength):
            number = (x//(10**counter))%10
            flippedNumber+=number*10**(numLength-counter-1)
        if isPrime(flippedNumber)==False or x == flippedNumber:
            return False
        return flippedNumber
    else:
        return False


def nthEmirpsPrime(n):
    found = 0
    guess = 0
    while (found <= n):
        guess += 1
        if (flipNumber(guess)):
            found += 1
    return guess

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

#################################################
# Test Functions
#################################################

def testNumberLength():
    print('Testing numberLength()... ', end='')
    assert(numberLength(12) == 2)
    assert(numberLength(3) == 1)
    assert(numberLength(89) == 2)
    assert(numberLength(12345) == 5)
    assert(numberLength(120021) == 6)
    assert(numberLength(5000) == 4)
    print('Passed!')

def testCountMatchingDigits():
    print('Testing countMatchingDigits()... ', end='')
    assert(countMatchingDigits(1234, 2071) == 2)
    assert(countMatchingDigits(2203, 1527) == 2)
    assert(countMatchingDigits(5, 1253) == 1)
    assert(countMatchingDigits(18737, 7) == 2)
    assert(countMatchingDigits(1220, 7322) == 4)
    assert(countMatchingDigits(1234, 5678) == 0)
    print('Passed!')

def testRotateNumber():
    print('Testing rotateNumber()... ', end='')
    assert(rotateNumber(1234) == 4123)
    assert(rotateNumber(4123) == 3412)
    assert(rotateNumber(3412) == 2341)
    assert(rotateNumber(2341) == 1234)
    assert(rotateNumber(5) == 5)
    assert(rotateNumber(111) == 111)
    print('Passed!')

def testIsCircularPrime():
    print('Testing isCircularPrime()... ', end='')
    assert(isCircularPrime(2) == True)
    assert(isCircularPrime(11) == True)
    assert(isCircularPrime(13) == True)
    assert(isCircularPrime(79) == True)
    assert(isCircularPrime(197) == True)
    assert(isCircularPrime(1193) == True)
    print('Passed!')

def testNthCircularPrime():
    print('Testing nthCircularPrime()... ', end='')
    assert(nthCircularPrime(0) == 2)
    assert(nthCircularPrime(4) == 11)
    assert(nthCircularPrime(5) == 13)
    assert(nthCircularPrime(11) == 79)
    assert(nthCircularPrime(15) == 197)
    assert(nthCircularPrime(25) == 1193)
    print('Passed!')

def testNthEmirpsPrime():
    print('Testing nthEmirpsPrime()... ', end='')
    assert(nthEmirpsPrime(0) == 13)
    assert(nthEmirpsPrime(5) == 73)
    assert(nthEmirpsPrime(10) == 149)
    assert(nthEmirpsPrime(20) == 701)
    assert(nthEmirpsPrime(30) == 941)
    print('Passed.')

#################################################
# testAll and main
#################################################

def testAll():
    testNumberLength()
    testCountMatchingDigits()
    testRotateNumber()
    testIsCircularPrime()
    testNthCircularPrime()
    testNthEmirpsPrime()

def main():
    cs112_f17_week2_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
