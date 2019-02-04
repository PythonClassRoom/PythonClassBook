# Fig. 19.8: SynchronizedInteger.py
# Synchronized access to an integer with condition variable.

import threading

class SynchronizedInteger:
   """Class that provides synchronized access an integer"""

   def __init__( self ):
      """Initialize integer, buffer count and condition variable"""
      
      self.buffer = -1  
      self.occupiedBufferCount = 0   # number of occupied buffers
      self.threadCondition = threading.Condition()

   def set( self, newNumber ):
      """Set value of integer--blocks until lock acquired"""

      # block until lock released then acquire lock
      self.threadCondition.acquire()   

      # while not producer's turn, release lock and block
      while self.occupiedBufferCount == 1:
         print "%s tries to write." % \
            threading.currentThread().getName()
         self.displayState( "Buffer full. " + \
            threading.currentThread().getName() + " waits." )
         self.threadCondition.wait()

      # (lock has now been re-acquired)

      self.buffer = newNumber         # set new buffer value
      self.occupiedBufferCount += 1   # allow consumer to consume

      self.displayState( "%s writes %d" % \
         ( threading.currentThread().getName(), newNumber ) )

      self.threadCondition.notify()    # wake up a waiting thread
      self.threadCondition.release()   # allow lock to be acquired

   def get( self ):
      """Get value of integer--blocks until lock acquired"""

      # block until lock released then acquire lock
      self.threadCondition.acquire()   

      # while producer's turn, release lock and block
      while self.occupiedBufferCount == 0:
         print "%s tries to read." % \
            threading.currentThread().getName()
         self.displayState( "Buffer empty. " + \
            threading.currentThread().getName() + " waits." )
         self.threadCondition.wait()   

      # (lock has now been re-acquired)

      tempNumber = self.buffer
      self.occupiedBufferCount -= 1 # allow producer to produce
      
      self.displayState( "%s reads %d" % \
         ( threading.currentThread().getName(), tempNumber ) )

      self.threadCondition.notify()    # wake up a waiting thread
      self.threadCondition.release()   # allow lock to be acquired

      return tempNumber

   def displayState( self, operation ):
      """Display current state"""
      
      print "%-35s %-9s%2s\n" % \
         ( operation, self.buffer, self.occupiedBufferCount )

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
