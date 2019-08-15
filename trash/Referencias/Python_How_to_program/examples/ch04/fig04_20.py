# Fig. 4.20: fig04_20.py
# Using default arguments.

# function definition with default arguments
def boxVolume( length = 1, width = 1, height = 1 ):
   return length * width * height

print "The default box volume is:", boxVolume()
print "\nThe volume of a box with length 10,"
print "width 1 and height 1 is:", boxVolume( 10 )
print "\nThe volume of a box with length 10,"
print "width 5 and height 1 is:", boxVolume( 10, 5 )
print "\nThe volume of a box with length 10,"
print "width 5 and height 2 is:", boxVolume( 10, 5, 2 )

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
