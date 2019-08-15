# Fig. 7.14: fig07_14.py
# Demonstrating default constructor method for class Time.

from Time3 import Time

def printTimeValues( timeToPrint ):
    timeToPrint.printMilitary()
    print
    timeToPrint.printStandard()
    print

time1 = Time()             # all default 
time2 = Time( 2 )          # minute, second default
time3 = Time( 21, 34 )     # second default
time4 = Time( 12, 25, 42 ) # all specified

print "Constructed with:"

print "\nall arguments defaulted:"
printTimeValues( time1 )

print "\nhour specified; minute and second defaulted:"
printTimeValues( time2 )

print "\nhour and minute specified; second defaulted:"
printTimeValues( time3 )

print "\nhour, minute and second specified:"
printTimeValues( time4 )

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
