#################################################
# Lab9
#Derek Li (derekl1)
#Trevor Arashiro (tarashir)
# No iteration! no 'for' or 'while'.  Also, no 'zip' or 'join'.
# You may add optional parameters
# You may use wrapper functions
#
#################################################

import cs112_f17_week9_linter
import math
def almostEqual(x, y, epsilon = 10**-8):
    return abs(x-y) < epsilon

##############################################
# Recursive questions
##############################################

def alternatingSum(L):   
    #creates alternating sum by subtracting and adding alternatively
    if L == []:
        #if empty list no alternating sum
        return 0
    elif len(L)%2==1:
        #if the length is odd the values are added
        return alternatingSum(L[:-1])+L[-1]
        #calls self and adds to last value
    elif len(L)%2==0:
        #if the length is even the values are subtracted
        return alternatingSum(L[:-1])-L[-1]
        #calls self and subtracts last value

def powersOf3ToN(n):
    #finds the positive powers of 3 equal to or below n
    if n<1:
        #when there are no powers of 3 below the value of n
        return None
    elif n<3:
        #when 1 is the only power of 3 below the value of n
        return [1]
    return powersOf3ToN(n/3)+[3**int(math.log(n,3)+0.0000001)]
    #gets the largest power of 3 that is less than n and adds it to the end
    #then calls it again
    

