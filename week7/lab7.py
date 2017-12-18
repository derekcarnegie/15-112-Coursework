#Derek Li (derekl1)
#Trevor Arashiro (tarashir)
# Lab 7
#################################################

import cs112_f17_week7_linter
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

''' 
slow1: 
1. Finds the length of the list a
2. The worst case big-oh runtime is O(N) since copy.copy(a) and the while loop 
are both O(N)
3. 
def fast1(a):
    return len(a)
4. The worst case big-oh runtime is O(1) since the function is a constant 
runtime function.


slow2(a):
1. Checks if the list has any duplicate values, and if it does it returns False.
 But if the list has no duplicate values, True is returned.
2. O(N^2) since there is two for loops which each have runtime O(N). Since they 
are nested they are multiplied together so the worst case total runtime is
 O(N^2)
3.
def fast2(a):
    return (len(set(a)) == len(a))
4. The worst case run time for this function is O(N) since the len(set(a)) 
function has a runtime of O(N) and the length function has a worst case run 
function of O(1). Thus the overall runtime = O(n)

slow3(a, b):
1. Returns the values that are in b and not in a
2. O(N^2) since the for loop has a worst case run time of O(N) and nested 
within this loop is the statement (if c not in a) which also has a runtime of
 O(N). Thus, the worst case runtime is O(N^2).
3.
def fast3(a,b):
    total = 0
    b = set(a)
    for i in b:
        if i not in b:
            total += 1
    return total
    
4. This has a worst case run time of O(N) since the for loop has a runtime of
 O(N) and since s is a set the line (if i not in s) has a runtime of O(1). Thus,
  the worst case run time is O(N)

slow4(a, b):
1. This function returns the biggest difference between an element of a and an 
element of b
2. Each for loop has a worst case run time of O(N) and since the for loops are 
nested the total worst case run time is O(N^2)
3.
def fast4(a,b):
    assert(len(a) == len(b))
    minA = min(a)
    maxA = max(a)
    minB = min(b)
    maxB = max(b)
    return max(abs(minA-maxB),abs(minB-maxA))
4. The assert and each min and max function has a worst case run time of O(N).
 The last line has a worst case run time of O(1) thus the total worst case 
 runtime of the function is O(N)

slow5(a, b):
1. This function takes lists a and b and returns the absolute smallest 
difference between an element of a and an element of b.
2. Each for loop has a worst case run time of O(N) and since they are nested
 the total function worst case run time is O(N^2)
3.

import bisect
# taken from 
# https://www.cs.cmu.edu/~112/notes/notes-efficiency.html#sorting2
def merge(a, start1, start2, end):
    index1 = start1
    index2 = start2
    length = end - start1
    aux = [None] * length
    for i in range(length):
        if ((index1 == start2) or
            ((index2 != end) and (a[index1] > a[index2]))):
            aux[i] = a[index2]
            index2 += 1
        else:
            aux[i] = a[index1]
            index1 += 1
    for i in range(start1, end):
        a[i] = aux[i - start1]

# taken from 
# https://www.cs.cmu.edu/~112/notes/notes-efficiency.html#sorting2
def mergeSort(a):
    n = len(a)
    step = 1
    while (step < n):
        for start1 in range(0, n, 2*step):
            start2 = min(start1 + step, n)
            end = min(start1 + 2*step, n)
            merge(a, start1, start2, end)
        step *= 2

def minDiff(a,b):
    assert(len(a) == len(b))
    minDiff = abs(a[0]-b[0])
    mergeSort(b)
    for i in a:
        bisectionPoint = bisect.bisect(b,i)
        if bisectionPoint == len(b):
            if abs(i-b[bisectionPoint-1]) < minDiff:
                minDiff = abs(i-b[bisectionPoint-1])
        else:
            currentMin = min(abs(i-b[bisectoinPoint-1]),
                    abs(i-b[bisectionPoint]))
            if (currentMin < minDiff):
                minDiff = currentMin 
    return minDiff

4. Merge sort has a worst case run time of O(Nlog(N)) and every operation 
within the for loop has a worst case run time of O(1). Thus, the total worst
 case run time of the function is O(Nlog(N))

'''

    
def largestSumOfPairs(a):
    #finds the largest sum of pairs in a list of integers
    if len(a)<=1:
        return None
        #if list is empty or has 1 element there is no pairs to be summed
    maxNum = max(a)
    maxNumIndex = a.index(maxNum)
    maxNum = a.pop(maxNumIndex)
    maxNum2 = max(a)
    maxNumIndex2 = a.index(maxNum2)
    maxNum2 = a.pop(maxNumIndex2)
    #finds the max of the list, then removes that value
    #then it finds the new highest value (second highest value)
    return maxNum+maxNum2

def containsPythagoreanTriple(a):
    #determines if there is a pythagorean triple in the list
    if len(a)<3:
        return False
        #immediately returns false if the list is less than 3 elements long
    for i in range(len(a)):
        a[i]=a[i]**2
        #squares values within the list
    setOfPythagTrip = set(a)
    for j in range(len(a)):
        for k in range(len(a)):
            if a[j]+a[k] in setOfPythagTrip:
                #checks if the squared values together are the c^2 value
                return True
    return False
    
######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

#################################################
# Test Functions
#################################################


def testLargestSumofPairs():
    print("Testing largestSumofPairs()...", end ="")
    assert (largestSumOfPairs([1])==None)
    assert (largestSumOfPairs([8,4,2,8])==16)
    assert (largestSumOfPairs([10,10,10,15,5])==25)
    print("Passed!")
    
def testcontainsPythagoreanTriple():
    print("Testing containsPythagoreanTriple()...", end ="")
    assert (containsPythagoreanTriple([1,3,6,2,5,1,4])==True)
    assert (containsPythagoreanTriple([1,2,3,5,8,9])==False)
    assert (containsPythagoreanTriple([9,4,3,15,13,8,17])==True)
    print ("Passed!")
    

#################################################
# testAll and main
#################################################

def testAll():
    testLargestSumofPairs()
    testcontainsPythagoreanTriple()

def main():
    cs112_f17_week7_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
