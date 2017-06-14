# lab05.py by Kenneth Toombs for CS8 lab05, 11/06/2013
# Reading from files in Python

from collections import namedtuple
Student = namedtuple("Student","fName lName major") 

def lineToStudent(inputLine):
   """
   creates a Student (named tuple) from an inputLine (string)
   >>> lineToStudent('SHARON, ROBINSON, PHYSICS')
   Student(fName='SHARON', lName='ROBINSON', major='PHYSICS')
   >>> 
   """

   itemStripped = inputLine.strip()  # remove the newlines
   itemSplit = itemStripped.split(',')  # split into a list at the comma

   # now, itemSplit[0] is the first name,
   #      itemSplit[1] is the last name
   #      itemSplit[2] is the major
   # but each might still have spaces
  
   return Student(itemSplit[0].strip(), itemSplit[1].strip(), itemSplit[2].strip())

infile = open('students.txt', 'r')
inputList = [] # empty list of all lines in file

# read all lines from file into inputList

for line in infile:
   inputList = inputList + [line]

# Now inputList is a list of strings. 

students = [] # initalize to empty list

# make a list of students from the inputList

for item in inputList:
    thisStudent =  lineToStudent(item)
    students = students + [thisStudent]



def whatMajor(fName, listOfStudents):
    """
    return the major of first student in listOfStudents with first name fName, False if none found

    >>> whatMajor("FRED",[Student("MARY","KAY","MATH"), Student("FRED","CRUZ","HISTORY"), Student("CHRIS","GAUCHO","UNDEC")])
    'HISTORY'
    >>> whatMajor("MARY",[Student("MARY","KAY","MATH"), Student("FRED","CRUZ","HISTORY"), Student("CHRIS","GAUCHO","UNDEC")])
    'MATH'
    >>> whatMajor("CHRIS",[Student("MARY","KAY","MATH"), Student("FRED","CRUZ","HISTORY"), Student("CHRIS","GAUCHO","UNDEC")])
    'UNDEC'
    >>>
    """

    for i in range(len(listOfStudents)):

       # step through every item in listOfStudents
       # when you find a match, return that students's major

       if listOfStudents[i].fName == fName:
          return listOfStudents[i].major

    # if you got all the way through the loop and didn't find
    #  the name, return False

    return False

def whatLName(fName, listOfStudents):
    """
    return the last name of first student in listOfStudents with first name fName, False if none found

    >>> whatLName("FRED",[Student("FRED","CRUZ","HISTORY")])
    'CRUZ'
    >>> whatLName("MARY",[Student("MARY","KAY","MATH"), Student("FRED","CRUZ","HISTORY"), Student("CHRIS","GAUCHO","UNDEC")])
    'KAY'
    >>>
    """

    for i in range(len(listOfStudents)):

        if listOfStudents[i].fName == fName:
            return listOfStudents[i].lName

    return False



def countUndec(listOfStudents):
    """
    return the number of undeclared students in listOfStudents

    >>> countUndec([Student("MARY","KAY","MATH"), Student("FRED","CRUZ","HISTORY"), Student("CHRIS","GAUCHO","UNDEC")])
    1
    >>> countUndec([Student("MARY","KAY","MATH"), Student("FRED","CRUZ","HISTORY")])
    0
    >>>
    """

    count = 0

    for i in range(len(listOfStudents)):
        if listOfStudents[i].major == "UNDEC":
            count = count + 1

    return count



def lNamesOfUndec(listOfStudents):
    """
    return the list of last names of students that have UNDEC as their major, if none return empty list
    
    >>> lNamesOfUndec([Student("MARY","KAY","MATH"), Student("FRED","CRUZ","HISTORY"), Student("CHRIS","GAUCHO","UNDEC")])
    ['GAUCHO']
    >>> lNamesOfUndec([Student("MARY","KAY","MATH"), Student("FRED","CRUZ","HISTORY")])
    []
    >>>
    """

    answerList = []

    for i in range(len(listOfStudents)):
        if listOfStudents[i].major == "UNDEC":
            answerList = answerList + [listOfStudents[i].lName]

    return answerList



def majorToLNames(thisMajor, listOfStudents):
    """

    returns the list of last names of students with thisMajor, if none return empty list

    >>> majorToLNames("MATH" , [Student("MARY","KAY","MATH"), Student("FRED","CRUZ","HISTORY"), Student("CHRIS","GAUCHO","UNDEC")])
    ['KAY']
    >>> majorToLNames("HISTORY" , [Student("MARY","KAY","MATH"), Student("FRED","CRUZ","HISTORY"), Student("CHRIS","GAUCHO","UNDEC")])
    ['CRUZ']
    >>> majorToLNames("ECE" , [Student("MARY","KAY","MATH"), Student("FRED","CRUZ","HISTORY"), Student("CHRIS","GAUCHO","UNDEC")])
    []
    >>>
    """

    answerList = []

    for i in range(len(listOfStudents)):
        if listOfStudents[i].major == thisMajor:
            answerList = answerList + [listOfStudents[i].lName]

    return answerList



def allStudentsMajoringIn(thisMajor, listOfStudents):
    """
    returns the list of the entire Student named tuple of students with thisMajor, if none return empty list

    >>> allStudentsMajoringIn("HISTORY" , [Student("MARY","KAY","MATH"), Student("FRED","CRUZ","HISTORY"), Student("CHRIS","GAUCHO","UNDEC")])
    ['FRED', 'CRUZ', 'HISTORY']
    >>> allStudentsMajoringIn("MATH" , [Student("MARY","KAY","MATH"), Student("FRED","CRUZ","HISTORY"), Student("CHRIS","GAUCHO","UNDEC")])
    ['MARY', 'KAY', 'MATH']
    >>>
    
    """

    answerList = []

    for i in range(len(listOfStudents)):
        if listOfStudents[i].major == thisMajor:
            answerList = answerList + [listOfStudents[i].fName, listOfStudents[i].lName, listOfStudents[i].major]

    return answerList
    

# run tests on either whole file (testmod) or a single function (first param to run_docstring_examples)
import doctest
doctest.testmod(verbose=False)
#doctest.run_docstring_examples(lineToStudent, globals(), verbose=True)
#doctest.run_docstring_examples(allStudentsMajoringIn, globals(), verbose=True)
