# Fig. 4.5: fig04_05.py
# Finding the maximum of three integers.

def maximumValue( x, y, z ):
   maximum = x

   if y > maximum:
      maximum = y

   if z > maximum:
      maximum = z

   return maximum

a = int( raw_input( "Enter first integer: " ) )
b = int( raw_input( "Enter second integer: " ) )
c = int( raw_input( "Enter third integer: " ) )

# function call
print "Maximum integer is:", maximumValue( a, b, c ) 
print   # print new line

d = float( raw_input( "Enter first float: " ) )
e = float( raw_input( "Enter second float: " ) )
f = float( raw_input( "Enter third float: " ) )
print "Maximum float is: ", maximumValue( d, e, f )
print

g = raw_input( "Enter first string: " )
h = raw_input( "Enter second string: " )
i = raw_input( "Enter third string: " )
print "Maximum string is: ", maximumValue( g, h, i )

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
