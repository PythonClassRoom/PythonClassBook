
# Class that defines method __getattribute__

class DemonstrateAccess( object ):
   """Class to demonstrate when method __getattribute__ executes"""

   def __init__( self ):
      """DemonstrateAccess constructor, initializes attribute
      value"""

      self.value = 1
      
   def __getattribute__( self, name ):
      """Executes for every attribute access"""

      print("__getattribute__ executing...")
      print("\tClient attempt to access attribute:", name)

      return object.__getattribute__( self, name )

   def __getattr__( self, name ):
      """Executes when client access attribute not in __dict__"""

      print("__getattr__ executing...")
      print("\tClient attempt to access non-existent attribute:",\
         name)

      raise AttributeError("Object has no attribute %s" \
                           % name)
