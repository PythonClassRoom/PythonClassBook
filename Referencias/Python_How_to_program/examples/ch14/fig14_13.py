# Fig. 14.13: fig14_13.py
# Reading and printing pickled object in a file.

import sys, cPickle

# open file
try:
   file = open( "users.dat", "r" )
except IOError:
   print >> sys.stderr, "File could not be opened"
   sys.exit( 1 )
   
records = cPickle.load( file ) # retrieve list of lines in file
file.close()

print "Username".ljust( 15 ),
print "Name".ljust( 10 ),
print "Date of birth".rjust( 20 )

for record in records:          # format each line
   print record[ 0 ].ljust( 15 ),
   print record[ 1 ].ljust( 10 ),
   print record[ 2 ].rjust( 20 )

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
