def isEinNumber(n):
    counter = 0
    digit = 0
    while (counter<=n):
        if n%10>digit:
            digit=n%10
        else:
            return False
        if digit%2==1:
            return False
        n//=10
        counter+=1
    return True

def nthEinNumber(n):
    found = 0
    guess = 0
    while (found <= n):
        guess += 1
        if (isEinNumber(guess)):
            found += 1
    return guess
    
