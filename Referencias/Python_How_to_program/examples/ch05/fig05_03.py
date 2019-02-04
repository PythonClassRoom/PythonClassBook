# Fig. 5.3: fig05_03.py
# Creating, accessing and changing a list.

aList = []    # create empty list

# add values to list
for number in range( 1, 11 ):
   aList += [ number ]

print "The value of aList is:", aList   

# access list values by iteration
print "\nAccessing values by iteration:"

for item in aList:
   print item,

print   

# access list values by index
print "\nAccessing values by index:"
print "Subscript   Value"

for i in range( len( aList ) ):
   print "%9d %7d" % ( i, aList[ i ] )

# modify list
print "\nModifying a list value..."
print "Value of aList before modification:", aList
aList[ 0 ] = -100   
aList[ -3 ] = 19
print "Value of aList after modification:", aList

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
