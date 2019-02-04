# Fig. 14.6: fig14_06.py
# Reading and printing a file.

import sys

# open file
try:
   file = open( "clients.dat", "r" )
except IOError:
   print >> sys.stderr, "File could not be opened"
   sys.exit( 1 )
   
records = file.readlines()   # retrieve list of lines in file

print "Account".ljust( 10 ),
print "Name".ljust( 10 ),
print "Balance".rjust( 10 )

for record in records:          # format each line
   fields = record.split()
   print fields[ 0 ].ljust( 10 ),
   print fields[ 1 ].ljust( 10 ),
   print fields[ 2 ].rjust( 10 )

file.close()
 
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
