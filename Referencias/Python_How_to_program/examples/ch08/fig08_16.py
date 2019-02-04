# Fig. 8.16: fig08_16.py
# Driver for class SimpleDictionary.

from NewDictionary import SimpleDictionary

# create and print SimpleDictionary object
simple = SimpleDictionary()
print "The empty dictionary:", simple

# add values to simple (invokes simple.__setitem__)
simple[ 1 ] = "one"
simple[ 2 ] = "two"
simple[ 3 ] = "three"
print "The dictionary after adding values:", simple

del simple[ 1 ]  # remove a value
print "The dictionary after removing a value:", simple

# use mapping methods
print "Dictionary keys:", simple.keys()
print "Dictionary values:", simple.values()
print "Dictionary items:", simple.items()

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
