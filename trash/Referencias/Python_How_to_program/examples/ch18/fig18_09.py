# Fig. 18.9: fig18_09.py
# Demonstrating popen and popen2.

import os

# determine operating system, then set directory-listing and
# reverse-sort commands
if os.name == "nt" or os.name == "dos":  # Windows system
   fileList = "dir /B"
   sortReverse = "sort /R"
elif os.name == "posix":  # UNIX-compatible system
   fileList = "ls -1"
   sortReverse = "sort -r"
else:
   sys.exit( "OS not supported by this program." )

# obtain stdout of directory-listing command
dirOut = os.popen( fileList, "r" )

# obtain stdin, stdout of reverse-sort command
sortIn, sortOut = os.popen2( sortReverse )

filenames = dirOut.read()  # output from directory-listing command

# display output from directory-listing command
print "Before sending to sort"
print "(Output from ’%s’):" % fileList
print filenames

sortIn.write( filenames )  # send to stdin of sort command

dirOut.close()  # close stdout of directory-listing command 
sortIn.close()  # close stdin of sort command -- sends EOF

# display output from sort command
print "After sending to sort"
print "(Output from ’%s’):" % sortReverse
print sortOut.read()  # output from sort command

sortOut.close()  # close stdout of sort command
 
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
