# Fig. 9.17: TimeProperty.py
# Class Time with properties

class Time( object ):
   """Class Time with hour, minute and second properties"""

   def __init__( self, hourValue, minuteValue, secondValue ):
      """Time constructor, takes hour, minute and second"""

      self.__hour = hourValue
      self.__minute = minuteValue
      self.__second = secondValue

   def __str__( self ):
      """String representation of an object of class Time"""

      return "%.2d:%.2d:%.2d" % \
         ( self.__hour, self.__minute, self.__second ) 

   def deleteValue( self ):
      """Delete method for Time properties"""

      raise TypeError, "Cannot delete attribute"

   def setHour( self, value ):
      """Set method for hour attribute"""

      if 0 <= value < 24:
         self.__hour = value
      else:
         raise ValueError, \
            "hour (%d) must be in range 0-23, inclusive" % value

   def getHour( self ):
      """Get method for hour attribute"""

      return self.__hour

   # create hour property
   hour = property( getHour, setHour, deleteValue, "hour" )   

   def setMinute( self, value ):
      """Set method for minute attribute"""

      if 0 <= value < 60:
         self.__minute = value
      else:
         raise ValueError, \
            "minute (%d) must be in range 0-59, inclusive" % value

   def getMinute( self ):
      """Get method for minute attribute"""

      return self.__minute       

   # create minute property
   minute = property( getMinute, setMinute, deleteValue, "minute" )

   def setSecond( self, value ):
      """Set method for second attribute"""

      if 0 <= value < 60:
         self.__second = value
      else:
         raise ValueError, \
            "second (%d) must be in range 0-59, inclusive" % value

   def getSecond( self ):
      """Get method for second attribute"""

      return self.__second

   # create second property
   second = property( getSecond, setSecond, deleteValue, "second" )

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