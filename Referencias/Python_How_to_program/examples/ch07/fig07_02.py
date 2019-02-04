# Fig. 7.2: fig07_02.py
# Creating and manipulating objects of class Time.

from Time1 import Time  # import class definition from file

time1 = Time()  # create object of class Time

# access object's attributes
print "The attributes of time1 are: "
print "time1.hour:", time1.hour
print "time1.minute:", time1.minute
print "time1.second:", time1.second

# access object's methods
print "\nCalling method printMilitary:",
time1.printMilitary()

print "\nCalling method printStandard:",
time1.printStandard()

# change value of object's attributes
print "\n\nChanging time1's hour attribute..."
time1.hour = 25
print "Calling method printMilitary after alteration:",
time1.printMilitary()

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
