# Fig. 16.4: fig16_04.py
# Using 4DOM to traverse an XML Document.

import sys
from xml.dom.ext import StripXml
from xml.dom.ext.reader import PyExpat
from xml.parsers.expat import ExpatError

# open XML file
try:
   file = open( "article2.xml" )
except IOError:
   sys.exit( "Error opening file" )

# parse contents of XML file
try:
   reader = PyExpat.Reader()            # create Reader instance
   document = reader.fromStream( file ) # parse XML document
   file.close()
except ExpatError:
   sys.exit( "Error processing XML file" )

# get root element
rootElement = StripXml( document.documentElement )
print "Here is the root element of the document: %s" % \
   rootElement.nodeName

# traverse all child nodes of root element
print "The following are its child elements:"

for node in rootElement.childNodes:
   print node.nodeName

# get first child node of root element
child = rootElement.firstChild
print "\nThe first child of root element is:", child.nodeName
print "whose next sibling is:",

# get next sibling of first child
sibling = child.nextSibling
print sibling.nodeName
print 'Value of "%s" is:' % sibling.nodeName,

value = sibling.firstChild

# print text value of sibling
print value.nodeValue
print "Parent node of %s is: %s" % \
   ( sibling.nodeName, sibling.parentNode.nodeName )

reader.releaseNode( document ) # remove DOM tree from memory

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
