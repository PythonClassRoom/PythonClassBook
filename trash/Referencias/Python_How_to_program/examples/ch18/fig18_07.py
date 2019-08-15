# Fig. 18.7: fig18_07.py
# Opens a Web page in a system-specific editor.

import os
import sys
import urllib

if len( sys.argv ) != 3:
   sys.exit( "Incorrect number of arguments." )

# determine operating system and set editor command
if os.name == "nt" or os.name == "dos":
   editor = "notepad.exe"
elif os.name == "posix":
   editor = "vi"
else:
   sys.exit( "Unsupported OS" )

# obtain Web page and store in file
urllib.urlretrieve( sys.argv[ 1 ], sys.argv[ 2 ] )

# editor expects to receive itself as an argument
os.execvp( editor, ( editor, sys.argv[ 2 ] ) )

print "This line never executes."
 
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
