#lab01.py for Kenneth Toombs and Liliana Gallegos
#CS8, Fall 2013, Prof. Conrad
#Draw some initials using turtle graphics

import turtle
t=turtle.Turtle()

def drawK(t, w, h):
    """
draw the letter K using t, with some width and height
    """

    #Find my starting point
    startX = t.xcor()
    startY = t.ycor()


    #Draw the left side
    sideKX = startX
    sideKY = startY + h
    t.goto(sideKX, sideKY)
	
	
    #Arrive to mid point
    middleKX = startX
    middleKY = startY + (h/2)
    t.goto(middleKX, middleKY)
	
    #Top line on right
    topRightKX = startX + w
    topRightKY = startY + h
    t.goto(topRightKX, topRightKY)
	
    #back to the middle
    t.goto(middleKX, middleKY)
	
    #Draw bottom right leg
    bottomRightKX = startX + w
    bottomRightKY = startY
    t.goto(bottomRightKX, bottomRightKY)
	
    #Make space for next letter
    t.up()
    t.forward(w/2)
    t.down()

def drawT(t, w, h):
    """
Draw the letter T using t, with some width and height
    """
    
    #Start Drawing T
    startX = t.xcor()
    startY = t.ycor()

    #From top left point
    topLeftTX=startX
    topLeftTY=startY + h
    
    #Move turtle to next starting point
    t.up()
    t.goto(topLeftTX, topLeftTY)
    t.down()

    #Draw top line of T
    topRightTX=startX + w
    topRightTY=startY + h
    t.goto(topRightTX, topRightTY)

    #Preparing to draw middle line
    middleTX = startX + (w/2)
    middleTY = startY + h
    t.goto(middleTX, middleTY)

    #draw down
    bottomTX = startX + (w/2)
    bottomTY = startY
    t.goto(bottomTX, bottomTY)

    #move turtle to the next space / area
    t.up()
    t.forward(w)
    t.down()

def drawL(t, w, h):
    """
Draw the letter L using t, with some width and height
    """

    #Now to draw letter L
    startX=t.xcor()
    startY=t.ycor()

    #Draw the left side
    sideLX = startX
    sideLY = startY + w
    t.goto(sideLX, sideLY)
    t.goto(startX, startY)

   #Draw the bottom
    bottomLX = startX + h
    bottomLY = startY
    t.goto(bottomLX, bottomLY)

    #move turtle to the next space / area
    t.up()
    t.forward(w/2)
    t.down()

def drawG(t, w, h):
    """
Draw the letter G using t, with some width and height
    """


    #Draw G
    startX=t.xcor()
    startY=t.ycor()

    #Draw top part
    topGX = startX+h
    topGY = startY+w
    t.up()
    t.goto(topGX, topGY)
    t.down()

    #Draw left side
    topLeftGX = startX
    topLeftGY = startY + w
    t.goto(topLeftGX, topLeftGY)

    #To draw to bottom left point
    bottomGX = startX
    bottomGY = startY
    t.goto(bottomGX, bottomGY)
    
    #Draw bottom line
    bottomRightGX = startX + h
    bottomRightGY = startY
    t.goto(bottomRightGX, bottomRightGY)

    #Go to center of left side to begin curl
    middleRightGX = startX + h
    middleRightGY = startY + (w/2)
    t.goto(middleRightGX, middleRightGY)
    
    #Draw mid-section of G
    middleGX = startX + (h/2)
    middleGY = startY + (w/2)
    t.goto(middleGX, middleGY)
    t.goto(middleRightGX, middleRightGY)
    t.goto(bottomRightGX, bottomRightGY)
    
    
def go():

    """
Draw K,T,L, and G at the same time by incorporating all functions into one big function
    """
	t=turtle.Turtle()
	drawK(t,70,80)

def drawKTLG(t, w, h):

    #Draw the K
    drawK(t, w, h)

    #Draw the T
    drawT(t, w, h)

    #Draw the L
    drawL(t, h, w)

    #Draw the G
    drawG(t, h, w)

def drawKT(t, w, h):

    #Draw the K
    drawK(t, w, h)

    #Draw the T
    drawT(t, w, h)

def drawLG(t, w, h):

    #Draw the L
    drawL(t, h, w)

    #Draw the G
    drawG(t, h, w)
    
