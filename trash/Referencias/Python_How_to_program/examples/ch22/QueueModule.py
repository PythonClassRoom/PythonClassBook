# Fig. 22.11: QueueModule.py
# Class Queue definition.

from ListModule import List

class Queue:
   """Queue composed from linked list"""

   def __init__( self ):
      """Queue constructor"""         

      self._queueList = List()

   def __str__( self ):
      """Queue string representation"""

      return str( self._queueList )
     
   def enqueue( self, element ):
      """Enqueue element"""

      self._queueList.insertAtBack( element )

   def dequeue( self ):
      """Dequeue element"""

      return self._queueList.removeFromFront()

   def isEmpty( self ):
      """Return 1 if Queue is empty"""

      return self._queueList.isEmpty()
   
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
