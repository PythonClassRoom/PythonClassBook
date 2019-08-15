# Fig. 2.13: fig02_13.py
# Displaying an object's location, type and value.

# prompt the user for input
integer1 = raw_input( "Enter first integer:\n" )  # read a string
print "integer1: ", id( integer1 ), type( integer1 ), integer1 
integer1 = int( integer1 )   # convert the string to an integer
print "integer1: ", id( integer1 ), type( integer1 ), integer1

integer2 = raw_input( "Enter second integer:\n" ) # read a string
print "integer2: ", id( integer2 ), type( integer2 ), integer2
integer2 = int( integer2 )   # convert the string to an integer
print "integer2: ", id( integer2 ), type( integer2 ), integer2

sum = integer1 + integer2    # assignment of sum
print "sum: ", id( sum ), type( sum ), sum

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
