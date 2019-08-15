# Fig. 18.14: fig18_14.py
# Defining our own signal handler.

import time
import signal

def stop( signalNumber, frame ):
   global keepRunning
   keepRunning -= 1
   print "Ctrl-C pressed; keepRunning is", keepRunning

keepRunning = 3

# set the handler for SIGINT to be function stop
signal.signal( signal.SIGINT, stop )

while keepRunning:
   print "Executing..."
   time.sleep( 1 )

print "Program terminating..."
 
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
