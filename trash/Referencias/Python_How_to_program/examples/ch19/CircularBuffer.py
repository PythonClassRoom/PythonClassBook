# Fig. 19.13: CircularBuffer.py
# Synchronized circular buffer of integer values.

import threading

class CircularBuffer:

   def __init__( self ):
      """Set buffer, count, locations and condition variable"""

      # each element in list is a buffer      
      self.buffer = [ -1, -1, -1 ]
      
      self.occupiedBufferCount = 0   # count of occupied buffers
      self.readLocation = 0          # current reading index
      self.writeLocation = 0         # current writing index
      
      self.threadCondition = threading.Condition()

   def set( self, newNumber ):
      """Set next buffer index value--blocks until lock acquired"""

      # block until lock released then acquire lock      
      self.threadCondition.acquire()

      # while all buffers are full, release lock and block      
      while self.occupiedBufferCount == len( self.buffer ):
         print "All buffers full. %s waits." % \
            threading.currentThread().getName()
         self.threadCondition.wait()

      # (there is an empty buffer, lock has been re-acquired)

      # place value in writeLocation of buffer
      # print string indicating produced value
      self.buffer[ self.writeLocation ] = newNumber
      print "%s writes %d " % \
         ( threading.currentThread().getName(), newNumber ),

      # produced value, so increment number of occupied buffers
      self.occupiedBufferCount += 1

      # update writeLocation for future write operation
      # add current state to output
      self.writeLocation = ( self.writeLocation + 1 ) % \
         len( self.buffer )
      self.displayState()  

      self.threadCondition.notify()    # wake up a waiting thread
      self.threadCondition.release()   # allow lock to be acquired

   def get( self ):
      """Get next buffer index value--blocks until lock acquired"""

      # block until lock released then acquire lock
      self.threadCondition.acquire()

      # while all buffers are empty, release lock and block
      while self.occupiedBufferCount == 0:
         print "All buffers empty. %s waits." % \
            threading.currentThread().getName()
         self.threadCondition.wait()

      # (there is a full buffer, lock has been re-acquired)

      # obtain value at current readLocation
      # print string indicating consumed value
      tempNumber = self.buffer[ self.readLocation ]
      print "%s reads %d " % ( threading.currentThread().getName(),
         tempNumber ),

      # consumed value, so decrement number of occupied buffers
      self.occupiedBufferCount -= 1

      # update readLocation for future read operation
      # add current state to output
      self.readLocation = ( self.readLocation + 1 ) % \
         len( self.buffer )
      self.displayState()  

      self.threadCondition.notify()    # wake up a waiting thread
      self.threadCondition.release()   # allow lock to be acquired

      return tempNumber

   def displayState( self ):
      """Display current state"""

      # display first line of state information
      print "(buffers occupied: %d)" % self.occupiedBufferCount
      print "buffers: ",

      for item in self.buffer:
         print " %d  " % item,
         
      # display second line of state information
      print "\n         ",

      for item in self.buffer:
         print "---- ",

      # display third line of state information
      print "\n         ",

      for i in range( len( self.buffer ) ):

         if ( i == self.writeLocation ) and \
            ( self.writeLocation == self.readLocation ):
            print " WR  ",
         elif ( i == self.writeLocation ):
            print " W   ",
         elif ( i == self.readLocation ):
            print "  R  ",
         else:
            print "     ",

      print "\n"
   
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
