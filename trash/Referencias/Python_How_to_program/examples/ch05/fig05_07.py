# Fig. 5.7: fig05_07.py
# Unpacking sequences.

# create sequences
aString = "abc"
aList = [ 1, 2, 3 ]
aTuple = "a", "A", 1

# unpack sequences to variables
print "Unpacking string..."
first, second, third = aString
print "String values:", first, second, third

print "\nUnpacking list..."
first, second, third = aList
print "List values:", first, second, third

print "\nUnpacking tuple..."
first, second, third = aTuple
print "Tuple values:", first, second, third

# swapping two values
x = 3
y = 4

print "\nBefore swapping: x = %d, y = %d" % ( x, y )
x, y = y, x     # swap variables
print "After swapping: x = %d, y = %d" % ( x, y )

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
