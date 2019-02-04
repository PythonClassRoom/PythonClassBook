# Fig. 3.15: fig03_15.py
# Analysis of examination results.

# initialize variables
passes = 0                  # number of passes
failures = 0                # number of failures
studentCounter = 1          # student counter

# process 10 students; counter-controlled loop
while studentCounter <= 10:
   result = raw_input( "Enter result (1=pass,2=fail): " )
   result = int( result )   # one exam result

   if result == 1:
      passes = passes + 1
   else:
      failures = failures + 1

   studentCounter = studentCounter + 1

# termination phase
print "Passed", passes
print "Failed", failures

if passes > 8:
   print "Raise tuition"

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
