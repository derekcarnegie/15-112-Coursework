#Derek Li (derekl1)
#HW 7
#################################################

#import cs112_f17_week7_linter
import math, string, copy, time, random

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
    
def swap(a, i, j):
    (a[i], a[j]) = (a[j], a[i])

#################################################
# Problems
#################################################


    
def invertDictionary(d):
    #inverts key within dictionary
    a = dict()
    for key in d:
        #iterates through the keys in dictionary d
        newKey = d.get(key)
        if a.get(newKey)!=None:
            #if the key already has a value the next value is appended
            a[newKey].add(key)
        else:
            #takes the value from the previous set and 
            #makes it the key of the new dictionary
            a[newKey] = set([key])
    return a

def friendsOfFriends(d):
    #finds the friends of friends for each dictionary
    a = dict()
    for key in d:
        a[key] = set([])
        #sets equal to empy set
        for key2 in d[key]:
            #finds friends
            for key3 in d[key2]:
                #finds friends of friends
                if key != key3 and key3 not in d[key]:
                    #ensures that original friends and themselves are 
                    #not counted
                    a[key].add(key3)
    return a

def instrumentedSelectionSort(a):#from site
    startTime = time.time()
    #finds the initial time at the beginning of the function
    n = len(a)
    swapCount = 0
    comparison = 0
    #initializes variable to increment per swap and comparison
    for startIndex in range(n):
        minIndex = startIndex
        for i in range(startIndex+1, n):
            if (a[i] < a[minIndex]):
                minIndex = i
            comparison +=1
            #every iteration is a comparison
        swap(a, startIndex, minIndex)
        swapCount+=1
        #after each swap the swap count is incremented by 1
    return comparison,swapCount,time.time()-startTime

def instrumentedBubbleSort(a):#from site
    startTime = time.time()
    #finds the initial time when the function is called
    n = len(a)
    end = n
    swapped = True
    comparison = 0
    swapCount = 0
    #initializes the swapCount and comparison values which are incremented
    #each time they happen
    while (swapped):
        swapped = False
        for i in range(1, end):
            comparison+=1
            #increments during each comparison
            if (a[i-1] > a[i]):
                swap(a, i-1, i)
                swapCount+=1
                #increments after each swap
                swapped = True
        end -= 1
    return(comparison,swapCount,time.time()-startTime)
    
def selectionSortVersusBubbleSort():
    #compares the run time, swap count, and comparisons of BubbleSort and 
    #SelectionSort
    for i in range(1,4):
        #allows bubble and selection sort to run through variable length lists
        for k in range(3):
            #used to display comparisons, swaps, and time taken
            if k==0:
                print("The number of comparisons for BubbleSort "+ \
                str(instrumentedBubbleSort(generateRandomNumList(i*800))[k]))
                print("The number of comparisons for SelectionSort "+ \
                str(instrumentedSelectionSort(generateRandomNumList(i*800))[k]))
            if k==1:
                print("The number of swaps for BubbleSort "+ \
                str(instrumentedBubbleSort(generateRandomNumList(i*800))[k]))
                print("The number of swaps for SelectionSort "+ \
                str(instrumentedSelectionSort(generateRandomNumList(i*800))[k]))
            if k==2:
                print("The time taken for BubbleSort "+ \
                str(instrumentedBubbleSort(generateRandomNumList(i*800))[k]))
                print("The time taken for SelectionSort "+ \
                str(instrumentedSelectionSort(generateRandomNumList(i*800))[k]))
    return
    
def generateRandomNumList(length):
    #used to generate random list for bubble and selection sort comparison
    a =[0 for i in range(length)]
    for i in range(length):
        a[i]=(random.randint(0,1000000))
        #range of random values put into list
    return a
    
######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

#################################################
# Test Functions
#################################################


def testinvertDictionary():
    print("Testing largestSumofPairs()...", end ="")
    assert(invertDictionary({1:2, 2:3, 3:4, 5:3}) == \
    {2:set([1]), 3:set([2,5]), 4:set([3])})
    print("Passed!")
    
def testfriendsOfFriends():
    print("Testing friendsOfFriends()...", end ="")
    d = dict()

    d["jon"] = set(["arya", "tyrion"])
    d["tyrion"] = set(["jon", "jaime", "pod"])
    d["arya"] = set(["jon"])
    d["jaime"] = set(["tyrion", "brienne"])
    d["brienne"] = set(["jaime", "pod"])
    d["pod"] = set(["tyrion", "brienne", "jaime"])
    d["ramsay"] = set()
    answer =     {'tyrion': {'arya', 'brienne'}, 
    'pod': {'jon'}, 
    'brienne': {'tyrion'}, 
    'arya': {'tyrion'}, 
    'jon': {'pod', 'jaime'}, 
    'jaime': {'pod', 'jon'}, 
    'ramsay': set()}
    assert (friendsOfFriends(d) == answer)
    
    print("Passed!")
    

#################################################
# testAll and main
#################################################

def testAll():
    testinvertDictionary()
    testfriendsOfFriends()
    selectionSortVersusBubbleSort()
    
def main():
    #cs112_f17_week7_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
