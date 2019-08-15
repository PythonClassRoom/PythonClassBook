# Fig. 19.9: fig19_09.py
# Multiple threads producing/consuming values.

from Queue import Queue
from ProduceToQueue import ProduceToQueue
from ConsumeFromQueue import ConsumeFromQueue

# initialize number and threads
queue = Queue()
producer = ProduceToQueue( "Producer", queue )
consumer = ConsumeFromQueue( "Consumer", queue )

print "Starting threads...\n"

# start threads
producer.start()
consumer.start()

# wait for threads to terminate
producer.join()
consumer.join()

print "\nAll threads have terminated."

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
