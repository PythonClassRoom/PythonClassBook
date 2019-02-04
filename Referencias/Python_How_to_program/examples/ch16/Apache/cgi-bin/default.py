#!/usr/local/bin/python
# Fig. 16.23: default.py
# Default page for message forums.

import os
import sys
from xml.dom.ext.reader import PyExpat

def printHeader( title, style ):
   print """Content-type: text/html

<?xml version = "1.0" encoding = "UTF-8"?>
<!DOCTYPE html PUBLIC
   "-//W3C//DTD XHTML 1.0 Strict//EN"
   "DTD/xhtml1-strict.dtd">
<html xmlns = "http://www.w3.org/1999/xhtml">

<head>
<title>%s</title>
<link rel = "stylesheet" href = "%s" type = "text/css" />
</head>

<body>""" % ( title, style )

# open XML document that contains the forum names and locations
try:
   XMLFile = open( "../htdocs/XML/forums.xml" )
except IOError:
   print "Location: /error.html\n"
   sys.exit()

# parse XML document containing forum information
reader = PyExpat.Reader()
document = reader.fromStream( XMLFile )
XMLFile.close()

# write XHTML to browser
printHeader( "Bug2Bug Message Forums", "/XML/site.css" )
print """<h1>Bug2Bug Message Forums</h1>
<p style="font-weight:bold">Available Forums</p>
<ul>"""

# determine client-browser type
if os.environ[ "HTTP_USER_AGENT" ].find( "MSIE" ) != -1:
   prefix = "../XML/"   # Internet Explorer
else:
   prefix = "forum.py?file="

# add links for each forum
for forum in document.getElementsByTagName( "forum" ):

   # create link to forum
   link = prefix + forum.attributes.item( 0 ).value

   # get element nodes containing tag name "name"
   name = forum.getElementsByTagName( "name" )[ 0 ]

   # get Text node's value
   nameText = name.childNodes[ 0 ].nodeValue
   print '<li><a href = "%s">%s</a></li>' % ( link, nameText )

print """</ul>
<p style="font-weight:bold">Forum Management</p>
<ul>
   <li><a href = "addForum.py">Add a Forum</a></li>
   <li>Delete a Forum</li>
   <li>Modify a Forum</li>
</ul>
</body>

</html>"""

reader.releaseNode( document )

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
