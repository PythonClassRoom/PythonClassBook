# Fig: 8.3: TimeAccess.py
# Class Time with customized attribute access.

class Time:
   """Class Time with customized attribute access"""
   
   def __init__( self, hour = 0, minute = 0, second = 0 ):
      """Time constructor initializes each data member to zero"""

      # each statement invokes __setattr__
      self.hour = hour
      self.minute = minute
      self.second = second
      
   def __setattr__( self, name, value ):
      """Assigns a value to an attribute"""

      if name == "hour":

         if 0 <= value < 24:
            self.__dict__[ "_hour" ] = value
         else:
            raise ValueError, "Invalid hour value: %d" % value

      elif name == "minute" or name == "second":

         if 0 <= value < 60:
            self.__dict__[ "_" + name ] = value
         else:
            raise ValueError, "Invalid %s value: %d" % \
               ( name, value )

      else:
         self.__dict__[ name ] = value

   def __getattr__( self, name ):
      """Performs lookup for unrecognized attribute name"""

      if name == "hour":
         return self._hour
      elif name == "minute":
         return self._minute
      elif name == "second":
         return self._second
      else:
         raise AttributeError, name
 
   def __str__( self ):
      """Returns Time object string in military format"""

      # attribute access does not call __getattr__      
      return "%.2d:%.2d:%.2d" % \
         ( self._hour, self._minute, self._second )
 
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
