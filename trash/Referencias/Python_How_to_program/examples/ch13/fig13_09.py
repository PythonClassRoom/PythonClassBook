# Fig. 13.9: fig13_09.py
# Repetition patterns, matching vs searching.

import re

testStrings = [ "Heo", "Helo", "Hellllo" ]
expressions = [ "Hel?o", "Hel+o", "Hel*o" ]

# match every expression with every string
for expression in expressions:

   for string in testStrings:

      if re.match( expression, string ):
         print expression, "matches", string
      else:
         print expression, "does not match", string

   print

# demonstrate the difference between matching and searching
expression1 = "elo"    # plain string
expression2 = "^elo"   # "elo" at beginning of string
expression3 = "elo$"   # "elo" at end of string

# match expression1 with testStrings[ 1 ]
if re.match( expression1, testStrings[ 1 ] ):
   print expression1, "matches", testStrings[ 1 ]

# search for expression1 in testStrings[ 1 ]
if re.search( expression1, testStrings[ 1 ] ):
   print expression1, "found in", testStrings[ 1 ]

# search for expression2 in testStrings[ 1 ]
if re.search( expression2, testStrings[ 1 ] ):
   print expression2, "found in", testStrings[ 1 ]

# search for expression3 in testStrings[ 1 ]
if re.search( expression3, testStrings[ 1 ] ):
   print expression3, "found in", testStrings[ 1 ]
    
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
