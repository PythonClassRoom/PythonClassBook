# Fig. 19.4: ProduceInteger.py
# Integer-producing class.

import threading
import random
import time

class ProduceInteger( threading.Thread ):
   """Thread to produce integers"""

   def __init__( self, threadName, sharedObject, begin, end ):
      """Initialize thread, set shared object"""
      
      threading.Thread.__init__( self, name = threadName )
      self.sharedObject = sharedObject
      self.begin = begin
      self.end = end

   def run( self ):
      """Produce integers in given range at random intervals"""

      for i in range( self.begin, ( self.end + 1 ) ):
         time.sleep( random.randrange( 4 ) )
         self.sharedObject.set( i )

      print "%s done producing." % self.getName()
      print "Terminating %s." % self.getName()

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
