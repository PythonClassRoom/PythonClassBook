# Fig. 5.16: fig05_16.py
# Passing lists and individual list elements to functions.

def modifyList( aList ):

   for i in range( len( aList ) ):
      aList[ i ] *= 2

def modifyElement( element ):
   element *= 2

aList = [ 1, 2, 3, 4, 5 ]

print "Effects of passing entire list:"
print "The values of the original list are:"

for item in aList:
   print item,

modifyList( aList )

print "\n\nThe values of the modified list are:"

for item in aList:
   print item,

print "\n\nEffects of passing list element:"
print "aList[ 3 ] before modifyElement:", aList[ 3 ]
modifyElement( aList[ 3 ] )
print "aList[ 3 ] after modifyElement:", aList[ 3 ]

print "\nEffects of passing slices of list:"
print "aList[ 2:4 ] before modifyList:", aList[ 2:4 ]
modifyList( aList[ 2:4 ] )
print "aList[ 2:4 ] after modifyList:", aList[ 2:4 ]


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
