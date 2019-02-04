#!/usr/local/bin/python
# Fig. 6.12: fig06_12.py
# Handles entry to Bug2Bug Travel.

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

form = cgi.FieldStorage()

if not form.has_key( "name" ):
   print "Location: /fig06_11.html\n"
else:
   printHeader( "Bug2Bug Travel" )
   print "<h1>Welcome, %s!</h1>" % form[ "name" ].value
   print """<p>Here are our weekly specials:<br /></p>
      <ul><li>Boston to Taiwan for $300</li></ul>"""

   if not form.has_key( "password" ):
      print """<p style = "font-style: italic">
         Become a member today for more great deals!</p>"""
   elif form[ "password" ].value == "Coast2Coast":
      print """<hr />
         <p>Current specials just for members:<br /></p>
         <ul><li>San Diego to Hong Kong for $250</li></ul>"""
   else:
      print """<p style = "font-style: italic">
         Sorry, you have entered the wrong password.
         If you have the correct password, enter
         it to see more specials.</p>"""

   print "<hr /></body></html>"

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
