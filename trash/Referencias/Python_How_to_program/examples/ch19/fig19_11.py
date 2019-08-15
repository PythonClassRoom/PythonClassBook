# Figure 19.11: fig19_11.py
# Semaphore to control access to a critical section.

import threading
import random
import time

class SemaphoreThread( threading.Thread ):
    "Class using semaphores"
    
    threadCount = 0  # number of threads in critical section

    def __init__( self, threadName, semaphore ):
        "Initialize thread"

        threading.Thread.__init__( self, name = threadName )
        self.sleepTime = random.randrange( 1, 6 )

        # set the semaphore as a data attribute of the class
        self.threadSemaphore = semaphore

	# allow only one thread to access threadCount at a time
	self.threadCondition = threading.Condition()       

    def run( self ):
        "Print message and release semaphore"

        # acquire the semaphore
	self.threadSemaphore.acquire()

	print "%s is executing;" % self.getName(),

	# increment threadCount
	self.threadCondition.acquire()
	SemaphoreThread.threadCount += 1

	# local variable holds threadCount's value 
	threads = SemaphoreThread.threadCount
	self.threadCondition.release()
	
        print "%s entered critical section as thread number %d" \
           % ( self.getName(), threads )
	time.sleep( self.sleepTime )

	# decrement threadCount
	self.threadCondition.acquire()
	SemaphoreThread.threadCount -= 1
	
	print "%s exiting critical section;" % self.getName(),
	print "Number of threads in critical section: %d" \
            % SemaphoreThread.threadCount 
	
	self.threadCondition.release()
	
	# release the semaphore after execution finishes
	self.threadSemaphore.release()
 
threads = []  # list of threads

# semaphore allows five threads to enter critical section
threadSemaphore = threading.Semaphore( 5 )
 
# create ten threads
for i in range( 1, 11 ):
    threads.append( SemaphoreThread( "thread" + str( i ),
       threadSemaphore ) )

# start each thread
for i in range( 0, 10 ):
    threads[ i ].start()
	      
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
