# Fig. 14.3: fig14_03.py
# Opening and writing to a file.

import sys

# open file
try:
   file = open( "clients.dat", "w" )  # open file in write mode
except IOError, message:              # file open failed
   print >> sys.stderr, "File could not be opened:", message
   sys.exit( 1 )

print "Enter the account, name and balance."
print "Enter end-of-file to end input."

while 1:

   try:
      accountLine = raw_input( "? " )   # get account entry
   except EOFError:
      break                             # user entered EOF
   else:
      print >> file, accountLine        # write entry to file
      
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
