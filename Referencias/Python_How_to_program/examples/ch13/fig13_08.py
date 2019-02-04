# Fig. 13.8: fig13_08.py
# Compiled regular-expression and match objects.

import re

testString = "Hello world"
formatString = "%-35s: %s"   # string for formatting the output

# create regular expression and compiled expression
expression = "Hello"
compiledExpression = re.compile( expression ) 

# print expression and compiled expression
print formatString % ( "The expression", expression )
print formatString % ( "The compiled expression",
   compiledExpression )

# search using re.search and compiled expression's search method
print formatString % ( "Non-compiled search",
   re.search( expression, testString ) )
print formatString % ( "Compiled search",
   compiledExpression.search( testString ) )

# print results of searching
print formatString % ( "search SRE_Match contains",
   re.search( expression, testString ).group() )
print formatString % ( "compiled search SRE_Match contains",
   compiledExpression.search( testString ).group() )

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
