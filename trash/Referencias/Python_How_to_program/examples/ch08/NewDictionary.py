# Fig. 8.15: NewDictionary.py
# Definition of class SimpleDictionary.

class SimpleDictionary:
   """Class to make an instance behave like a dictionary"""

   # mapping special methods
   def __getitem__( self, key ):
      """Overloaded key-value access"""
      
      return self.__dict__[ key ]

   def __setitem__( self, key, value ):
      """Overloaded key-value assignment/creation"""
      
      self.__dict__[ key ] = value

   def __delitem__( self, key ):
      """Overloaded key-value deletion"""

      del self.__dict__[ key ]      

   def __str__( self ):
      """Overloaded string representation"""
      
      return str( self.__dict__ )

   # common mapping methods
   def keys( self ):
      """Returns list of keys in dictionary"""
      
      return self.__dict__.keys()

   def values( self ):
      """Returns list of values in dictionary"""
      
      return self.__dict__.values()

   def items( self ):
      """Returns list of items in dictionary"""
      
      return self.__dict__.items()
   
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
