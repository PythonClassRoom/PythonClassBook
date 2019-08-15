# Fig. 5.9: fig05_09.py
# Creating, accessing and modifying a dictionary.

# create and print an empty dictionary
emptyDictionary = {}
print "The value of emptyDictionary is:", emptyDictionary

# create and print a dictionary with initial values
grades = { "John": 87, "Steve": 76, "Laura": 92, "Edwin": 89 }
print "\nAll grades:", grades

# access and modify an existing dictionary
print "\nSteve's current grade:", grades[ "Steve" ]
grades[ "Steve" ] = 90
print "Steve's new grade:", grades[ "Steve" ]

# add to an existing dictionary
grades[ "Michael" ] = 93
print "\nDictionary grades after modification:"
print grades

# delete entry from dictionary
del grades[ "John" ]
print "\nDictionary grades after deletion:"
print grades

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
