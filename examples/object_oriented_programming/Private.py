
# Class with private data members.

class PrivateClass:
   """Class that contains public and private data"""

   def __init__( self ):
      """Private class, contains public and private data members"""
      
      self.publicData = "public"      # public data member
      self.__privateData = "private"  # private data member
