# Fig. 22.3: ListModule.py
# Classes List and Node definitions.

class Node:
   """Single node in a data structure"""

   def __init__( self, data ):
      """Node constructor"""
      
      self._data = data
      self._nextNode = None
    
   def __str__( self ):
      """Node data representation"""

      return str( self._data )      

class List:
   """Linked list"""

   def __init__( self ):
      """List constructor"""

      self._firstNode = None
      self._lastNode = None

   def __str__( self ):
      """List string representation"""

      if self.isEmpty():
         return "empty"

      currentNode = self._firstNode
      output = []

      while currentNode is not None:
         output.append( str( currentNode._data ) )
         currentNode = currentNode._nextNode

      return " ".join( output )      

   def insertAtFront( self, value ):
      """Insert node at front of list"""

      newNode = Node( value )

      if self.isEmpty():  # List is empty
         self._firstNode = self._lastNode = newNode
      else:   # List is not empty
         newNode._nextNode = self._firstNode
         self._firstNode = newNode
        
   def insertAtBack( self, value ):
      """Insert node at back of list"""

      newNode = Node( value )

      if self.isEmpty():  # List is empty
         self._firstNode = self._lastNode = newNode
      else:  # List is not empty
         self._lastNode._nextNode =  newNode
         self._lastNode = newNode

   def removeFromFront( self ):
      """Delete node from front of list"""

      if self.isEmpty():  # raise exception on empty list
         raise IndexError, "remove from empty list"

      tempNode = self._firstNode

      if self._firstNode is self._lastNode:  # one node in list
         self._firstNode = self._lastNode = None
      else:
         self._firstNode = self._firstNode._nextNode

      return tempNode

   def removeFromBack( self ):
      """Delete node from back of list"""

      if self.isEmpty():  # raise exception on empty list
         raise IndexError, "remove from empty list"
     
      tempNode = self._lastNode

      if self._firstNode is self._lastNode:  # one node in list
         self._firstNode = self._lastNode = None
      else:
         currentNode = self._firstNode

         # locate second-to-last node
         while currentNode._nextNode is not self._lastNode:
               currentNode = currentNode._nextNode
               
         currentNode._nextNode = None
         self._lastNode = currentNode

      return tempNode
    
   def isEmpty( self ):
      """Returns true if List is empty"""

      return self._firstNode is None

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
