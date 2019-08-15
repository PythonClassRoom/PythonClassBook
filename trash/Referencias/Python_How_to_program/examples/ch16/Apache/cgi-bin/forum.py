#!/usr/local/bin/python
# Fig. 16.29: forum.py
# Display forum postings for non-Internet Explorer browsers.

import re
import cgi
import sys
from xml.xslt import Processor

form = cgi.FieldStorage()

# form to display has been specified
if form.has_key( "file" ):

   # determine whether file is xml
   if not re.match( "\w+\.xml$", form[ "file" ].value ):
      print "Location: /error.html\n"
      sys.exit()

   try:
      style = open( "../htdocs/XML/formatting.xsl" )
      XMLFile = open( "../htdocs/XML/" + form[ "file" ].value )
   except IOError:
      print "Location: /error.html\n"
      sys.exit()

   # create XSLT processor instance
   processor = Processor.Processor()

   # specify style sheet
   processor.appendStylesheetStream( style )

   # apply style sheet to XML document
   results = processor.runStream( XMLFile )
   style.close()
   XMLFile.close()
   print "Content-type: text/html\n"
   print results
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
