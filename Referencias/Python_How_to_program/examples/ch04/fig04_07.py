# Fig. 4.7: fig04_07.py
# Roll a six-sided die 6000 times.

import random

frequency1 = 0
frequency2 = 0
frequency3 = 0
frequency4 = 0
frequency5 = 0
frequency6 = 0

for roll in range( 1, 6001 ):       # 6000 die rolls
   face = random.randrange( 1, 7 )

   if face == 1:                    # frequency counted
      frequency1 += 1
   elif face == 2:
      frequency2 += 1
   elif face == 3:
      frequency3 += 1
   elif face == 4:
      frequency4 += 1
   elif face == 5:
      frequency5 += 1
   elif face == 6:
      frequency6 += 1
   else:                            # simple error handling
      print "should never get here!"

print "Face %13s" % "Frequency"
print "   1 %13d" % frequency1
print "   2 %13d" % frequency2
print "   3 %13d" % frequency3
print "   4 %13d" % frequency4
print "   5 %13d" % frequency5
print "   6 %13d" % frequency6
 
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
