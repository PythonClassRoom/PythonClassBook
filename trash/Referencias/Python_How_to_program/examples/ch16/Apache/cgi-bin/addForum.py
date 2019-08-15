#!/usr/local/bin/python
# Fig. 16.24: addForum.py
# Adds a forum to the list.

import re
import sys
import cgi

# 4DOM packages
from xml.dom.ext.reader import PyExpat
from xml.dom.ext import PrettyPrint

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

form = cgi.FieldStorage()

# if user enters data in form fields
if form.has_key( "name" ) and form.has_key( "filename" ):
   newFile = form[ "filename" ].value

   # determine whether file has xml extension
   if not re.match( "\w+\.xml$", newFile ):
      print "Location: /error.html\n"
      sys.exit()
   else:
      
      # create forum files from xml files
      try:
         newForumFile = open( "../htdocs/XML/" + newFile, "w" )
         forumsFile = open( "../htdocs/XML/forums.xml", "r+" )
         templateFile = open( "../htdocs/XML/template.xml" )
      except IOError:
         print "Location: /error.html\n"
         sys.exit()

      # parse forums document
      reader = PyExpat.Reader()
      document = reader.fromStream( forumsFile )

      # add new forum element
      forum = document.createElement( "forum" )
      forum.setAttribute( "filename", newFile )

      name = document.createElement( "name" )
      nameText = document.createTextNode( form[ "name" ].value )
      name.appendChild( nameText )
      forum.appendChild( name )

      # obtain root element of forum
      documentNode = document.documentElement
      firstForum = documentNode.getElementsByTagName( 
         "forum" )[ 0 ]
      documentNode.insertBefore( forum, firstForum )
   
      # write updated XML to disk
      forumsFile.seek( 0, 0 )
      forumsFile.truncate()
      PrettyPrint( document, forumsFile )
      forumsFile.close()

      # create document for new forum from template file
      document = reader.fromStream( templateFile )
      forum = document.documentElement
      forum.setAttribute( "file", newFile )

      # create name element
      name = document.createElement( "name" )
      nameText = document.createTextNode( form[ "name" ].value )
      name.appendChild( nameText )
      forum.appendChild( name )

      # write generated XML to new forum file
      PrettyPrint( document, newForumFile )
      newForumFile.close()
      templateFile.close()
      reader.releaseNode( document )

      print "Location: default.py\n"
else:
   printHeader( "Add a forum", "/XML/site.css" )
   print """<form action = "addForum.py" method="post">
Forum Name<br />
<input type = "text" name = "name" size = "40" /><br />
Forum File Name<br />
<input type = "text" name = "filename" size = "40" /><br />
<input type = "submit" name = "submit" value = "Submit" />
<input type = "reset" value = "Reset" />
</form>

<a href = "/cgi-bin/default.py">Return to Main Page</a>
</body>

</html>"""

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
