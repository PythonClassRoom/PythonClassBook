# Figure 19.14: fig19_14.py
# Semaphore to control access to a critical section.

import threading
import random
import time

class SemaphoreThread( threading.Thread ):
   """Class using semaphores"""

   availableTables = [ "A", "B", "C", "D", "E" ]   

   def __init__( self, threadName, semaphore ):
      """Initialize thread"""

      threading.Thread.__init__( self, name = threadName )
      self.sleepTime = random.randrange( 1, 6 )

      # set the semaphore as a data attribute of the class
      self.threadSemaphore = semaphore     

   def run( self ):
      """Print message and release semaphore"""

      # acquire the semaphore
      self.threadSemaphore.acquire()

      # remove a table from the list
      table = SemaphoreThread.availableTables.pop()
      print "%s entered; seated at table %s."  % \
         ( self.getName(), table ), 
      print SemaphoreThread.availableTables

      time.sleep( self.sleepTime )   # enjoy a meal

      # free a table
      print "   %s exiting; freeing table %s." % \
         ( self.getName(), table ),
      SemaphoreThread.availableTables.append( table )
      print SemaphoreThread.availableTables

      # release the semaphore after execution finishes
      self.threadSemaphore.release()

threads = []  # list of threads

# semaphore allows five threads to enter critical section
threadSemaphore = threading.Semaphore(
   len( SemaphoreThread.availableTables ) )

# create ten threads
for i in range( 1, 11 ):
   threads.append( SemaphoreThread( "thread" + str( i ),
      threadSemaphore ) )

# start each thread
for thread in threads:
   thread.start()

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
