# Fig. 9.15: fig09_15.py
# Class that defines method __getattribute__

class DemonstrateAccess( object ):
   """Class to demonstrate when method __getattribute__ executes"""

   def __init__( self ):
      """DemonstrateAccess constructor, initializes attribute
      value"""

      self.value = 1
      
   def __getattribute__( self, name ):
      """Executes for every attribute access"""

      print "__getattribute__ executing..."
      print "\tClient attempt to access attribute:", name

      return object.__getattribute__( self, name )

   def __getattr__( self, name ):
      """Executes when client access attribute not in __dict__"""

      print "__getattr__ executing..."
      print "\tClient attempt to access non-existent attribute:",\
         name

      raise AttributeError, "Object has no attribute %s" \
         % name

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