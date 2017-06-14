#lab02.py by Kenneth Toombs for CS8 lab02, 10/21/2013
#Some Example Python Functions

# Next define a function for the perimeter of a rectangle
#  consumes: length, width
#  produces: perimeter of the rectangle
#  THIS ONE SHOULD PASS ITS TESTS ALREADY.  IT IS HERE AS AN EXAMPLE

def perimRect(length,width):
   """
   Compute perimiter of rectangle
   >>> perimRect(2,3)
   10
   >>> perimRect(4, 2.5)
   13.0
   >>> perimRect(3, 3)
   12
   >>> perimRect(8,4)
   24
   """
   return 2 * length + 2 * width


# Next define a function to convert Fahrenheit to Celsius
#  consumes: temperature in Fahrenheit
#  produces: temperature in Celsius

def FtoC(fTemp):
    """
    Convert Fahrenheit to Celsius
    >>> FtoC(212)
    100.0
    >>> FtoC(32)
    0.0
    >>> FtoC(68)
    20.0
    """
    return (fTemp - 32.0) * (5.0/9.0)

# Next, here are some test cases for FtoC. 
    
    """
    >>> FtoC(-40)
    -40.0
    """


# Next define a function for the area of a rectangle
#  consumes: length, width
#  produces: area of the rectangle

def areaRect(length,width):
   """
   compute area of rectangle
   >>> areaRect(2,3)
   6
   >>> areaRect(4, 2.5)
   10.0
   >>> areaRect(3,3)
   9
   >>> areaRect(5,5)
   25
   """
   return length * width

# Next, define a function to convert Celsius to Fahrenheit
#  consumes: temperature in Celsius (call the parameter cTemp )
#  produces: temperature in Fahrenheit (this is what you return) 

def CtoF(cTemp):
    """
    Convert Celsius to Farenheit
    >>> CtoF(100)
    212.0
    >>> CtoF(0)
    32.0
    >>> CtoF(20)
    68.0
    >>> CtoF(-40)
    -40.0
    
    """

  

    return cTemp * (9/5) + 32




import doctest
doctest.testmod(verbose=True)
