# lab06.py by Kenneth Toombs for CS8 lab06, 11/13/2013
# Writing to files in Python

import os  # This allows access to operating system features

def webDirectory():
    """
    returns a string containing the folder associated with
    web directory http://www.cs.ucsb.edu/~yourusername/cs8/lab06
    """
    
    # Get the home directory

    myHome = os.getenv("HOME")
    if (type(myHome)!=str):
        
       # raise Exception is a way to force Python to vomit
       # if we've run into a situation we don't know how to handle
       raise Exception("Can't get home directory")

    return myHome + "/public_html/cs8/lab06"


def webAddress():
    """
    returns the URL (complete with the correct username) for
    http://www.cs.ucsb.edu/~yourusername/cs8/lab06
    """
    
    # Get the home directory

    myUsername = os.getenv("USER")
    if (type(myUsername)!=str):
        
       # raise Exception is a way to force Python to vomit
       # if we've run into a situation we don't know how to handle
       raise Exception("Can't get home directory")

    return "http://www.cs.ucsb.edu/~" + myUsername + "/cs8/lab06"


def makeWebDirectoryIfItDoesNotExistAlready():
    """
    Create the directory ~/public_html/cs8/lab06 unless it already
    exists.
    """
    # This code checks to see if the web directory
    # ~/public_html/cs8/lab06 already exists
    # If so,we just return---there is nothing to do!
    
    if (os.access(webDirectory(),os.F_OK)):
        return

    # If not, then create a web directory for this lab (cs8/lab06)
    # The 0o755 is the Python way or writing octal number 755 (rwxr-xr-x)

    else:
        os.makedirs(webDirectory(),0o755)

        
        
    # If you run this on CSIL, now you should be able to navigate to
    # http://www.cs.ucsb.edu/~yourusername/cs8/lab06 and see files




def webPageHeader(myTitle):
    """
    Returns a string with the head element for a web page
    with title myTitle.
    
    Example: webPageHeader("Temperatures") returns the
    header for a web page with temperatures on it, i.e.
    <head>
      <title>Temperatures</title>
    </head>
    """

    return ("<head>\n" +
      " <title>"+ myTitle + "</title>\n" + 
      "</head>\n")

        





def makeWeatherWebPage(inputFileName, outputFileName):


    weatherFile = open(inputFileName,"r")

    # Open the output file
    
    makeWebDirectoryIfItDoesNotExistAlready()
    
    htmlFileName = webDirectory() + "/" + outputFileName

    htmlFile = open(htmlFileName,"w")

    # Write the start of the HTML file
    
    htmlFile.write("<html>\n")
    htmlFile.write(webPageHeader("SB Weather"))
    htmlFile.write("<body>\n")
    htmlFile.write("<h1>SB Weather</h1>\n")
    htmlFile.write("<table border='1'>\n")

    # Write the table header

    htmlFile.write("<tr><th>Date</th><th>Precip (in)</th><th>High</th><th>Low</th><th>Wind Dir</th><th>Wind Speed</th><th>Rel Humid max</th><th>Rel Humid min</th></tr>\n")
    

    # process every line in the file---and for each one
    # write a line to the html for the web page
    
    for line in weatherFile:

        # Convert this line into a list
        lineAsAList = line.strip().split(",")

        # Pull out the first name, last name and major
        date = lineAsAList[0].strip()
        precipIn = lineAsAList[1].strip()
        high = lineAsAList[2].strip()
        low = lineAsAList[3].strip()
        windDir = lineAsAList[4].strip()
        windSpeed = lineAsAList[5].strip()
        relHumidMax = lineAsAList[6].strip()
        relHumidMin = lineAsAList[7].strip()

        # Write one line to the table

        htmlFile.write("<tr>" +
                       "<td>" + date + "</td>" +
                       "<td>" + precipIn + "</td>" +
                       "<td>" + high + "</td>" +
                       "<td>" + low + "</td>" +
                       "<td>" + windDir + "</td>" +
                       "<td>" + windSpeed + "</td>" +
                       "<td>" + relHumidMax + "</td>" +
                       "<td>" + relHumidMin + "</td>" +
                       "</tr>")

    htmlFile.write("</table>\n")
    htmlFile.write("</body>\n")
    htmlFile.write("</html>\n")

    # close the intput file and the output file
    
    weatherFile.close()
    htmlFile.close()

    # Tell the user where to find the page

    print("Look for the web page at this URL:\n")
    print(" " + webAddress() + "/" + outputFileName)

    print("Or if working on a PC or Mac, at this one:\n")
    print(" file://" + htmlFileName)

