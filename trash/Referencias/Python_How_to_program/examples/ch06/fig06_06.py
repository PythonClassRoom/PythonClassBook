#!/usr/local/bin/python
# Fig. 6.6: fig06_06.py
# Example using QUERY_STRING.

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

printHeader( "QUERY_STRING example" )
print "<h1>Name/Value Pairs</h1>"

query = os.environ[ "QUERY_STRING" ]

if len( query ) == 0:
   print """<p><br />
      Please add some name-value pairs to the URL above.
      Or try 
      <a href = "fig06_06.py?name=Veronica&amp;age=23">this</a>.
      </p>"""
else:   
   print """<p style = "font-style: italic">
      The query string is '%s'.</p>""" % cgi.escape( query )
   pairs = cgi.parse_qs( query )

   for key, value in pairs.items():
      print "<p>You set '%s' to value %s</p>" % \
         ( key, value )

print "</body></html>"

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
