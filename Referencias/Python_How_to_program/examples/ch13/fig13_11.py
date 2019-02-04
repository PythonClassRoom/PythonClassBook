# Fig. 13.11: fig13_11.py
# Program that demonstrates classes and special sequences.

import re

# specifying character classes with [ ]
testStrings = [ "2x+5y","7y-3z" ]
expressions = [ r"2x\+5y|7y-3z",                
                r"[0-9][a-zA-Z0-9_].[0-9][yz]", 
                r"\d\w-\d\w" ]

# match every expression with every string
for expression in expressions:

   for testString in testStrings:

      if re.match( expression, testString ):
         print expression, "matches", testString

# specifying character classes with special sequences
testString1 = "800-123-4567"
testString2 = "617-123-4567"
testString3 = "email: \t joe_doe@deitel.com"

expression1 = r"^\d{3}-\d{3}-\d{4}$"
expression2 = r"\w+:\s+\w+@\w+\.(com|org|net)"

# matching with character classes
if re.match( expression1, testString1 ):
   print expression1, "matches", testString1

if re.match( expression1, testString2 ):
   print expression1, "matches", testString2

if re.match( expression2, testString3 ):
   print expression2, "matches", testString3

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
