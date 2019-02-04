# Fig. 5.20: fig05_20.py
# Making tables using lists of lists and tuples of tuples.

table1 = [ [ 1, 2, 3 ], [ 4, 5, 6 ] ]
table2 = ( ( 1, 2 ), ( 3, ), ( 4, 5, 6 ) )

print "Values in table1 by row are"

for row in table1:

   for item in row:
      print item,

   print

print "\nValues in table2 by row are"

for row in table2:

   for item in row:
      print item,

   print

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
