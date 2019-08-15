# Fig. 8.13: fig08_13.py
# Driver for simple class SingleList.

from NewList import SingleList

def getIntegers():
   size = int( raw_input( "List size: " ) )

   returnList = []  # the list to return

   for i in range( size ):
      returnList.append(
         int( raw_input( "Integer %d: " % ( i + 1 ) ) ) )
      
   return returnList

# input and create integers1 and integers2
print "Creating integers1..."
integers1 = SingleList( getIntegers() )

print "Creating integers2..."
integers2 = SingleList( getIntegers() )

# print integers1 size and contents
print "\nSize of list integers1 is", len( integers1 )
print "List:\n", integers1

# print integers2 size and contents
print "\nSize of list integers2 is", len( integers2 )
print "List:\n", integers2

# use overloaded comparison operator
print "Evaluating: integers1 != integers2"

if integers1 != integers2:
   print "They are not equal"

print "\nEvaluating: integers1 == integers2"

if integers1 == integers2:
   print "They are equal"

print "integers1[ 0 ] is", integers1[ 0 ]
print "Assigning 0 to integers1[ 0 ]"
integers1[ 0 ] = 0
print "integers1:\n", integers1

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