def binarySearchValues(L, v):
    #recursively searches for the value v in L
    if not isinstance(v,list):
        #if v has not been converted to a list yet
        return binarySearchValues(L, [v,0,len(L)-1])
        #v is changed to a list and calls the function again
    else:
        if v[2] < 0 or v[1] < 0:
            #base case for recursion
            return []
        indx = int((v[2]+v[1]) // 2)
        #finds the index value by integer dividing 0 and total length-1
        if v[2]-v[1]==0 or L[indx] == v[0]: 
            #if it finds the correct value on the first try/base case
            return[(indx,L[indx])]
        if L[indx] < v[0]:
            #if the data is in the top half of the list
            return [(indx,L[indx])]+binarySearchValues(L, [v[0],indx+1,v[2]])
        else:
            #if the data is in the bottom half of the list
            return [(indx,L[indx])]+binarySearchValues(L, [v[0],v[1],indx-1])
        

##############################################
# OOP questions
##############################################

class Book(object):
    #class that uses OOP for use in looking at different aspects of books
    def __init__(self,book,author,nbrPage):
        #initializes the variables that are necessary
        self.book = book
        self.author = author
        self.nbrPage = nbrPage
        self.currPage = 1
        self.bookMark = None
    def __repr__(self):
        #creates the string values for the books
        if self.nbrPage==1 or self.nbrPage==0:
            #if book is 0 or 1 page long
            return "Book<"+str(self.book)+" by "+str(self.author)+": "\
            +str(self.nbrPage)+" page,"+ " currently on page "\
            +str(self.currPage)+">"
        elif self.bookMark!=None:
            #when there is a bookmark the bookmarked page is displayed
            return "Book<"+str(self.book)+" by "+str(self.author)+": "\
            +str(self.nbrPage)+" pages,"+ " currently on page "\
            +str(self.currPage)+", page "+str(self.bookMark)+ " bookmarked>"
        else:
            #when there is no bookmarked page and the length is greater
            #than 1 page
            return "Book<"+str(self.book)+" by "+str(self.author)+": "\
            +str(self.nbrPage)+" pages,"+ " currently on page "\
            +str(self.currPage)+">"
    def turnPage(self,pageTurn):
        #changes the current page of the book
        self.currPage+=pageTurn
        if self.currPage<1:
            #does not allow the currPage to be less than 1
            self.currPage = 1
        if self.currPage>self.nbrPage:
            #does not allow the currPage to be greater than the number of pages
            self.currPage = self.nbrPage
    def getCurrentPage(self):
        #returns what the current page is
        return self.currPage
    def getBookmarkedPage(self):
        #returns what the current bookmarked page is
        return self.bookMark
    def placeBookmark(self):
        #sets the current bookmark
        self.bookMark = self.currPage
    def turnToBookmark(self):
        #changes the current page to where the current bookmark is
        if self.bookMark!=None:
            self.currPage = self.bookMark
    def removeBookmark(self):
        #removes the bookmark and sets it back to None
        self.bookMark=None
    def __eq__(self, other):
        #checks that the books are equal in every way
        #(title,author,number of pages,current pages, and bookmark values)
        return (self.book == other.book and self.author==other.author\
        and self.nbrPage==other.nbrPage and self.currPage==other.currPage\
        and self.bookMark==other.bookMark)
    

#################################################
# Test Functions
#################################################

def testAlternatingSum():
    print('Testing alternatingSum()...', end='')
    assert(alternatingSum([ ]) == 0)
    assert(alternatingSum([1]) == 1)
    assert(alternatingSum([1, 5]) == 1-5)
    assert(alternatingSum([1, 5, 17]) == 1-5+17)
    assert(alternatingSum([1, 5, 17, 4]) == 1-5+17-4)
    print('Done!')

def testPowersOf3ToN():
    print('Testing powersOf3ToN()...', end='')
    assert(powersOf3ToN(-42) == None)
    assert(powersOf3ToN(0.99) == None)
    assert(powersOf3ToN(1) == [1])
    assert(powersOf3ToN(3) == [1, 3])
    assert(powersOf3ToN(8.9999) == [1, 3])
    assert(powersOf3ToN(9) == [1, 3, 9])
    assert(powersOf3ToN(9.1111) == [1, 3, 9])
    assert(powersOf3ToN(2187) == [1, 3, 9, 27, 81, 243, 729, 2187])
    
    print('Done!')

def testBinarySearchValues():
    print('Testing binarySearchValues()...', end='')
    L = ['a', 'c', 'f', 'g', 'm', 'q']
    assert(binarySearchValues(L, 'a') == [(2,'f'), (0,'a')])
    assert(binarySearchValues(L, 'c') == [(2,'f'), (0,'a'), (1,'c')])
    assert(binarySearchValues(L, 'f') == [(2,'f')])
    assert(binarySearchValues(L, 'g') == [(2,'f'), (4, 'm'), (3, 'g')])
    assert(binarySearchValues(L, 'm') == [(2,'f'), (4, 'm')])
    assert(binarySearchValues(L, 'q') == [(2,'f'), (4, 'm'), (5, 'q')])
    assert(binarySearchValues(L, 'z') == [(2,'f'), (4, 'm'), (5, 'q')])
    assert(binarySearchValues(L, 'b') == [(2,'f'), (0,'a'), (1,'c')])
    print('Done!')

def testBookClass():
    print("Testing Book class...", end="")
    # A Book has a title, and author, and a number of pages.
    # It also has a current page, which always starts at 1. There is no page 0!
    book1 = Book("Harry Potter and the Sorcerer's Stone", 
                 "J. K. Rowling", 309)
    assert(str(book1) == "Book<Harry Potter and the Sorcerer's Stone by " + 
                         "J. K. Rowling: 309 pages, currently on page 1>")
    book2 = Book("Carnegie Mellon Motto", "Andrew Carnegie", 1)
    assert(str(book2) == "Book<Carnegie Mellon Motto by Andrew Carnegie: " +
                         "1 page, currently on page 1>")
                         
    # You can turn pages in a book. Turning a positive number of pages moves
    # forward; turning a negative number moves backwards. You can't move past
    # the first page going backwards or the last page going forwards
    book1.turnPage(4) # turning pages does not return
    assert(book1.getCurrentPage() == 5)
    book1.turnPage(-1)
    assert(book1.getCurrentPage() == 4)
    book1.turnPage(400)
    assert(book1.getCurrentPage() == 309)
    assert(str(book1) == "Book<Harry Potter and the Sorcerer's Stone by " + 
                         "J. K. Rowling: 309 pages, currently on page 309>")
    book2.turnPage(-1)
    assert(book2.getCurrentPage() == 1)
    book2.turnPage(1)
    assert(book2.getCurrentPage() == 1)
    
    # You can also put a bookmark on the current page. This lets you turn
    # back to it easily. The book starts out without a bookmark.
    book3 = Book("The Name of the Wind", "Patrick Rothfuss", 662)
    assert(str(book3) == "Book<The Name of the Wind by Patrick Rothfuss: " + \
                         "662 pages, currently on page 1>")
    assert(book3.getBookmarkedPage() == None)
    book3.turnPage(9)
    book3.placeBookmark() # does not return
    assert(book3.getBookmarkedPage() == 10)
    book3.turnPage(7)
    assert(book3.getBookmarkedPage() == 10)
    assert(book3.getCurrentPage() == 17)
    assert(str(book3) == "Book<The Name of the Wind by Patrick Rothfuss: " + \
                         "662 pages, currently on page 17, page 10 bookmarked>")
    book3.turnToBookmark()
    assert(book3.getCurrentPage() == 10)
    book3.removeBookmark()
    assert(book3.getBookmarkedPage() == None)
    book3.turnPage(25)
    assert(book3.getCurrentPage() == 35)
    book3.turnToBookmark() # if there's no bookmark, don't turn to a page
    assert(book3.getCurrentPage() == 35)
    assert(str(book3) == "Book<The Name of the Wind by Patrick Rothfuss: " + \
                         "662 pages, currently on page 35>")
    
    # Finally, you should be able to compare two books directly
    book5 = Book("A Game of Thrones", "George R.R. Martin", 807)
    book6 = Book("A Game of Thrones", "George R.R. Martin", 807)
    book7 = Book("A Natural History of Dragons", "Marie Brennan", 334)
    book8 = Book("A Game of Spoofs", "George R.R. Martin", 807)
    assert(book5 == book6)
    assert(book5 != book7)
    assert(book5 != book8)
    book5.turnPage(1)
    assert(book5 != book6)
    book5.turnPage(-1)
    assert(book5 == book6)
    book6.placeBookmark()
    assert(book5 != book6)
    print("Done!")

##############################################
# testAll and main
##############################################

def testAll():
    testAlternatingSum()
    testPowersOf3ToN()
    #testBinarySearchValues()
    testBookClass()

def main():
    cs112_f17_week9_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
