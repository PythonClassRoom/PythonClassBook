# Fig. 19.5: ConsumeInteger.py
# Integer-consuming queue.

import threading
import random
import time

class ConsumeInteger( threading.Thread ):
   """Thread to consume integers"""

   def __init__( self, threadName, sharedObject, amount ):
      """Initialize thread, set shared object"""
      
      threading.Thread.__init__( self, name = threadName )
      self.sharedObject = sharedObject
      self.amount = amount

   def run( self ):
      """Consume given amount of values at random time intervals"""
      
      sum = 0   # total sum of consumed values

      # consume given amount of values
      for i in range( self.amount ):
         time.sleep( random.randrange( 4 ) )
         sum += self.sharedObject.get()

      print "%s read values totaling: %d." % \
         ( self.getName(), sum )
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
