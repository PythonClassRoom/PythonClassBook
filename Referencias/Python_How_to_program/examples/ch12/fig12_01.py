# Fig. 12.1: fig12_01.py
# Simple exception handling example.

number1 = raw_input( "Enter numerator: " )
number2 = raw_input( "Enter denominator: " )

# attempt to convert and divide values
try:
   number1 = float( number1 )
   number2 = float( number2 )
   result = number1 / number2

# float raises a ValueError exception   
except ValueError:
   print "You must enter two numbers"

# division by zero raises a ZeroDivisionError exception   
except ZeroDivisionError:
   print "Attempted to divide by zero"

# else clause's suite executes if try suite raises no exceptions
else:
   print "%.3f / %.3f = %.3f" % ( number1, number2, result )

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
