# lab03.py by Kenneth Toombs for CS8 lab03, 10/23/2013
# Python Predicate, String, and List functions

def isList(x):
   """
   returns True if argument is of type list, otherwise False

   >>> isList(3)
   False
   >>> isList([3])
   True
   >>> isList([5,10,15,20])
   True
   >>> isList("foo")
   False
   >>> isList(["John","Paul","Ringo","George"])
   True
   >>> isList([])
   True
   >>>
   """
   
   return ( type(x) == list )   # True if the type of x is a list




def isString(x):
    """"
    >>> isString(4)
    False
    >>> isString([1,2])
    False
    >>> isString("")
    True
    >>> isString("Dude")
    True
    >>>

    """
    
    return ( type(x) == str )
    

# The following function is provided for you as an example
# of how to write a Python function involving "or"
# This contains HINTS as to how to do the next function definition.


def isAdditivePrimaryColor(color):
    """
    return True if color is a string equal to "red", "green" or "blue", otherwise False
    >>> isAdditivePrimaryColor("blue")
    True
    >>> isAdditivePrimaryColor("black")
    False
    >>> isAdditivePrimaryColor(42)
    False
    >>>
    """
    
    return ( (color == "red" ) or (color == "green" ) or (color == "blue") )

# NOTE: the following will NOT work for isAdditivePrimaryColor:
#
# def isAdditivePrimaryColor(color):
#   return ( color == "red" or "green" or "blue" )
#
# Try it, and convince yourself that it doesn't work.
# Does it fail to compile, fail to run (python vomit), or just give the
#  wrong answer?    You may be surprised!
# Try it, then try to understand _why_ this doesn't do what you want
# Hints: 'or' is an operator, and it must take operands that are
# either True or False
# (color == "red") is either True or False.  What about the other operands?


def isSimpleNumeric(x):
   """
   returns True if x is has type int or float; anything else, False 
   >>> isSimpleNumeric(5)
   True
   >>> isSimpleNumeric(3.5)
   True
   >>> isSimpleNumeric("5")
   False
   >>> isSimpleNumeric([5])
   False
   >>> isSimpleNumeric(6.0221415E23)
   True
   >>>
   """
   
   return ((type(x) == int) or (type(x) == float)) # True if type of x is an integer or floating point number
  


def notStringContainingE(word):
   """
   return True when word is a string that contains no letter 'e' (or 'E')
   It should work both for lower and upper case.
   When word isn't a string, return True (because it is not a string contaning an E)

   >>> notStringContainingE('Fred')    
   False
   >>> notStringContainingE('Jane')
   False
   >>> notStringContainingE('Santa')
   True
   >>> notStringContainingE('Barbara')
   True
   >>> notStringContainingE('Edward')
   False
   >>> notStringContainingE('Ice Cream')
   False
   >>> notStringContainingE(23)
   True
   >>> notStringContainingE(['e'])
   True
   >>>
   """

   if not(type(word)==str):
      return True
   for letter in word:
     if (letter == 'e' or letter == 'E'):   
       return False
   return True


#@@@ Here is a function definition that doesn't pass one or more of its tests.
#@@@ Fix it!  (Also try to understand why it is wrong)

def hasNoX(word):
   """
   return True when word is a string that contains no letter 'x' (and no letter 'X')
   It should work both for lower and upper case.
   When word isn't a string, return True (because it is not a string with an  x in that case!)

   >>> hasNoX('Fred')
   True
   >>> hasNoX('Xerox')
   False
   >>> hasNoX('Box')
   False
   >>> hasNoX('Xbox')
   False
   >>> hasNoX(23)
   True
   >>> hasNoX(['x'])
   True
   >>> hasNoX('x')
   False
   >>>


   """
   if (type(word)!=str):
      return True

   for letter in word:
     if (letter == 'x' or letter == 'X'):
       return False
   
   return True


# The following function is provided for you as an example
# of how to write a Python function that checks if EVERY element
# of a list has some property.


def isListOfSimpleNumeric(theList):
   """
   indicates whether value of argument is a list of only simple numerics (int or float)
   Note: empty list should return True---it doesn't contain anything that ISN'T simple numeric
   theList can be anything, and it will return either True or False.

   >>> isListOfSimpleNumeric('Fred')
   False
   >>> isListOfSimpleNumeric(3)
   False
   >>> isListOfSimpleNumeric([3])
   True
   >>> isListOfSimpleNumeric([3.4])
   True
   >>> isListOfSimpleNumeric([2,3,4,5.6,7])
   True
   >>> isListOfSimpleNumeric([2,3,'oops',5])
   False
   >>> isListOfSimpleNumeric([2,3,[4]])
   False
   >>> isListOfSimpleNumeric([])
   True  
   """
   if (not isList(theList)):
      return False  # it isn't really a list!

   # Now we can assume that theList really is a list
   # But is it a list of all numerics?
   # If we find even a single item that isn't numeric, we can
   # immediately return false.  
   
   for item in theList:
     if not isSimpleNumeric(item):
       return False

   # If we get here and didn't return yet, then we know everything
   # in the list is a simple numeric!
   # (i.e. there isn't anything in the list that is NOT simple numeric)
   
   return True




def isListOfIntegers(theList):
   """
   indicates whether value of argument is a list of only int 
   Note: empty list should return True---it doesn't contain anything that ISN'T int
   theList can be anything, and it will return either True or False.

   >>> isListOfIntegers('Fred')
   False
   >>> isListOfIntegers(3)
   False
   >>> isListOfIntegers([3])
   True
   >>> isListOfIntegers([3.4])
   False
   >>> isListOfIntegers([2,3,4,5.6,7])
   False
   >>> isListOfIntegers([2,3,'oops',5])
   False
   >>> isListOfIntegers([2,3,4,5,6,7])
   True
   >>> isListOfIntegers([2,3,[4]])
   False
   >>> isListOfIntegers([])
   True
   
   """
   if type(theList) != list:
      return False

   if theList == []:
      return True

   for i in (theList):
      if type(i) != int :
         return False

   return True
   

   



