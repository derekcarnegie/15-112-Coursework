# events-example0.py
# Barebones timer, mouse, and keyboard events
#Derek Li (derekl1) Phil Johnson (phjohnso)

from tkinter import *
import cs112_f17_week6_linter
import random
import copy
####################################
# customize these functions
####################################

def init(data):
    # load data.xyz as appropriate
    data.rows=15
    data.cols=10
    data.cellSize = 20
    data.emptyColor = "blue"
    data.margin = 10
    data.board =[[data.emptyColor]*data.cols for row in range(data.rows)]
    
    # pre-load a few cells with known colors for testing purposes
    data.board[0][0] = "red" # top-left is red
    data.board[0][data.cols-1] = "white" # top-right is white
    data.board[data.rows-1][0] = "green" # bottom-left is green
    data.board[data.rows-1][data.cols-1] = "gray" # bottom-right is gray
 
 # Seven "standard" pieces (tetrominoes)
    iPiece = [
        [  True,  True,  True,  True ]
    ]

    jPiece = [
        [  True, False, False ],
        [  True,  True,  True ]
    ]

    lPiece = [
        [ False, False,  True ],
        [  True,  True,  True ]
    ]

    oPiece = [
        [  True,  True ],
        [  True,  True ]
    ]

    sPiece = [
        [ False,  True,  True ],
        [  True,  True, False ]
    ]

    tPiece = [
        [ False,  True, False ],
        [  True,  True,  True ]
    ]

    zPiece = [
        [  True,  True, False ],
        [ False,  True,  True ]
    ]
    tetrisPieces = [ iPiece, jPiece, lPiece, oPiece, sPiece, tPiece, zPiece ]
    tetrisPieceColors = [ "red", "yellow", "magenta", "pink", "cyan", "green", 
    "orange" ]
    data.tetrisPieces = tetrisPieces
    data.tetrisPieceColors = tetrisPieceColors
    data.initialPiece = newFallingPiece(data)
    #allows for these parameters to be accessed elsewhere
    
def newFallingPiece(data):
    #randomly decides which pieces are created and puts them at the top of
    #the screen
    randomIndex = random.randint(0, len(data.tetrisPieces) - 1)
    data.fallingPiece = data.tetrisPieces[randomIndex]
    data.currColor = data.tetrisPieceColors[randomIndex]
    #randomly decides piece and color of piece
    data.fallingPieceRow = 0
    #always starts at row 0
    data.fallingPieceCols = len(data.fallingPiece[0])
    data.fallingPieceCol = data.cols//2 - data.fallingPieceCols//2
    #determines location so that the piece is centered
    return None

def drawFallingPiece(canvas,data):
    #iterates through the elements of each list for each piece to draw
    #the cells
    for row in range(len(data.fallingPiece)):
        for col in range(len(data.fallingPiece[0])):
            if data.fallingPiece[row][col]==True:
                #only works if the boolean value of the list is true
                drawCell(canvas,data,data.fallingPieceRow+row,
                data.fallingPieceCol+col,data.currColor)

def mousePressed(event, data):
    pass

def keyPressed(event, data):
    #takes key presses to perform certain actions
    if event.keysym=="Left":
        moveFallingPiece(data,0,-1)
    if event.keysym=="Right":
        moveFallingPiece(data,0,+1)
    if event.keysym=="Up":
        rotateFallingPiece(data)
    if event.keysym=="Down":
        moveFallingPiece(data, +1, 0)
    if event.keysym == "p":
        newFallingPiece(data)
        
def rotateFallingPiece(data):
    #rotates the falling piece by altering the list
    origFallingPiece = copy.deepcopy(data.fallingPiece) 
    #need copy to double check legality after piece is rotated
    newFallingPiece = []
    for col in range(len(data.fallingPiece[0])):
        newRow = []
        for row in range(len(data.fallingPiece)):
            newRow+=[data.fallingPiece[row][len(data.fallingPiece[0])-col-1]]
            #uses the last col to get the first row
        newFallingPiece.append(newRow)
        #rows of rotated block are added to new list
    data.fallingPiece=newFallingPiece
    if fallingPieceIsLegal(data)==False:
        #checks legality of rotation
        data.fallingPiece = origFallingPiece
        #if the piece is not legal set back to original value
    pass
    
    
        

def moveFallingPiece(data,drow,dcol):
    #alters the position of each piece
    data.fallingPieceCol+=dcol
    data.fallingPieceRow+=drow
    #changes the column and row index
    if fallingPieceIsLegal(data)==False:
        data.fallingPieceCol-=dcol
        data.fallingPieceRow-=drow
        #if not legal the values are reverted
    pass
        
def fallingPieceIsLegal(data):
    #checks that the piece does not go off the board
    for row in range(len(data.fallingPiece)):
        for col in range(len(data.fallingPiece[0])):
            row1=data.fallingPieceRow+row
            col1=data.fallingPieceCol+col
            if row1<0 or row1>=data.rows:return False
            if col1<0 or col1>=data.cols:return False
            #both check if the values are within the board
            if data.board[row1][col1] != data.emptyColor \
            and data.fallingPiece[row][col]==True:
                #makes sure that the values that are being drawn are
                return False
    return True
            

def playTetris():
    #sets parameters for board
    cols = 10
    rows = 15
    cellSize = 20
    margin = 10
    width = (cols*cellSize)+2*margin
    height = (rows*cellSize)+2*margin
    run(width,height)
    
    
def drawCell(canvas,data,row,col,currentColor):
    #draws individual blocks on board
    x1 = data.margin+data.cellSize*col
    x2 = data.margin+data.cellSize*(col+1)
    y1 = data.margin+data.cellSize*row
    y2 = data.margin+data.cellSize*(row+1)
    #finds coordinate values of each cell
    canvas.create_rectangle(x1,y1,x2,y2,fill = currentColor, width = 3)

def drawBoard(canvas,data):
    #creates the cells for each row and column
    for row in range(data.rows):
        for col in range(data.cols):
            currentColor = data.board[row][col]
            #finds the color that needs to be sent
            drawCell(canvas,data,row,col,currentColor)
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    #calls all the helper functions to create the board and game
    canvas.create_rectangle(0,0,data.width,data.height,fill = "orange")
    drawBoard(canvas,data)
    data.initialPiece
    drawFallingPiece(canvas,data)
    pass

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

playTetris()