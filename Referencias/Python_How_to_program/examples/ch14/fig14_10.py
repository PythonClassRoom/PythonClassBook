# Fig. 14.9: fig14_09.py
# Reading a shelve file. 

import sys
import shelve

# print formatted credit data
def outputLine( account, aList ):
   
   print account.ljust( 10 ),
   print aList[ 0 ].ljust( 10 ),
   print aList[ 1 ].ljust( 10 ),
   print aList[ 2 ].rjust( 10 )

# open shelve file
try:
   creditFile = shelve.open( "credit.dat" )
except IOError:
   print >> sys.stderr, "File could not be opened"
   sys.exit( 1 )

print "Account".ljust( 10 ),
print "Last Name".ljust( 10 ),
print "First Name".ljust( 10 ),
print "Balance".rjust( 10 )

# display each account
for accountNumber in creditFile.keys():
   outputLine( accountNumber, creditFile[ accountNumber ] )

creditFile.close()   # close shelve file
 
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
