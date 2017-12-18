#Derek Li (derekl1)

import cs112_f17_week5_linter
from tkinter import *
from sudoku import *
import copy
#########################################################
# Customize these functions
# You will need to write many many helper functions, too.
#########################################################

        

def init(data):
    #initializes data values that are needed in later helper functions
    data.highlightedRow = 0
    data.highlightedColumn = 0
    data.Squares=9
    data.permBoard = copy.deepcopy(data.board)
    #so permBoard is not an alias of board

def drawNumbers(canvas,data):
    #draws the numbers that are in board list
    for i in range(data.Squares):
        for k in range(data.Squares):
            if data.board[i][k]==0:
                continue
                #ensures that 0 is not put into the board
            canvas.create_text(((k)*(data.width/9))+30,
            i*data.height/9+25,
            text=str(data.board[i][k]),font = ("Times New Roman",25,"bold"))
    for j in range(data.Squares):
        for l in range(data.Squares):
            if data.permBoard[j][l]==0:
                continue
                #ensures that 0 is not put into the board
            canvas.create_text(((l)*(data.width/9))+30,
            j*data.height/9+25,
            text=str(data.permBoard[j][l]),font = ("Times New Roman",
            25,"bold"),fill="blue")
            #creates intial blue text on top of entire board

def keyPressed(event, data):
    #accepts the key presses so that the pointer moves
    if not isFull(data):
        if event.keysym.isdigit():
            #for numbers that are entered into the spaces
            if data.board[data.highlightedRow][data.highlightedColumn]==0:
                tempBoard = copy.deepcopy(data.board)
                tempBoard[data.highlightedRow]\
                [data.highlightedColumn]=int(event.keysym)
                #creates a copy of the original board to check for legality
                if (isLegalSudoku(tempBoard)==True):
                    #checks the legality of the board
                    data.board[data.highlightedRow]\
                    [data.highlightedColumn]=int(event.keysym)
        if event.keysym == "BackSpace":
            if data.permBoard[data.highlightedRow][data.highlightedColumn]==0:
                if not data.board[data.highlightedRow]\
[data.highlightedColumn]==0:
                    data.board[data.highlightedRow][data.highlightedColumn]=0
                #ensures that the values that are backspaced were previously
                #entered and are not part of the permanent board
        if event.keysym == "Right": data.highlightedColumn+=1
        if event.keysym == "Left": data.highlightedColumn-=1
        if event.keysym == "Down":data.highlightedRow+=1
        if event.keysym == "Up":data.highlightedRow-=1
        #changes the location of the pointer block
        if data.highlightedColumn>=9:data.highlightedColumn=0
        if data.highlightedRow>=9:data.highlightedRow=0
        if data.highlightedColumn<0:data.highlightedColumn = 8
        if data.highlightedRow<0:data.highlightedRow=8
        #ensures wraparound
        
def drawBackground(canvas,data):
    #creates the rectangles and bolded lines
    for i in range(data.Squares+1):
        #9 squares but 10 lines
        for k in range(data.Squares+1):
            #9 squares but 10 lines
            canvas.create_rectangle(i*(data.width/9),
            i*(data.height/9),k*(data.width/9),k*(data.height/9))
            #creates the inital grid of squares
            canvas.create_rectangle((data.width/9)*(data.highlightedColumn),
            (data.height/9)*data.highlightedRow,
            (data.width/9)*(data.highlightedColumn+1),
            (data.height/9)*(data.highlightedRow+1),fill="yellow")
            #creates the square filled with yellow that moves by key presses
            if i%3==0:
                canvas.create_line(0,i*(data.height/9),
                data.width,i*(data.height/9), width = 3)
                canvas.create_line(i*(data.width/9),
                0,i*(data.width/9),data.height,width=3)
                #creates lines at every third squares
    canvas.create_line(0,0,data.width,0, width = 10)
    canvas.create_line(0,0,0,data.height, width = 10)
    canvas.create_line(data.width,0,data.width,data.height, width = 3)
    canvas.create_line(0,data.height,data.width,data.height,width=3)
    #creates border lines for the sudoku board   

def isFull(data):
    #checks to see if the board is full of values which
    #when full is what is used to determine a winner
    for row in range(data.Squares):
        for cols in range(data.Squares):
            if data.board[row][cols]==0:
                return False
    return True

def drawGameOver(canvas,data):
    #creates the game over/win screen 
    canvas.create_rectangle(data.width/4,data.height/4,
    data.width*3/4,data.height*3/4,fill="black")
    #centers the square in the middle of the sudoku board
    canvas.create_text(data.width/2,data.height/2,
    text = "You are a winner",
    fill = "blue",font = ("Times New Roman",24,"bold"))
    #text goes in the center of the square

def redrawAll(canvas, data):
    #calls all helper functions to display the full game
    drawBackground(canvas,data)
    drawNumbers(canvas,data)
    if isFull(data):
        #ensures that the board is full so that the game ends
        drawGameOver(canvas,data)

########################################
# Do not modify the playSudoku function.
########################################

def playSudoku(sudokuBoard, width=500, height=500):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.board = sudokuBoard

    # Initialize any other things you want to store in data
    init(data)

    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()

    # set up events
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))

    # Draw the initial screen
    redrawAll(canvas, data)

    # Start the event loop
    root.mainloop()  # blocks until window is closed
    print("bye!")

def main():
    cs112_f17_week5_linter.lint() # check style rules
    
    board = [
[1,2,3,4,5,6,7,8,9],
[5,0,8,1,3,9,6,2,4],
[4,9,6,8,7,2,1,5,3],
[9,5,2,3,8,1,4,6,7],
[6,4,1,2,9,7,8,3,5],
[3,8,7,5,6,4,0,9,1],
[7,1,9,6,2,3,5,4,8],
[8,6,4,9,1,5,3,7,2],
[2,3,5,7,4,8,9,1,6]
]
    playSudoku(board)

if __name__ == '__main__':
    main()
