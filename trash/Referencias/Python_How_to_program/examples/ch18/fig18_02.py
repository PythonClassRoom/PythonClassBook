# Fig. 18.2: fig18_02.py
# Using fork to create child processes.

import os
import sys
import time

processName = "parent"  # only the parent is running now

print "Program executing\n\tpid: %d, processName: %s" \
   % ( os.getpid(), processName )

# attempt to fork child process
try:
   forkPID = os.fork()  # create child process
except OSError:
   sys.exit( "Unable to create new process." )

if forkPID != 0:  # am I parent process?
   print "Parent executing\n" + \
      "\tpid: %d, forkPID: %d, processName: %s" \
      % ( os.getpid(), forkPID, processName )
   
elif forkPID == 0:  # am I child process?
   processName = "child"
   print "Child executing\n" + \
      "\tpid: %d, forkPID: %d, processName: %s" \
      % ( os.getpid(), forkPID, processName )

print "Process finishing\n\tpid: %d, processName: %s" \
   % ( os.getpid(), processName )
 
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
