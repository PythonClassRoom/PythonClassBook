# Fig. 22.15: TreeModule.py
# Treenode and Tree definition.

class Treenode:
   """Single Node in a Tree"""

   def __init__( self, data ):
      """Treenode constructor"""

      self._left = None
      self._data = data
      self._right = None

   def __str__( self ):
      """Tree string representation"""

      return str( self._data )      

class Tree:
   """Binary search tree"""

   def __init__( self ):
      """Tree Constructor"""
      
      self._rootNode = None
        
   def insertNode( self, value ):
      """Insert node into tree"""

      if self._rootNode is None:  # tree is empty
         self._rootNode = Treenode( value )
      else:  # tree is not empty
         self.insertNodeHelper( self._rootNode, value )

   def insertNodeHelper( self, node, value ):
      """Recursive helper method"""

      if value < node._data:  # insert to left

         if node._left is None:
            node._left = Treenode( value )
         else:
            self.insertNodeHelper ( node._left, value )

      elif value > node._data:
            
         if node._right is None:  # insert to right
            node._right = Treenode( value )
         else:
            self.insertNodeHelper( node._right, value )

      else:  # duplicate node
         print value, "duplicate"

   def preOrderTraversal( self ):
      """Preorder traversal"""
      
      self.preOrderHelper( self._rootNode )

   def preOrderHelper( self, node ):
      """Preorder traversal helper function"""

      if node is not None:
         print node,
         self.preOrderHelper( node._left )
         self.preOrderHelper( node._right )

   def inOrderTraversal( self ):
      """Inorder traversal"""

      self.inOrderHelper( self._rootNode )

   def inOrderHelper( self, node ):
      """Inorder traversal helper function"""

      if node is not None:
         self.inOrderHelper( node._left )
         print node,
         self.inOrderHelper( node._right )

   def postOrderTraversal( self ):
      """Postorder traversal"""

      self.postOrderHelper( self._rootNode )

   def postOrderHelper( self, node ):
      """Postorder traversal helper function"""

      if node is not None:
         self.postOrderHelper( node._left )
         self.postOrderHelper( node._right )
         print node,
         
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
