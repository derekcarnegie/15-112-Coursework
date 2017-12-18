# events-example0.py
# Targets Game

from tkinter import *
import cs112_f17_week6_linter
import random
import math

####################################
# customize these functions
####################################

def init(data):
    #initializes struct variables
    data.width = 400
    data.height = 400
    data.startGame = "Targets Game!"
    data.startGameKey = "Press 'p' to play"
    data.initializeGame = False
    data.possibleRadius = [5,15,25]
    data.radius = data.possibleRadius[random.randint(0,2)]
    data.x1 = random.randint(0,data.width-data.radius*2)
    data.x2 = data.x1+data.radius
    data.y1 = random.randint(0,data.height-data.radius*2)
    data.y2 = data.y1+data.radius
    data.dx = 1
    data.dy = 1
    data.widthBtwnCircle = 2
    data.numConcentricCircles = 5
    data.time=0
    data.timeRemainingStart=20
    data.timeRemaining = 0
    data.timeBeforeStart = 0
    data.circleParameters = [data.x1,data.x2,data.y1,data.y2,data.radius]
    data.targetList=[]
    data.score = 0
    data.xScroll=0
    data.yScroll=0
    data.distance = 0
    
def mousePressed(event, data):
    #finds location of mouse presses
    # use event.x and event.y
    data.xPressed = event.x
    data.yPressed = event.y
    checkClickerLoc(data)

def distance(x1,y1,data):
    #checks distance between coordinates and mouse click
    data.distance = math.sqrt((data.xPressed-x1)**2+(data.yPressed-y1)**2)


def keyPressed(event, data):
    #controls how the key presses interact with the game
    if event.keysym == "p":
        data.timeBeforeStart = data.time//1000
        #saves the current time when the game is started
        data.initializeGame = True
    if not data.timeRemaining<=0 and data.initializeGame ==True:
        if event.keysym == "Up":
            data.yScroll-=data.height/10
        if event.keysym == "Down":
            data.yScroll+=data.height/10
        if event.keysym == "Right":
            data.xScroll+=data.width/10
        if event.keysym == "Left":
            data.xScroll-=data.width/10
        #controls the movement of the game window and ensures that 
        #the window only moves during gameplay
    if data.timeRemainingStart+data.timeBeforeStart-data.time//1000<=0 and \
    event.keysym == "s":
        #restarts game if s is pressed and resets variables
        data.timeBeforeStart = 0
        data.time = 0
        data.score = 0
        data.initializeGame = False
        del data.targetList[:]
        #empties contents of list with coordinates

def timerFired(data):
    #keeps track of the change in time
    data.time+=100
    if data.initializeGame == False:
        #only for start screen
        if data.x2 == data.width:
            data.dx = -1
        if data.y2 == data.height:
            data.dy = -1
        if data.x1 == 0:
            data.dx = 1
        if data.y1 == 0:
            data.dy = 1
        if data.time%10==0:
            data.x1+=data.dx
            data.x2+=data.dx
            data.y1+=data.dy
            data.y2+=data.dy
        #ensures that target bounces and changes directions when it
        #hits the side walls
            
def drawStartScreen(canvas,data):
    #draws the start screen
    canvas.create_text(data.width/2,data.height/4,
    text = (data.startGame),font = ("Times New Roman", 20))
    canvas.create_text(data.width/2,data.height*2/3,
    text = (data.startGameKey),font = ("Times New Roman", 20))
    drawBouncingTarget(canvas,data)
    
    
def drawBouncingTarget(canvas,data):
    #draws the bouncing target used on the start screen
    for i in range(data.numConcentricCircles):
        if i%2==1:
            canvas.create_oval(data.x1+data.widthBtwnCircle*i,
            data.y1+i*data.widthBtwnCircle,data.x2-i*data.widthBtwnCircle,
            data.y2-i*data.widthBtwnCircle,fill = "white",outline = "white")
            #builds white circle every other iteration
        if i%2==0:
            canvas.create_oval(data.x1+i*data.widthBtwnCircle,
            data.y1+i*data.widthBtwnCircle,data.x2-i*data.widthBtwnCircle,
            data.y2-i*data.widthBtwnCircle,fill = "red", outline="red")
            #builds red circle every other iteration
            

