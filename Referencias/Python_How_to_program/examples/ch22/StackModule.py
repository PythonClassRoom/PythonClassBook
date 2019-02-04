# Fig. 22.9: StackModule.py
# Class Stack definition.

from ListModule import List

class Stack ( List ):
   """Stack composed from linked list"""

   def __init__( self ):
      """Stack constructor"""

      self._stackList = List()

   def __str__( self ):
      """Stack string representation"""

      return str( self._stackList )

   def push( self, element ):
      """Push data onto stack"""
      
      self._stackList.insertAtFront( element )

   def pop( self ):
      """Pop data from stack"""

      return self._stackList.removeFromFront()
   
   def isEmpty( self ):
      """Return 1 if Stack is empty"""

      return self._stackList.isEmpty()

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
