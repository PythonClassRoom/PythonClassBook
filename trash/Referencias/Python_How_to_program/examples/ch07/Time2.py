# Fig: 7.7: Time2.py
# Class Time with accessor methods.

class Time:
   """Class Time with accessor methods"""
   
   def __init__( self ):
      """Time constructor initializes each data member to zero"""

      self._hour = 0     # 0-23
      self._minute = 0   # 0-59
      self._second = 0   # 0-59
      
   def setTime( self, hour, minute, second ):
      """Set values of hour, minute, and second"""

      self.setHour( hour )
      self.setMinute( minute )
      self.setSecond( second )

   def setHour( self, hour ):
      """Set hour value"""

      if 0 <= hour < 24:
         self._hour = hour
      else:
         raise ValueError, "Invalid hour value: %d" % hour

   def setMinute( self, minute ):
      """Set minute value"""

      if 0 <= minute < 60:
         self._minute = minute
      else:
         raise ValueError, "Invalid minute value: %d" % minute
   
   def setSecond( self, second ):
      """Set second value"""

      if 0 <= second < 60:
         self._second = second
      else:
         raise ValueError, "Invalid second value: %d" % second

   def getHour( self ):
      """Get hour value"""
      
      return self._hour

   def getMinute( self ):
      """Get minute value"""

      return self._minute

   def getSecond( self ):
      """Get second value"""

      return self._second

   def printMilitary( self ):
      """Prints Time object in military format"""
      
      print "%.2d:%.2d:%.2d" % \
         ( self._hour, self._minute, self._second ),
 
   def printStandard( self ):
      """Prints Time object in standard format"""

      standardTime = ""

      if self._hour == 0 or self._hour == 12:
         standardTime += "12:"
      else:
         standardTime += "%d:" % ( self._hour % 12 )

      standardTime += "%.2d:%.2d" % ( self._minute, self._second )

      if self._hour < 12:
         standardTime += " AM"
      else:
         standardTime += " PM"
      
      print standardTime,

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