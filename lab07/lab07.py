# lab07.py by Kenneth Toombs for CS8 lab07, 11/26/13
# Testing functions
#  lab07StartingPoint.py
#   Starting point for lab07, CS8, 11/19/2013
#   Exercises for working with lists




  
def concatAllStrings(thelist):
    """
    returns a string which is the concatenation of all strings in thelist

    if thelist is not a list, return an empty string ""
    if thelilst is a list and contains items that are not strings, 
    ignore those and just concat the items that ARE strings.

    >>> concatAllStrings(['This', 'is', 'a', 'test'])
    'Thisisatest'
    >>> concatAllStrings([])
    ''
    >>> concatAllStrings(-42)
    ''
    >>> concatAllStrings([1, 2, 3])
    ''
    >>> concatAllStrings([1, 'Go', 3, 'Gauchos'])
    'GoGauchos'
    >>>
    """
    string = ""

    if type(thelist) != list:
        return ""
    
    for i in (thelist):
        
        if type(i) == str:
            string = string + i
   
            
    return string

    for i in thelist:

        if type(i) != str:
            return "" 






  
def onlyTheStrings(thelist):
    """
    returns a list which contains only the strings from thelist

    if thelist is not a list, return an empty list []
    thelist may contain things that are not strings---just ignore those items

    >>> onlyTheStrings(['This', 'is', 'a', 'test'])
    ['This', 'is', 'a', 'test']
    >>> onlyTheStrings([1, 'is', 3, 'test'])
    ['is', 'test']
    >>> onlyTheStrings([])
    []
    >>> onlyTheStrings(-42)
    []
    >>> onlyTheStrings([1, 2, 3])
    []
    >>>

    """
    resultList = []

    if type(thelist) != list:
        return []

    for i in thelist:
        if type(i) == str:
            resultList = resultList + [i]

    return resultList

    for i in thelist:
        if type(i) != str:
            return []



def removeItemX(thelist,x):
    """
    returns a copy of thelist with all occurences of item x removed

    if thelist is not a list, return an empty list []

    Note that it is possible that x does not occur in the list--in that case,
    return the original list unchanged

    >>> removeItemX(['This', 'is', 'a', 'test'], 'is')
    ['This', 'a', 'test']
    >>> removeItemX(['This', 'This', 'is', 'is', 'a', 'a', 'test'], 'a')
    ['This', 'This', 'is', 'is', 'test']
    >>> removeItemX([], 4)
    []
    >>> removeItemX([1, 2, 3, 4, 4, 3, 2, 1], 3)
    [1, 2, 4, 4, 2, 1]
    >>> removeItemX([1, 2, 3], 5)
    [1, 2, 3]
    >>>
    
    
    """

    resultList = []
    
    if type(thelist) != list:
        return []

    for i in thelist:
        if i != x:
            resultList = resultList + [i]
               

    return resultList




  
def removeDups(thelist):
    """
    returns a list in which all duplicate elements in thelist have been removed

    if thelist is not a list, return an empty list []

    >>> removeDups(['This', 'is', 'a', 'test'])
    ['This', 'is', 'a', 'test']
    >>> removeDups(['This', 'This', 'is', 'is', 'a', 'a', 'test', 'test'])
    ['This', 'is', 'a', 'test']
    >>> removeDups([])
    []
    >>> removeDups([1, 2, 3, 4, 4, 3, 2, 1])
    [1, 2, 3, 4]
    >>> removeDups([1, 2, 3])
    [1, 2, 3]
    >>> removeDups("1123")
    []
    >>> removeDups(21)
    []
    >>>

    """

    resultList = []

    if type(thelist) != list:
        return []

    for i in thelist:
        if i not in resultList:
            resultList = resultList + [i]

            
    return resultList


# The "main" routine that runs the tests from the docstrings.

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose="True")
    #doctest.run_docstring_examples(removeDups, globals(), verbose=True)
