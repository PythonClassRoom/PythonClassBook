# Fig. 14.9: fig14_09.py
# Writing to shelve file.

import sys
import shelve

# open shelve file
try:
   outCredit = shelve.open( "credit.dat" )
except IOError:
   print >> sys.stderr, "File could not be opened"
   sys.exit( 1 )

print "Enter account number (1 to 100, 0 to end input)"

# get account information
while 1:

   # get account information
   accountNumber = int( raw_input( 
         "\nEnter account number\n? " ) )
       
   if 0 < accountNumber <= 100:
      
      print "Enter lastname, firstname, balance"
      currentData = raw_input( "? " )

      outCredit[ str( accountNumber ) ] = currentData.split()

   elif accountNumber == 0:
      break

outCredit.close()   # close shelve file
 
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
