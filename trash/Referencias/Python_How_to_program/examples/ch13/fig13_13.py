# Fig. 13.13: fig13_13.py
# Regular-expression string manipulation.

import re

testString1 = "This sentence ends in 5 stars *****"
testString2 = "1,2,3,4,5,6,7"
testString3 = "1+2x*3-y"
formatString = "%-34s: %s"   # string to format output

print formatString % ( "Original string", testString1 )

# regular expression substitution
testString1 =  re.sub( r"\*", r"^", testString1 )
print formatString % ( "^ substituted for *", testString1 )

testString1 = re.sub( r"stars", "carets", testString1 )
print formatString % ( '"carets" substituted for "stars"',
   testString1 )

print formatString % ( 'Every word replaced by "word"',
   re.sub( r"\w+", "word", testString1 ) )

print formatString % ( 'Replace first 3 digits by "digit"',
   re.sub( r"\d", "digit", testString2, 3 ) )

# regular expression splitting
print formatString % ( "Splitting " + testString2,
   re.split( r",", testString2 ) )

print formatString % ( "Splitting " + testString3,
   re.split( r"[+\-*/%]", testString3 ) )

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
