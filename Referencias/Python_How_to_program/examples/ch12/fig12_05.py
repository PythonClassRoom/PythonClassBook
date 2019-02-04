# Fig. 12.5: fig12_05.py
# Demonstrating a programmer-defined exception class.

import math

class NegativeNumberError( ArithmeticError ):
   """Attempted improper operation on negative number."""
   pass

def squareRoot( number ):
   """Computes square root of number. Raises NegativeNumberError
   if number is less than 0."""

   if number < 0:
      raise NegativeNumberError, \
         "Square root of negative number not permitted"

   return math.sqrt( number )

while 1:

   # get user-entered number and compute square root
   try:
      userValue = float( raw_input( "\nPlease enter a number: " ) )
      print squareRoot( userValue )

   # float raises ValueError if input is not numerical
   except ValueError:
      print "The entered value is not a number"

   # squareRoot raises NegativeNumberError if number is negative
   except NegativeNumberError, exception:
      print exception

   # successful execution: terminate while loop
   else:
      break

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
