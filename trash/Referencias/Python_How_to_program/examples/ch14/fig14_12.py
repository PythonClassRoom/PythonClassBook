# Fig. 14.11: fig14_11.py
# Opening and writing pickled object to a file.

import sys, cPickle

# open file
try:
   file = open( "users.dat", "w" )    # open file in write mode
except IOError, message:              # file open failed
   print >> sys.stderr, "File could not be opened:", message
   sys.exit( 1 )

print "Enter the user name, name and date of birth."
print "Enter end-of-file to end input."

inputList = []

while 1:

   try:
      accountLine = raw_input( "? " )         # get user entry
   except EOFError:
      break                                   # user-entered EOF
   else:
      inputList.append( accountLine.split() ) # append entry

cPickle.dump( inputList, file )  # write pickled object to file

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
