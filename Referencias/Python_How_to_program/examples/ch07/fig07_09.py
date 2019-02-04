# Fig. 7.9: fig07_09.py
# Driver to test class TimeControl.

from Time2 import Time

time1 = Time()

# print initial time
print "The initial military time is",
time1.printMilitary()
print "\nThe initial standard time is",
time1.printStandard()

# change time
time1.setTime( 13, 27, 6 )
print "\n\nMilitary time after setTime is",
time1.printMilitary()
print "\nStandard time after setTime is",
time1.printStandard()

time1.setHour( 4 )
time1.setMinute( 3 )
time1.setSecond( 34 )
print "\n\nMilitary time after setHour, setMinute, setSecond is",
time1.printMilitary()
print "\nStandard time after setHour, setMinute, setSecond is",
time1.printStandard()


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
