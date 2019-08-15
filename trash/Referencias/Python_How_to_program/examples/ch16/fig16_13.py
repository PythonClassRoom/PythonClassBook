# Fig. 16.13: fig16_13.py
# Using 4DOM to manipulate an XML Document.

import sys
from xml.dom.ext.reader import PyExpat
from xml.dom.ext import PrettyPrint

def printInstructions():
   print """\nEnter 'a' to add a contact.
Enter 'l' to list contacts.xml.
Enter 'i' for instructions.
Enter 'q' to quit."""

def printList( document ):
   print "Your contact list is:"

   # iterate over NodeList of contact elements
   for contact in document.getElementsByTagName( "contact" ):
      first = contact.getElementsByTagName( "FirstName" )[ 0 ]

      # get first node's value
      firstText = first.firstChild.nodeValue

      # get NodeList for nodes containing tag name "LastName"
      last = contact.getElementsByTagName( "LastName" )[ 0 ]
      lastText = last.firstChild.nodeValue

      print firstText, lastText

def addContact( document ):
   root = document.documentElement   # get root element node

   name = raw_input( 
      "Enter the name of the person you wish to add: " )

   first, last = name.split()

   # create first name element node
   firstNode = document.createElement( "FirstName" )
   firstNodeText = document.createTextNode( first )
   firstNode.appendChild( firstNodeText )

   # create last name element node
   lastNode = document.createElement( "LastName" )
   lastNodeText = document.createTextNode( last )
   lastNode.appendChild( lastNodeText )

   # create contact node, append first name and last name nodes
   contactNode = document.createElement( "contact" )
   contactNode.appendChild( firstNode )
   contactNode.appendChild( lastNode )
   
   root.appendChild( contactNode ) # add contact node

# open contacts file
try:
   file = open( "contacts.xml", "r+" )
except IOError:
   sys.exit( "Error opening file" )

# create DOM parser and parse XML document
reader = PyExpat.Reader()
document = reader.fromStream( file )

printList( document )
printInstructions()
character = "l"

while character != "q":   
   character = raw_input( "\n? " )

   if character == "a":
      addContact( document )
   elif character == "l":
      printList( document )
   elif character == "i":
      printInstructions()
   elif character != "q":
      print "Invalid command!"

file.seek( 0, 0 )               # position to beginning of file
file.truncate()                 # remove data from file
PrettyPrint( document, file )   # print DOM contents to file
file.close()                    # close XML file
reader.releaseNode( document )  # free memory

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
