# Fig. 5.13: fig05_13.py
# Dictionary methods.

monthsDictionary = { 1 : "January", 2 : "February", 3 : "March",
                4 : "April", 5 : "May", 6 : "June", 7 : "July",
                8 : "August", 9 : "September", 10 : "October",
                11 : "November", 12 : "December" }

print "The dictionary items are:"
print monthsDictionary.items()

print "\nThe dictionary keys are:"
print monthsDictionary.keys()

print "\nThe dictionary values are:"
print monthsDictionary.values()

print "\nUsing a for loop to get dictionary items:"

for key in monthsDictionary.keys():
   print "monthsDictionary[", key, "] =", monthsDictionary[ key ]

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
