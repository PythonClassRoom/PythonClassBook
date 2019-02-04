# Fig. 5.8: fig05_08.py
# Slicing sequences.

# create sequence
sliceString = "abcdefghij"
sliceTuple = ( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 )
sliceList = [ "I", "II", "III", "IV", "V",
              "VI", "VII", "VIII", "IX", "X" ]

# print strings
print "sliceString: ", sliceString
print "sliceTuple: ", sliceTuple
print "sliceList: ", sliceList
print

# get slices
start = int( raw_input( "Enter start: " ) )
end = int( raw_input( "Enter end: " ) )

# print slices
print "\nsliceString[", start, ":", end, "] = ", \
   sliceString[ start:end ]

print "sliceTuple[", start, ":", end, "] = ", \
   sliceTuple[ start:end ]

print "sliceList[", start, ":", end, "] = ", \
   sliceList[ start:end ]

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
