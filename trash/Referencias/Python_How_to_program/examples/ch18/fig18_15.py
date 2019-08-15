# Fig. 18.15: fig18_15.py
# Sending signals to child processes using kill

import os
import signal
import time
import sys

# handles both SIGALRM and SIGINT signals
def parentInterruptHandler( signum, frame ):
   global pid
   global parentKeepRunning

   # send kill signal to child process and exit
   os.kill( pid, signal.SIGKILL )  # send kill signal
   print "Interrupt received. Child process killed."

   # allow parent process to terminate normally
   parentKeepRunning = 0

# set parent's handler for SIGINT
signal.signal( signal.SIGINT, parentInterruptHandler )

# keep parent running until child process is killed
parentKeepRunning = 1

# parent ready to fork child process
try:
   pid = os.fork()  # create child process
except OSError:
   sys.exit( "Unable to create child process." )

if pid != 0:  # am I parent process?

   while parentKeepRunning:
      print "Parent running. Press Ctrl-C to terminate child."
      time.sleep( 1 )

elif pid == 0:  # am I child process?

   # ignore interrupt in child process
   signal.signal( signal.SIGINT, signal.SIG_IGN )

   while 1:
      print "Child still executing."
      time.sleep( 1 )

print "Parent terminated child process."
print "Parent terminating normally."
 
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
