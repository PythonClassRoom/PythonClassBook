# Fig. 22.12: fig22_12.py
# Driver to test class QueueModule.

from QueueModule import Queue
       
queue = Queue()

print "processing a Queue"

for i in range( 4 ):
   queue.enqueue( i )
   print "The queue is: ", queue

while not queue.isEmpty():
   dequeue = queue.dequeue()
   print dequeue, "dequeued"
   print "The queue is: ", queue

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
