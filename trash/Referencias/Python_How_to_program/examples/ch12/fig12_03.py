# Fig. 12.3: fig12_03.py
# Using finally clauses.

def doNotRaiseException():

   # try block does not raise any exceptions
   try:
      print "In doNotRaiseException"

   # finally executes because corresponding try executed
   finally:
      print "Finally executed in doNotRaiseException"

   print "End of doNotRaiseException"

def raiseExceptionDoNotCatch():

   # raise exception, but do not catch it
   try:
      print "In raiseExceptionDoNotCatch"
      raise Exception

   # finally executes because corresponding try executed
   finally:
      print "Finally executed in raiseExceptionDoNotCatch"

   print "Will never reach this point"

# main program   

# Case 1: No exceptions occur in called function.
print "Calling doNotRaiseException"
doNotRaiseException()

# Case 2: Exception occurs, but is not handled in called function,
# because no except clauses exist in raiseExceptionDoNotCatch
print "\nCalling raiseExceptionDoNotCatch"

# call raiseExceptionDoNotCatch
try:
   raiseExceptionDoNotCatch()

# catch exception from raiseExceptionDoNotCatch
except Exception:
   print "Caught exception from raiseExceptionDoNotCatch " + \
      "in main program."

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
