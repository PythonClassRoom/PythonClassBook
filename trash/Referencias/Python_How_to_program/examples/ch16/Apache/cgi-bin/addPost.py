#!/usr/local/bin/python
# Fig. 16.26: addPost.py
# Adds a message to a forum.

import re
import os
import sys
import cgi
import time

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

# identify client browser
if os.environ[ "HTTP_USER_AGENT" ].find( "MSIE" ) != -1:
   prefix = "../XML/"   # Internet Explorer
else:
   prefix = "forum.py?file="

form = cgi.FieldStorage()

# user has submitted message to post
if form.has_key( "submit" ):
   filename = form[ "file" ].value

   # add message to forum
   if not re.match( "\w+\.xml$", filename  ):
      print "Location: /error.html\n"
      sys.exit()

   try:
      forumFile = open( "../htdocs/XML/" + filename, "r+" )
   except IOError:
      print "Location: /error.html\n"
      sys.exit()

   # parse forum document
   reader = PyExpat.Reader()
   document = reader.fromStream( forumFile )
   documentNode = document.documentElement

   # create message element   
   message = document.createElement( "message" )
   message.setAttribute( "timestamp", time.ctime( time.time() ) )

   # add elements to message
   messageElements = [ "user", "title", "text" ]

   for item in messageElements:
   
      if not form.has_key( item ):
         text = "( Field left blank )"
      else:
         text = form[ item ].value

      # create nodes
      element = document.createElement( item )      
      elementText = document.createTextNode( text )
      element.appendChild( elementText )
      message.appendChild( element )

   # append new message to forum and update document on disk
   documentNode.appendChild( message )
   forumFile.seek( 0, 0 )
   forumFile.truncate()
   PrettyPrint( document, forumFile )
   forumFile.close()
   reader.releaseNode( document )
   
   print "Location: %s\n" % ( prefix + form[ "file" ].value )

# create form to obtain new message
elif form.has_key( "file" ):
   printHeader( "Add a posting", "/XML/site.css" )
   print """\n<form action = "addPost.py" method="post">
User<br />
<input type = "text" name = "user" size = "40" /><br />
Message Title<br />
<input type = "text" name = "title" size = "40" /><br />
Message Text<br />
<textarea name = "text" cols = "40" rows = "5"></textarea><br />
<input type = "hidden" name = "file" value = "%s" />
<input type = "submit" name = "submit" value = "Submit" />
<input type = "reset" value = "Reset" />
</form>

<a href = "%s">Return to Forum</a>
</body>

</html>""" % ( form[ "file" ].value,
   prefix + form[ "file" ].value )
else:
   print "Location: /error.html\n"

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
