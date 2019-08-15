# Fig. 19.11: ConsumeFromQueue.py
# Integer-consuming queue.

import threading
import random
import time

class ConsumeFromQueue( threading.Thread ):
   """Thread to consume integers"""

   def __init__( self, threadName, queue ):
      """Initialize thread, set shared queue"""
      
      threading.Thread.__init__( self, name = threadName )
      self.sharedObject = queue

   def run( self ):
      """Consume 10 values at random time intervals"""
      
      sum = 0            # total sum of consumed values
      current = 10       # last value retrieved

      # consume 10 values
      for i in range( 10 ):
         time.sleep( random.randrange( 4 ) )
         print "%s attempting to read %s..." % \
            ( self.getName(), current + 1 )
         current = self.sharedObject.get()
         print "%s read %s" % ( self.getName(), current )
         sum += current

      print "%s retrieved values totaling: %d" % \
         ( self.getName(), sum )
      print "Terminating", self.getName()

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