def isListOfEvenIntegers(theList):
   """
   indicates whether value of argument is a list of only even integers
   Note: empty list should return True---it doesn't contain anything that ISN'T an even integer
   theList can be anything, and it will return either True or False.

   >>> isListOfEvenIntegers('Fred')
   False
   >>> isListOfEvenIntegers(3)
   False
   >>> isListOfEvenIntegers([3])
   False
   >>> isListOfEvenIntegers([4])
   True
   >>> isListOfEvenIntegers([3.4])
   False
   >>> isListOfEvenIntegers([2,3,4,5.6,7])
   False
   >>> isListOfEvenIntegers([2,3,'oops',5])
   False
   >>> isListOfEvenIntegers([2,3,4,5,6,7])
   False
   >>> isListOfEvenIntegers([2,4,6])
   True
   >>> isListOfEvenIntegers([2,3,[4]])
   False
   >>> isListOfIntegers([])
   True
   >>>
   
   """
   if type(theList) != list:
      return False

   for i in theList:
      if type(i) != int or (i%2) !=0:
         return False
      
   return True


    



def totalLength(listOfStrings):
    """
    returns total length of all the strings in a list of strings, False if argument not a list, 0 for empty list
    >>> totalLength('1')
    False
    >>> totalLength(['a','b'])
    2
    >>> totalLength([])
    0
    >>> totalLength(['Go','Gauchos'])
    9
    >>> totalLength(['x','xxx','xxxx'])
    8
    """
    acc = 0 
    if type(listOfStrings) != list:
       return False

    for item in listOfStrings:
      if type(item) != str:
          return False
         
      acc = acc +len(item) 
      
    return acc

    



def lengthOfEach(listOfStrings):
    """
    given list of strings, returns list of ints correponding to length of each string, otherwise False.

    empty list yields empty list.

    >>> lengthOfEach('1')
    False
    >>> lengthOfEach(['a','b'])
    [1, 1]
    >>> lengthOfEach([])
    []
    >>> lengthOfEach(['Go','Gauchos'])
    [2, 7]
    >>> lengthOfEach(['x','xxx','xxxx'])
    [1, 3, 4]
    >>>
    
    
    """
    acc = []
    
    if type(listOfStrings) != list:
       return False

    for item in listOfStrings:
       if type(item) != str:
          return False  

       acc = acc + [len(item)]    

    return acc
    




def countEvens(listOfInts):
    """
    given a list of ints, counts even ints in list.  Otherwise, returns False.
 
    yields 0 for empty list, or list of ints with no evens in it.


    >>> countEvens('1')
    False
    >>> countEvens(['a','b'])
    False
    >>> countEvens([])
    0
    >>> countEvens([1,2,3,4,5])
    2
    >>> countEvens([1])
    0
    >>> countEvens([3,2])
    1
    >>> countEvens([2,3,4])
    2
    >>>
    
    """
    acc = 0
    
    if type(listOfInts) != list:
       return False

    for i in listOfInts:
       if type(i) != int:
          return False
       if i%2 == 0: 
          acc = acc + 1

    return acc


### @@@ NOW, write a function called onlyEvens
### @@@ Use the accumulator pattern, starting with an empty list.
### @@@   Use a for loop to traverse the list—each time you find an item
### @@@     if it isn't an int, return False---otherwise, if it is even, add
### @@@     it to your accumulated list.


def onlyEvens(listOfInts):
    """
    given a list of ints, return new list with only the even ones.  Otherwise, return false.

    empty list yields empty list

    >>> onlyEvens('1')
    False
    >>> onlyEvens(['a','b'])
    False
    >>> onlyEvens([])
    []
    >>> onlyEvens([1,2,3,4,5])
    [2, 4]
    >>> onlyEvens([1])
    []
    >>> onlyEvens([1,3])
    []
    >>> onlyEvens([3,2])
    [2]
    >>> onlyEvens([2,3,4])
    [2, 4]
    >>>



    """
    acc = []

    if type(listOfInts) != list:
       return False

    for i in listOfInts:
       if type(i) != int:
          return False

       if i%2 == 0:
          acc = acc + [i]

    return acc     


    
    

import doctest
doctest.testmod(verbose=True)


### @@@ To test a single function, comment out the doctest.testmod(verbose=True) line above,
### @@@ by putting a single # in front of it

### @@@ Then uncomment one of the following lines.    For functions other than isList, isString, and 
### @@@ isAdditivePrimaryColor, copy/paste one of these lines and substitute
### @@@ in the name of the function you want to focus on

#doctest.run_docstring_examples(isList, globals(), verbose=True)
#doctest.run_docstring_examples(isString, globals(), verbose=True)
#doctest.run_docstring_examples(isAdditivePrimaryColor, globals(), verbose
#doctest.run_docstring_examples(isSimpleNumeric, globals(), verbose=True)
#doctest.run_docstring_examples(notStringContainingE, globals(), verbose=True)
#doctest.run_docstring_examples(hasNoX, globals(), verbose=True)
#doctest.run_docstring_examples(isListOfIntegers, globals(), verbose=True)
#doctest.run_docstring_examples(isListOfEvenIntegers, globals(), verbose=True)
#doctest.run_docstring_examples(totalLength, globals(), verbose=True)
#doctest.run_docstring_examples(lengthOfEach, globals(), verbose=True)
#doctest.run_docstring_examples(countEvens, globals(), verbose=True)
#doctest.run_docstring_examples(onlyEvens, globals(), verbose=True)
