# Fig: 7.13: Time3.py
# Class Time with default constructor.

class Time:
   """Class Time with default constructor"""
   
   def __init__( self, hour = 0, minute = 0, second = 0 ):
      """Time constructor initializes each data member to zero"""

      self.setTime( hour, minute, second )
      
   def setTime( self, hour, minute, second ):
      """Set values of hour, minute, and second"""

      self.setHour( hour )
      self.setMinute( minute )
      self.setSecond( second )

   def setHour( self, hour ):
      """Set hour value"""

      if 0 <= hour < 24:
         self.__hour = hour
      else:
         raise ValueError, "Invalid hour value: %d" % hour

   def setMinute( self, minute ):
      """Set minute value"""

      if 0 <= minute < 60:
         self.__minute = minute
      else:
         raise ValueError, "Invalid minute value: %d" % minute
   
   def setSecond( self, second ):
      """Set second value"""

      if 0 <= second < 60:
         self.__second = second
      else:
         raise ValueError, "Invalid second value: %d" % second

   def getHour( self ):
      """Get hour value"""
      
      return self.__hour

   def getMinute( self ):
      """Get minute value"""

      return self.__minute

   def getSecond( self ):
      """Get second value"""

      return self.__second

   def printMilitary( self ):
      """Prints Time object in military format"""
      
      print "%.2d:%.2d:%.2d" % \
         ( self.__hour, self.__minute, self.__second ),
 
   def printStandard( self ):
      """Prints Time object in standard format"""

      standardTime = ""

      if self.__hour == 0 or self.__hour == 12:
         standardTime += "12:"
      else:
         standardTime += "%d:" % ( self.__hour % 12 )

      standardTime += "%.2d:%.2d" % ( self.__minute, self.__second )

      if self.__hour < 12:
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
