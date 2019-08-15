# Fig. 13.6: fig13_06.py
# Token splitting and delimiter joining.

# splitting strings
string1 = "A, B, C, D, E, F"

print "String is:", string1
print "Split string by spaces:", string1.split()
print "Split string by commas:", string1.split( "," )
print "Split string by commas, max 2:", string1.split( ",", 2 )
print

# joining strings
list1 =  [ "A", "B", "C", "D", "E", "F" ]
string2 = "___"

print "List is:", list1
print 'Joining with "%s": %s' \
   % ( string2, string2.join ( list1 ) )
print 'Joining with "-.-":', "-.-".join( list1 )

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
