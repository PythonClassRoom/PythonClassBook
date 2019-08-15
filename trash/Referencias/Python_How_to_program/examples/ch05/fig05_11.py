# Fig. 5.11: fig05_11.py
# Student poll program.

responses = [ 1, 2, 6, 4, 8, 5, 9, 7, 8, 10,
              1, 6, 3, 8, 6, 10, 3, 8, 2, 7,
              6, 5, 7, 6, 8, 6, 7, 5, 6, 6,
              5, 6, 7, 5, 6, 4, 8, 6, 8, 10 ]

print "Rating     Frequency"

for i in range( 1, 11 ):
   print "%6d %13d" % ( i, responses.count( i ) )

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
