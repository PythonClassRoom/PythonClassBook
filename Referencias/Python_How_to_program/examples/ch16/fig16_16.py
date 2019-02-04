# Fig. 16.16: fig16_16.py
# Demonstrating SAX-based parsing.

from xml.sax import parse, SAXParseException, ContentHandler

class TagInfoHandler( ContentHandler ):
   """Custom xml.sax.ContentHandler"""

   def __init__( self, tagName ):
      """Initialize ContentHandler and set tag to search for"""
      
      ContentHandler.__init__( self )
      self.tagName = tagName
      self.depth = 0 # spaces to indent to show structure

   # override startElement handler
   def startElement( self, name, attributes ):
      """An Element has started"""

      # check if this is the tag name for which we are searching
      if name == self.tagName:
         print "\n%s<%s> started" % ( " " * self.depth, name )

         self.depth += 3

         print "%sAttributes:" % ( " " * self.depth )
         
         # check if element has attribute process
         for attribute in attributes.getNames():
            print "%s%s = %s" % ( " " * self.depth, attribute,
               attributes.getValue( attribute ) )

   # override endElement handler
   def endElement( self, name ):
      """An Element has ended"""

      if name == self.tagName:
         self.depth -= 3
         print "%s</%s> ended\n" % ( " " * self.depth, name )

def main():
   file = raw_input( "Enter a file to parse: " )
   tagName = raw_input( "Enter tag to search for: " )
   
   try:
      parse( file, TagInfoHandler( tagName ) )

   # handle exception if unable to open file
   except IOError, message:
      print "Error reading file:", message

   # handle exception parsing file
   except SAXParseException, message:
      print "Error parsing file:", message

if __name__ == "__main__":
   main()

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
