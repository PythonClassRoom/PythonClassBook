#!/usr/local/bin/python
# Fig 6.5: fig06_05.py
# Program to display CGI environment variables.

import os
import cgi

def printHeader( title ):
   print """Content-type: text/html

<?xml version = "1.0" encoding = "UTF-8"?>    
<!DOCTYPE html PUBLIC
   "-//W3C//DTD XHTML 1.0 Strict//EN"
   "DTD/xhtml1-strict.dtd">
<html xmlns = "http://www.w3.org/1999/xhtml">
<head><title>%s</title></head>

<body>""" % title

rowNumber = 0
backgroundColor = "white"

printHeader( "Environment Variables" )
print """<table style = "border: 0">"""

# print table of cgi variables and values
for item in os.environ.keys():
   rowNumber += 1

   if rowNumber % 2 == 0:          # even row numbers are white
      backgroundColor = "white"
   else:                           # odd row numbers are grey
      backgroundColor = "lightgrey"

   print """<tr style = "background-color: %s">
   <td>%s</td><td>%s</td></tr>""" % ( backgroundColor,
      cgi.escape( item ), cgi.escape( os.environ[ item ] ) )

print """</table></body></html>"""

########################################################################## 
# (C) Copyright 2002 by Deitel & Associates, Inc. and Prentice Hall.     #
# All Rights Reserved.                                                   #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
