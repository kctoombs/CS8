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
    t.forward(10)
    t.down()


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
    t.forward(45)
    t.down()

    #Now to draw letter L
    startX=t.xcor()
    startY=t.ycor()

    #Draw the left side
    sideLX = startX
    sideLY = startY + h
    t.goto(sideLX, sideLY)
    t.goto(startX, startY)

   #Draw the bottom
    bottomLX = startX + w
    bottomLY = startY
    t.goto(bottomLX, bottomLY)

    #move turtle to the next space / area
    t.up()
    t.forward(10)
    t.down()

    #Draw G
    startX=t.xcor()
    startY=t.ycor()

    #Draw top part
    topGX = startX+w
    topGY = startY+h
    t.up()
    t.goto(topGX, topGY)
    t.down()

    #Draw left side
    topLeftGX = startX
    topLeftGY = startY + h
    t.goto(topLeftGX, topLeftGY)

    #To draw to bottom left point
    bottomGX = startX
    bottomGY = startY
    t.goto(bottomGX, bottomGY)
    
    #Draw bottom line
    bottomRightGX = startX + w
    bottomRightGY = startY
    t.goto(bottomRightGX, bottomRightGY)

    #Go to center of left side to begin curl
    middleRightGX = startX + w
    middleRightGY = startY + (h/2)
    t.goto(middleRightGX, middleRightGY)
    
    #Draw mid-section of G
    middleGX = startX + (w/2)
    middleGY = startY + (h/2)
    t.goto(middleGX, middleGY)
    
def go():
	t=turtle.Turtle()
	drawK(t,70,80)
    
