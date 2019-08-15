# Fig. 18.5: fig18_05.py
# Uses the system function to clear the screen.

import os
import sys

def printInstructions( clearCommand ):
   os.system( clearCommand )  # clear display

   print """Type the text that you wish to save in this file.
Type clear on a blank line to delete the contents of the file.
Type quit on a blank line when you are finished.\n"""

# determine operating system
if os.name == "nt" or os.name == "dos":  # Windows system
   clearCommand = "cls"
   print "You are using a Windows system."
elif os.name == "posix":  # UNIX-compatible system
   clearCommand = "clear"
   print "You are using a UNIX-compatible system."
else:
   sys.exit( "Unsupported OS" )

filename = raw_input( "What file would you like to create? " )

# open file
try:
   file = open( filename, "w+" )
except IOError, message:
   sys.exit( "Error creating file: %s" % message )

printInstructions( clearCommand )
currentLine = ""

# write input to file
while currentLine != "quit\n":
   file.write( currentLine )
   currentLine = sys.stdin.readline()

   if currentLine == "clear\n":

      # seek to beginning and truncate file
      file.seek( 0, 0 )
      file.truncate()

      currentLine = ""
      printInstructions( clearCommand )

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
