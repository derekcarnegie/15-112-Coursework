#################################################
# Hw4
#################################################

import cs112_f17_week11_linter
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

    
#################################################
# Problems
#################################################

class Gate(object):
    #To pass testGateClasses test function
    def __init__(self):
        #initializes the number of inputs that are needed and input list
        self.numInputs=2
        self.input = []
    def __str__(self):
        #formats string to match format
        output = (type(self).__name__).replace("Gate","")+\
        str(self.input).replace("[","(")
        output = output.replace("]",")")
        output = output.replace(" ","")
        return (output)
    def numberOfInputs(self):
        #returns the number of inputs
        return self.numInputs
    def setInput(self,index,condition):
        #sets the condition of the input
        if self.input==[]:
            self.input=[0]*self.numInputs
            #creates initial list
        self.input[index]=condition

class AndGate(Gate):
    #And logic
    def getOutput(self):
        #if anything is false the entire statement is false
        for i in range (self.numInputs):
            if self.input[i]==False:
                return False
        return True

class OrGate(Gate):
    #Or logic
    def getOutput(self):
        #if anything is true the entire statement is true
        for i in range (self.numInputs):
            if self.input[i]==True:
                return True
        return False
        
class NotGate(Gate):
    #Returnts opposite condition
    def getOutput(self):
        #returns the opposite condition of what is in the input
        if self.input[0]==True:
            return False
        else:
            return True
    def numberOfInputs(self):
        #number of inputs is always 1
        self.numInputs=1
        return self.numInputs

class ComplexNumber(object):
    #Passes testComplexNumberClass test case
    def __init__(self,*args):
        #initialzies real number and imaginary number of a complex number
        self.realNum=0
        self.imagPart=0
        if len(args)>=1:
            if isinstance(args[0],ComplexNumber):
                #clones values if the value is duplicated 
                self.realNum = args[0].realNum
                self.imagPart = args[0].imagPart
            elif len(args)==1:
                #when the imaginary part is 0
                for num in args:
                    self.realNum = num
                self.imagPart=0
            elif len(args)==2:
                #when both values are provided
                self.realNum = args[0]
                self.imagPart = args[1]
    def __repr__(self):
        #string format of complex number 
        return str(self.realNum) + "+" + str(self.imagPart) + "i"
    def realPart(self):
        #returns what the real part of the complex number is
        return self.realNum
    def imaginaryPart(self):
        #returns what the imaginary part of the complex number is
        return self.imagPart
    def __eq__(self,other):
        #checks if two values are equal
        if isinstance(other,int):
            #checks against integers
            return self.realNum==other
        if isinstance(other,ComplexNumber):
            #ensures that other is a part of class ComplexNumber
            if self.realNum==other.realNum and self.imagPart==other.imagPart:
                return True
            else:return False
        else:return False
    def getHashables(self):
        #Allows sets to be used properly
        return (self.realNum, ) # return a tuple of hashables
    def __hash__(self):
        #Allows sets to be used properly
        return hash(self.getHashables())
    initial=None
    #stores the singleton instance
    def getZero():
        #gets Zero
        if ComplexNumber.initial==None:
            ComplexNumber.initial=ComplexNumber(0)
        return ComplexNumber.initial
    
######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

#################################################
# Test Functions
#################################################

import types

def getLocalMethods(clss):
    # This is a helper function for the test function below.
    # It returns a sorted list of the names of the methods
    # defined in a class.
    result = [ ]
    for var in clss.__dict__:
        val = clss.__dict__[var]
        if (isinstance(val, types.FunctionType)):
            result.append(var)
    return sorted(result)

def testGateClasses():
    print("Testing Gate Classes... ", end="")

    # require methods be written in appropriate classes
    assert(getLocalMethods(Gate) == ['__init__', '__str__',
                                     'numberOfInputs', 'setInput'])
    assert(getLocalMethods(AndGate) == ['getOutput'])
    assert(getLocalMethods(OrGate) == ['getOutput'])
    assert(getLocalMethods(NotGate) == ['getOutput', 'numberOfInputs'])

    # make a simple And gate
    and1 = AndGate()
    assert(type(and1) == AndGate)
    assert(isinstance(and1, Gate) == True)
    assert(and1.numberOfInputs() == 2)
    and1.setInput(0, True)
    and1.setInput(1, False)
    # Hint: to get the name of the class given an object obj,
    # you can do this:  type(obj).__name__
    # You might do this in the Gate.__str__ method...
    assert(str(and1) == "And(True,False)")
    assert(and1.getOutput() == False)
    and1.setInput(1, True) # now both inputs are True
    assert(and1.getOutput() == True)
    assert(str(and1) == "And(True,True)")

    # make a simple Or gate
    or1 = OrGate()
    assert(type(or1) == OrGate)
    assert(isinstance(or1, Gate) == True)
    assert(or1.numberOfInputs() == 2)
    or1.setInput(0, False)
    or1.setInput(1, False)
    assert(or1.getOutput() == False)
    assert(str(or1) == "Or(False,False)")
    or1.setInput(1, True)
    assert(or1.getOutput() == True)
    assert(str(or1) == "Or(False,True)")

    # make a simple Not gate
    not1 = NotGate()
    assert(type(not1) == NotGate)
    assert(isinstance(not1, Gate) == True)
    assert(not1.numberOfInputs() == 1)
    not1.setInput(0, False)
    assert(not1.getOutput() == True)
    assert(str(not1) == "Not(False)")
    not1.setInput(0, True)
    assert(not1.getOutput() == False)
    assert(str(not1) == "Not(True)")

    print("Passed!")

def testComplexNumberClass():
    print("Testing ComplexNumber class... ", end="")
    # Do not use the builtin complex numbers in Python!
    # Only use integers!

    c1 = ComplexNumber(1, 2)
    assert(str(c1) == "1+2i")
    assert(c1.realPart() == 1)
    assert(c1.imaginaryPart() == 2)

    c2 = ComplexNumber(3)
    assert(str(c2) == "3+0i") # default imaginary part is 0
    assert(c2.realPart() == 3)
    assert(c2.imaginaryPart() == 0)

    c3 = ComplexNumber()
    assert(str(c3) == "0+0i") # default real part is also 0
    assert(c3.realPart() == 0)
    assert(c3.imaginaryPart() == 0)

    # Here we see that the constructor for a ComplexNumber
    # can take another ComplexNumber, which it duplicates
    c4 = ComplexNumber(c1)
    assert(str(c4) == "1+2i")
    assert(c4.realPart() == 1)
    assert(c4.imaginaryPart() == 2)

    assert((c1 == c4) == True)
    assert((c1 == c2) == False)
    assert((c1 == "Yikes!") == False) # don't crash here
    assert((c2 == 3) == True)

    s = set()
    assert(c1 not in s)
    s.add(c1)
    assert(c1 in s)
    assert(c4 in s)
    assert(c2 not in s)

    assert(ComplexNumber.getZero() == 0)
    assert(isinstance(ComplexNumber.getZero(), ComplexNumber))
    assert(ComplexNumber.getZero() == ComplexNumber())
    # This next one is the tricky part -- there should be one and
    # only one instance of ComplexNumber that is ever returned
    # every time you call ComplexNumber.getZero():
    assert(ComplexNumber.getZero() is ComplexNumber.getZero())
    # Hint: you might want to store the singleton instance
    # of the zero in a class attribute (which you should
    # initialize to None in the class definition, and then
    # update the first time you call getZero()).

    print("Passed!")



#################################################
# testAll and main
#################################################

def testAll():
    testGateClasses()
    testComplexNumberClass()
    

def main():
    cs112_f17_week11_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
