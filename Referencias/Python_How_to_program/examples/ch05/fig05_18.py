# Fig. 5.18: fig05_18.py
# Searching a list for an integer.

# Create a list of even integers 0 to 198
aList = range( 0, 199, 2 )

secarhKey = int( raw_input( "Enter integer search key: " ) )

if secarhKey in aList:
   print "Found at index:", aList.index( secarhKey )
else:
   print "Value not found"

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
