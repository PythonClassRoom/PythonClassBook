#!/usr/local/bin/python
# Fig. 16.2: fig16_02.py
# Marking up a text file's data as XML.

import sys

print "Content-type: text/xml\n"

# write XML declaration and processing instruction
print """<?xml version = "1.0"?>
<?xml:stylesheet type = "text/xsl"
   href = "../XML/contact_list.xsl"?>"""

# open data file
try:
   file = open( "names.txt", "r" )
except IOError:
   sys.exit( "Error opening file" )

print "<contacts>" # write root element

# list of tuples: ( special character, entity reference )
replaceList = [ ( "&", "&amp;" ),
                ( "<", "&lt;" ),
                ( ">", "&gt;" ),
                ( '"', "&quot;" ),
                ( "'", "&apos;" ) ]

# replace special characters with entity references
for currentLine in file.readlines():

   for oldValue, newValue in replaceList:
      currentLine = currentLine.replace( oldValue, newValue )

   # extract lastname and firstname
   last, first = currentLine.split( ", " )
   first = first.strip() # remove carriage return

   # write contact element
   print """   <contact>"
      <LastName>%s</LastName>
      <FirstName>%s</FirstName>
   </contact>""" % ( last, first )

file.close()

print "</contacts>"

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
