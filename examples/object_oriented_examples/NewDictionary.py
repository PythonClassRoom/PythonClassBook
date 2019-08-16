
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
   
