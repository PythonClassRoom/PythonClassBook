# Fig. 19.6: UnsynchronizedInteger.py
# Unsynchronized access to an integer.

import threading

class UnsynchronizedInteger:
   """Class that provides unsynchronized access an integer"""

   def __init__( self ):
      """Initialize integer to -1"""
      
      self.buffer = -1

   def set( self, newNumber ):
      """Set value of integer"""
      
      print "%s writes %d" % \
         ( threading.currentThread().getName(), newNumber )
      self.buffer = newNumber

   def get( self ):
      """Get value of integer"""
      
      tempNumber = self.buffer
      print "%s reads %d" % \
         ( threading.currentThread().getName(), tempNumber )
      
      return tempNumber

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
