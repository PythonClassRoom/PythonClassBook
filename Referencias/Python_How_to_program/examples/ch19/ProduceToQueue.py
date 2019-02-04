# Fig. 19.10: ProduceToQueue.py
# Integer-producing class.

import threading
import random
import time

class ProduceToQueue( threading.Thread ):
   """Thread to produce integers"""

   def __init__( self, threadName, queue ):
      """Initialize thread, set shared queue"""
      
      threading.Thread.__init__( self, name = threadName )
      self.sharedObject = queue
      
   def run( self ):
      """Produce integers in range 11-20 at random intervals"""

      for i in range( 11, 21 ):
         time.sleep( random.randrange( 4 ) )
         print "%s adding %s to queue" % ( self.getName(), i )
         self.sharedObject.put( i )

      print self.getName(), "finished producing values"
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
