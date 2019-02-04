# Fig. 5.10: fig05_10.py
# Appending items to a list.

playList = []     # list of favorite plays

print "Enter your 5 favorite Shakespearean plays.\n"

for i in range( 5 ):
   playName = raw_input( "Play %d: " % ( i + 1 ) )
   playList.append( playName )
   
print "\nSubscript     Value"

for i in range( len( playList ) ):
   print "%9d     %-25s" % ( i + 1, playList[ i ] )

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
