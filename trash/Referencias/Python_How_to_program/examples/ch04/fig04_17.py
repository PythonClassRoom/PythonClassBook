# Fig. 4.17: fig04_17.py
# Recursive factorial function.

# Recursive definition of function factorial
def factorial( number ):

   if number <= 1:   # base case
      return 1
   else:
      return number * factorial( number - 1 )  # recursive call

for i in range( 11 ):
   print "%2d! = %d" % ( i, factorial( i ) )
 
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
