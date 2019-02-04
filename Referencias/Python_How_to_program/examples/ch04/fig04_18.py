# Fig. 4.18: fig04_18.py
# Recursive fibonacci function.

def fibonacci( n ):

   if n == 0 or n == 1:  # base case
      return n
   else:

      # two recursive calls
      return fibonacci( n - 1 ) + fibonacci( n - 2 )

number = int( raw_input( "Enter an integer: " ) )

if n > 0:
   result = fibonacci( number )
   print "Fibonacci(%d) = %d" % ( number, result )
else:
   print "Cannot find the fibonacci of a negative number"
 
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
