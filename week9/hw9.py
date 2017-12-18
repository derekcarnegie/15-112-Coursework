#################################################
#Derek Li
#derekl1
# Hw9
#
# No iteration! no 'for' or 'while'.  Also, no 'zip' or 'join'.
# You may add optional parameters
# You may use wrapper functions
#
#################################################

import cs112_f17_week9_linter

def almostEqual(x, y, epsilon = 10**-8):
    return abs(x-y) < epsilon

def findingOperation(L,i):
    #recursively searches for operation
    if isinstance(L[i],int):
        #if the value is an integer goes to the next list index backwards
        return findingOperation(L,i-1)
    else:
        return i
        #returns index of operation
        
##############################################
# Recursive questions
##############################################

def powerSum(n, k):
    #finds the power sum of n and k
    if k<0 or n==0:
        #all the cases the power sum is 0
        return 0
    else:
        #goes through every value of n until n==0
        return powerSum(n-1,k)+n**k

def power(base, expt):
    #from notes
    # assume expt is non-negative integer
    if (expt == 0):
        return 1
    elif (expt % 2 == 0):
        return power(base, expt//2)**2
    else:
        return base * power(base, expt//2)**2
    
def sumOfSquaresOfDigits(x):
    #finds the sum of the squares of digits
    if x<1:
        return 0
    else:
        return (power((x)%10,2)+sumOfSquaresOfDigits(x//10))
        #finds the digit squares it and then calls itself again after 
        #getting rid of the digit that was just taken

def isHappyNumber(x):
    #determines if x is a happy number
    if x<1:
        #any number less than 1 is a happy number
        return False
    if x!=1 and x!=4:
        #squares the digit if x is not equal to 1 or 4
        x = sumOfSquaresOfDigits(x)
    if x==1:
        #is happy
        return True
    if x==4:
        #is not happy
        return False
    else:
        #recalls self if neither is fulfilled
        return isHappyNumber(x)

def evalPrefixNotation(L):
    #evaluates list in prefix notation
    if len(L)==1:
        #when no operation takes place
        return L[0]
    operation = findingOperation(L,len(L)-3)
    #index of operation
    first = L.pop(operation+1)
    second = L.pop(operation+1)
    #finds the values of the indices next to the operation (values being
    #operated on)
    if L[operation]=="*":
        value=first*second
    elif L[operation]=="-":
        value=first-second
    elif L[operation]=="+":
        value=first+second
    L[operation] = value
    #changes the operation from symbol to the evaluated value
    return evalPrefixNotation(L)


##############################################
# OOP questions
##############################################

class VendingMachine(object):
    #uses OOP to pass test cases
    def __init__(self,bottles,price):
        #initializes variable in the vending machine class
        self.bottles=bottles
        self.price=price
        self.paid=0
    def __repr__(self):
        #returns for the str function
            if self.bottles == 1:
                #if there is only one bottle 
                if self.paid%100==0:
                    #whole digit being paid
                    if self.price%100==0:
                        #price is a whole dollar value
                        return "Vending Machine:<%d bottle; $%d each; $%d"\
                                %(self.bottles,self.price/100,self.paid/100)\
                                + " paid>"
                    return "Vending Machine:<%d bottle; $%.2f each; $%d"\
                            %(self.bottles,self.price/100,self.paid/100)\
                            + " paid>"
                if self.price%100 == 0:
                    #price is a whole dollar value
                    return "Vending Machine:<%d bottle; $%d each; $%.2f"\
                            %(self.bottles,self.price/100,self.paid/100)\
                            + " paid>"
                return "Vending Machine:<%d bottle; $%.2f each; $%.2f"\
                        %(self.bottles,self.price/100,self.paid/100)+ " paid>"
                    
            if not (self.paid%100 == 0):
                #if the paid amount is not a whole dollar value
                if self.price%100==0:
                    #if the price is a whole dollar value
                    return "Vending Machine:<%d bottles; $%d each; $%.2f"\
                            %(self.bottles,self.price/100,self.paid/100)+\
                            " paid>"
                return "Vending Machine:<%d bottles; $%.2f each; $%.2f"\
                        %(self.bottles,self.price/100,self.paid/100)+" paid>"
            if self.price%100==0:
                #if the price is a full dollar value
                return "Vending Machine:<%d bottles; $%d each; $%d"\
                        %(self.bottles,self.price/100,self.paid/100)+" paid>"
            return "Vending Machine:<%d bottles; $%.2f each; $%d"\
                    %(self.bottles,self.price/100,self.paid/100)+" paid>"
                
    def isEmpty(self):
        #checks if the machine is empty
        if self.bottles>0:
            return False
        else:
            return True
    def getBottleCount(self):
        #returns the current number of bottles
        return self.bottles
    def stillOwe(self):
        #checks how much is owed for the next bottle
        return self.price-self.paid
    def insertMoney(self,insertedMoney):
        #performs various operations depending on how much money is inputted
        self.paid+=insertedMoney
        if self.bottles==0:
            #displays how much was paid if the machine is empty
            b=self.paid
            self.paid=0
            return ("Machine is empty",b)
        if (self.price-self.paid)%100!=0:
            if (self.price-self.paid)>0:
                return ("Still owe $%0.2f"%((self.price-self.paid)/100),0)
        if (self.price-self.paid)%100==0:
            if (self.price-self.paid)>0:
                return ("Still owe $%d"%((self.price-self.paid)/100),0)
        if self.price==self.paid:
            #if the bottle is bought in exact change
            self.bottles-=1
            self.paid = 0
            return ("Got a bottle!",0)
        if self.price<self.paid:
            #if the bottle is overpayed for and needs to be refunded some money
            self.bottles-=1
            a = self.paid
            self.paid=0
            return ("Got a bottle!",abs(self.price-a))
    def stockMachine(self,stockedAmount):
        #adds to the current number of bottles
        self.bottles+=stockedAmount
    def __eq__(self,other):
        #checks that the machines are equal in every way
        if isinstance(other,VendingMachine):
            return (self.bottles == other.bottles and self.price==other.price\
            and self.paid==other.paid)
        else:
            return False
    def __hash__(self):
        #allows set to hash properly
        return hash(self.paid,)
    
    
#################################################
# Test Functions
#################################################

def testPowerSum():
    print('Testing powerSum()...', end='')
    assert(powerSum(4, 6) == 1**6 + 2**6 + 3**6 + 4**6)
    assert(powerSum(0, 6) == 0)
    assert(powerSum(4, 0) == 1**0 + 2**0 + 3**0 + 4**0)
    assert(powerSum(4, -1) == 0)
    print('Done!')

def testIsHappyNumber():
    print('Testing isHappyNumber()...', end='')
    assert(isHappyNumber(-7) == False)
    assert(isHappyNumber(1) == True)
    assert(isHappyNumber(2) == False)
    assert(isHappyNumber(97) == True)
    assert(isHappyNumber(98) == False)
    assert(isHappyNumber(404) == True)
    assert(isHappyNumber(405) == False)
    print('Done!')

def testEvalPrefixNotation():
    print('Testing evalPrefixNotation()...', end='')
    assert(evalPrefixNotation([42]) == 42)
    assert(evalPrefixNotation(['+', 3, 4]) == 7)
    assert(evalPrefixNotation(['-', 3, 4]) == -1)
    assert(evalPrefixNotation(['-', 4, 3]) == 1)
    assert(evalPrefixNotation(['+', 3, '*', 4, 5]) == 23)
    assert(evalPrefixNotation(['+', '*', 2, 3, '*', 4, 5]) == 26)
    assert(evalPrefixNotation(['*', '+', 2, 3, '+', 4, 5]) == 45)
    assert(evalPrefixNotation(['*', '+', 2, '*', 3, '-', 8, 7,
                               '+', '*', 2, 2, 5]) == 45)
    print('Done!')

def testVendingMachineClass():
    print("Testing Vending Machine class...", end="")
    # Vending machines have three main properties: 
    # how many bottles they contain, the price of a bottle, and
    # how much money has been paid. A new vending machine starts with no
    # money paid.
    vm1 = VendingMachine(100, 125)
    assert(str(vm1) == "Vending Machine:<100 bottles; $1.25 each; $0 paid>")
    assert(vm1.isEmpty() == False)
    assert(vm1.getBottleCount() == 100)
    assert(vm1.stillOwe() == 125)
    
    # When the user inserts money, the machine returns a message about their
    # status and any change they need as a tuple.
    assert(vm1.insertMoney(20) == ("Still owe $1.05", 0))
    assert(vm1.stillOwe() == 105)
    assert(vm1.getBottleCount() == 100)
    assert(vm1.insertMoney(5) == ("Still owe $1", 0))
    
    # When the user has paid enough money, they get a bottle and 
    # the money owed resets.
    assert(vm1.insertMoney(100) == ("Got a bottle!", 0))
    assert(vm1.getBottleCount() == 99)
    assert(vm1.stillOwe() == 125)
    assert(str(vm1) == "Vending Machine:<99 bottles; $1.25 each; $0 paid>")
    
    # If the user pays too much money, they get their change back with the
    # bottle.
    assert(vm1.insertMoney(500) == ("Got a bottle!", 375))
    assert(vm1.getBottleCount() == 98)
    assert(vm1.stillOwe() == 125)
    
    # Machines can become empty
    vm2 = VendingMachine(1, 120)
    assert(str(vm2) == "Vending Machine:<1 bottle; $1.20 each; $0 paid>")
    assert(vm2.isEmpty() == False)
    assert(vm2.insertMoney(120) == ("Got a bottle!", 0))
    assert(vm2.getBottleCount() == 0)
    assert(vm2.isEmpty() == True)
    
    # Once a machine is empty, it should not accept money until it is restocked.
    assert(str(vm2) == "Vending Machine:<0 bottles; $1.20 each; $0 paid>")
    assert(vm2.insertMoney(25) == ("Machine is empty", 25))
    assert(vm2.insertMoney(120) == ("Machine is empty", 120))
    assert(vm2.stillOwe() == 120)
    vm2.stockMachine(20) # Does not return anything
    assert(vm2.getBottleCount() == 20)
    assert(vm2.isEmpty() == False)
    assert(str(vm2) == "Vending Machine:<20 bottles; $1.20 each; $0 paid>")
    assert(vm2.insertMoney(25) == ("Still owe $0.95", 0))
    assert(vm2.stillOwe() == 95)
    vm2.stockMachine(20)
    assert(vm2.getBottleCount() == 40)
    
    # We should be able to test machines for basic functionality
    vm3 = VendingMachine(50, 100)
    vm4 = VendingMachine(50, 100)
    vm5 = VendingMachine(20, 100)
    vm6 = VendingMachine(50, 200)
    vm7 = "Vending Machine"
    assert(vm3 == vm4)
    assert(vm3 != vm5)
    assert(vm3 != vm6)
    assert(vm3 != vm7) # should not crash!
    s = set()
    assert(vm3 not in s)
    s.add(vm4)
    assert(vm3 in s)
    s.remove(vm4)
    assert(vm3 not in s)
    assert(vm4.insertMoney(50) == ("Still owe $0.50", 0))
    assert(vm3 != vm4)
    vm3 = VendingMachine(50, 100)
    vm4 = VendingMachine(50, 100)
    vm5 = VendingMachine(20, 100)
    vm6 = VendingMachine(50, 200)
    vm7 = "Vending Machine"
    assert(vm3 == vm4)
    assert(vm3 != vm5)
    assert(vm3 != vm6)
    assert(vm3 != vm7) # should not crash!
    s = set()
    assert(vm3 not in s)
    s.add(vm4)
    assert(vm3 in s)
    s.remove(vm4)
    assert(vm3 not in s)
    assert(vm4.insertMoney(50) == ("Still owe $0.50", 0))
    assert(vm3 != vm4)
    print("Done!")
    vm8 = VendingMachine(1, 100)
    vm9 = VendingMachine(1, 102)
    vm10 = VendingMachine(2, 100)
    vm11 = VendingMachine(2, 102)
    assert(str(vm8) == "Vending Machine:<1 bottle; $1 each; $0 paid>")
    assert(str(vm9) == "Vending Machine:<1 bottle; $1.02 each; $0 paid>")
    assert(str(vm10) == "Vending Machine:<2 bottles; $1 each; $0 paid>")
    assert(str(vm11) == "Vending Machine:<2 bottles; $1.02 each; $0 paid>")
    vm8.insertMoney(12)
    vm9.insertMoney(12)
    vm10.insertMoney(12)
    vm11.insertMoney(12)
    assert(str(vm8) == "Vending Machine:<1 bottle; $1 each; $0.12 paid>")
    assert(str(vm10) == "Vending Machine:<2 bottles; $1 each; $0.12 paid>")
    assert(str(vm11) == "Vending Machine:<2 bottles; $1.02 each; $0.12 paid>")
    assert(str(vm9) == "Vending Machine:<1 bottle; $1.02 each; $0.12 paid>")
    print("Done!")

##############################################
# testAll and main
##############################################

def testAll():
    testPowerSum()
    testIsHappyNumber()
    testEvalPrefixNotation()
    testVendingMachineClass()

def main():
    cs112_f17_week9_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
