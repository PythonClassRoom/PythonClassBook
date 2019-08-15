# Fig. 13.14: fig13_14.py
# Program that demonstrates grouping and greedy operations.

import re

formatString1 = "%-22s: %s"   # string to format output 

# string that contains fields and expression to extract fields
testString1 = \
   "Albert Antstein, phone: 123-4567, e-mail: albert@bug2bug.com"
expression1 = \
   r"(\w+ \w+), phone: (\d{3}-\d{4}), e-mail: (\w+@\w+\.\w{3})"

print formatString1 % ( "Extract all user data",
   re.match( expression1, testString1 ).groups() )
print formatString1 % ( "Extract user e-mail",
   re.match( expression1, testString1 ).group( 3 ) )
print

# greedy operations and grouping
formatString2 = "%-38s: %s"   # string to format output

# strings and patterns to find base directory in a path
pathString = "/books/2001/python"  # file path string

expression2 = "(/.+)/"  # greedy operator expression
print formatString1 % ( "Greedy error", 
   re.match( expression2, pathString ).group( 1 ) )

expression3 = "(/.+?)/"  # non-greedy operator expression
print formatString1 % ( "No error, base only", 
   re.match( expression3, pathString ).group( 1 ) )

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
