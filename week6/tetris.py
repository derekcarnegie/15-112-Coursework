# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *

####################################
# customize these functions
####################################

def init(data):
    # load data.xyz as appropriate
    data.rows=15
    data.cols=10
    data.cellSize = 20
    data.emptyColor = "blue"
    board = []
    for row in range(data.rows):
        for col in range(data.cols):
            board +=[[data.emptyColor]*data.cols]
    data.board = board
    # pre-load a few cells with known colors for testing purposes
    data.board[0][0] = "red" # top-left is red
    data.board[0][data.cols-1] = "white" # top-right is white
    data.board[data.rows-1][0] = "green" # bottom-left is green
    data.board[data.rows-1][data.cols-1] = "gray" # bottom-right is gray
    
    
def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

# def run(width,height):
#     x1=(data.width-width)/2
#     x2=data.width-(data.width-width)/2
#     y1=(data.height-height)/2
#     y2=height-(data.height-height)/2
#     canvas.create_rectangle(x1,y1,x2,y2)

def playTetris():
    cols = 10
    rows = 15
    cellSize = 20
    width = (cols*cellSize)
    height = (rows*cellSize)
    run(cols*cellSize,rows*cellSize)
    
def drawCells(canvas,data,row,col):
    currentColor = data.board[row][col]
    #canvas.create_rectangle(

def drawBoard(canvas,data):
    for row in range(data.rows):
        for col in range(data.cols):
            drawCell(canvas,data,row,col)
    
            

def timerFired(data):
    pass

def redrawAll(canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height,fill = "orange")
    playTetris()
    

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

run(400, 200)