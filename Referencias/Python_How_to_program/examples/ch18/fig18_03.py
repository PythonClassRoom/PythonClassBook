# Fig. 18.3: fig18_03.py
# Demonstrates the wait function.

import os
import sys
import time
import random

# generate random sleep times for child processes
sleepTime1 = random.randrange( 1, 6 )
sleepTime2 = random.randrange( 1, 6 )

# parent ready to fork first child process
try:
   forkPID1 = os.fork()  # create first child process
except OSError:
   sys.exit( "Unable to create first child. " )

if forkPID1 != 0:  # am I parent process?

   # parent ready to fork second child process
   try: 
      forkPID2 = os.fork()  # create second child process
   except OSError:
      sys.exit( "Unable to create second child." )

   if forkPID2 != 0:  # am I parent process?
      print "Parent waiting for child processes...\n" + \
         "\tpid: %d, forkPID1: %d, forkPID2: %d" \
         % ( os.getpid(), forkPID1, forkPID2 )

      # wait for any child process
      try:
         child1 = os.wait()[ 0 ]  # wait returns one child’s pid
      except OSError:
         sys.exit( "No more child processes." )

      print "Parent: Child %d finished first, one child left." \
         % child1

      # wait for another child process
      try:
         child2 = os.wait()[ 0 ]  # wait returns other child’s pid
      except OSError:
         sys.exit( "No more child processes." )

      print "Parent: Child %d finished second, no children left." \
         % child2

   elif forkPID2 == 0:  # am I second child process?      
      print """Child2 sleeping for %d seconds...
      \tpid: %d, forkPID1: %d, forkPID2: %d""" \
         % ( sleepTime2, os.getpid(), forkPID1, forkPID2 )
      time.sleep( sleepTime2 )  # sleep to simulate some work

elif forkPID1 == 0:  # am I first child process?
   print """Child1 sleeping for %d seconds...
      \tpid: %d, forkPID1: %d""" \
      % ( sleepTime1, os.getpid(), forkPID1 )
   time.sleep( sleepTime1 )  # sleep to simulate some work
 
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
