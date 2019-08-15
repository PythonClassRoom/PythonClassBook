# Fig. 5.5: fig05_05.py
# Creating a histogram from a list of values.

values = []   # a list of values

# input 10 values from user
print "Enter 10 integers:"

for i in range( 10 ):
   newValue = int( raw_input( "Enter integer %d: " % ( i + 1 ) ) )
   values += [ newValue ]

# create histogram
print "\nCreating a histogram from values:"
print "%s %10s %10s" % ( "Element", "Value", "Histogram" )

for i in range( len( values ) ):
   print "%7d %10d  %s" % ( i, values[ i ], "*" * values[ i ] )

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
