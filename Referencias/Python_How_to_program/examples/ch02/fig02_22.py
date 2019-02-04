# Fig. 2.22: fig02_22.py
# Compare integers using if structures, relational operators
# and equality operators.

print "Enter two integers, and I will tell you"
print "the relationships they satisfy."

# read first string and convert to integer
number1 = raw_input( "Please enter first integer: " )
number1 = int( number1 )

# read second string and convert to integer
number2 = raw_input( "Please enter second integer: " )
number2 = int( number2 )

if number1 == number2:
   print "%d is equal to %d" % ( number1, number2 )

if number1 != number2:
   print "%d is not equal to %d" % ( number1, number2 )

if number1 < number2:
   print "%d is less than %d" % ( number1, number2 )

if number1 > number2:
   print "%d is greater than %d" % ( number1, number2 )

if number1 <= number2:
   print "%d is less than or equal to %d" % ( number1, number2 )

if number1 >= number2:
   print "%d is greater than or equal to %d" % ( number1, number2 )

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