def newTargCoord(data):
    #finds the target coordinate for the game state
    radius = data.possibleRadius[random.randint(0,2)]
    diffRadius = radius/5
    x1 = random.randint(10, 2*data.width - 2*radius-10)
    y1= random.randint(10,2*data.height- 2*radius-10)
    if x1>10-data.xScroll-0.5*data.width and x1<2*data.width-data.xScroll+10 - 2*radius+0.5*data.height and \
    y1>10-data.yScroll-0.5*data.height and y1<2*data.height-data.yScroll- 2*data.radius+0.5*data.height: 
        #if the coordinates are within the window they are added to the list
        data.targetList.append([diffRadius,x1,y1])

def drawStationaryTarget(canvas,data):
    #draws targets that do not move in the game state
    for h in range(len(data.targetList)):
        diffRadius = data.targetList[h][0]
        x1 = data.targetList[h][1]
        y1 = data.targetList[h][2]
        diameter = diffRadius*10
        #gets coordinates from list with coord's from helper function
        for i in range(data.numConcentricCircles):
            #creates target
            if i%2==1:
                canvas.create_oval(x1+diffRadius*i-data.xScroll,
                y1+i*diffRadius-data.yScroll,x1-i*diffRadius+diameter-data.xScroll,
                y1+diameter-i*diffRadius-data.yScroll,fill = "white",outline = "white")
            if i%2==0:
                canvas.create_oval(x1+i*diffRadius-data.xScroll,
                y1+i*diffRadius-data.yScroll,x1-i*diffRadius-data.xScroll+diameter,
                y1-i*diffRadius-data.yScroll+diameter,fill = "red", outline="red")

def drawGameBoard(canvas,data):
    #creates game board that is 2 times the size of the initial window and 
    #creates it so that the window begins in the middle
    canvas.create_rectangle(-0.5*data.width-data.xScroll,-0.5*data.height-data.yScroll,
    1.5*data.width-data.xScroll,1.5*data.height-data.yScroll,width = 10)

def drawGameState(canvas,data):
    #calls helper functions and displays entire game state
    drawGameBoard(canvas,data)
    if data.time%500==0:
        newTargCoord(data)
        #creates a new target every 0.5 seconds
    drawStationaryTarget(canvas,data)
    canvas.create_text(data.width/10,data.height*19/20,
    text = ("Score "+ str(data.score)),font = ("Times New Roman", 20))
    data.timeRemaining = data.timeRemainingStart+data.timeBeforeStart-data.time//1000
    if data.score%5==0 and data.score!=0:
        data.timeRemaining+=1
        #adds time to the clock if the score is a multiple of 5 and not 0
    canvas.create_text(data.width/4.5,data.height/20,
    text = "Time Remaining %d" % data.timeRemaining,font = ("Times New Roman", 20))

def checkClickerLoc(data):
    #check's the location of the clicker
    for h in range(len(data.targetList)):
        radius = data.targetList[h][0]*5
        x1 = data.targetList[h][1]
        x1= x1-data.xScroll+radius
        #finds true position of the xCoordinate
        y1 = data.targetList[h][2]
        y1 = y1-data.yScroll+radius
        #finds true position of the yCoordinate
        if data.xPressed!=0 and data.yPressed!=0:
            distance(x1,y1,data)
            #finds the distance between the mouse click and the coordinates
        if (data.distance<int(radius)):
            #if the distance is within the radius a point is added to the score
            #and the target is deleted from the list
            data.score+=1
            del data.targetList[h]
            
    
def drawGameOver(canvas,data):
    #draws game over screen
    canvas.create_rectangle(0,0,data.width,data.height,fill = "red",)
    canvas.create_text(data.width/2,data.height/2,text = "Game Over",
    font = ("Times New Roman", 30),fill = "white")
    canvas.create_text(data.width/2,data.height*2/3,text = "Final Score: " + str(data.score),
    font = ("Times New Roman", 25),fill = "white")
    canvas.create_text(data.width/2,data.height*4/5,
    text = "Press 's' to start again ",
    font = ("Times New Roman", 25),fill = "white")

def redrawAll(canvas, data):
    #calls all previous helper functions
    if not data.initializeGame:
        drawStartScreen(canvas,data)
        #draws start screen if user has not initialized the game yet
    if data.initializeGame:
        drawGameState(canvas,data)
        #starts game after game has been initialized
    if data.timeRemaining<=0 and data.initializeGame ==True:
        drawGameOver(canvas,data)
        #ends the game when the time remaining goes to 0 and the game has been
        #initialized


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