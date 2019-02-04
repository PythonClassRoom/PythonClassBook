# Fig. 12.4: fig12_04.py
# Demonstrating exception arguments and stack unwinding.

import traceback

def function1():
   function2()

def function2():
   function3()

def function3():

   # raise exception, catch exception, reraise exception
   try:
      raise Exception, "An exception has occurred"
   except Exception:
      print "Caught exception in function3. Reraising....\n"
      raise   # reraises most recent exception

# call function1, any Exception it generates will be
# caught by the except clause that follows
try:
   function1()

# output exception arguments, string representation of exception,
# and the traceback
except Exception, exception:
   print "Exception caught in main program."
   print "\nException arguments:", exception.args
   print "\nException message:", exception
   print "\nTraceback:"
   traceback.print_exc()
   
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
