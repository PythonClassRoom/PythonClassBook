# Fig. 7.1: Time1.py
# Simple definition of class Time.

class Time:
   """Time abstract data type (ADT) definition"""
   
   def __init__( self ):
      """Initializes hour, minute and second to zero"""

      self.hour = 0     # 0-23
      self.minute = 0   # 0-59
      self.second = 0   # 0-59

   def printMilitary( self ):
      """Prints object of class Time in military format"""
      
      print "%.2d:%.2d:%.2d" % \
         ( self.hour, self.minute, self.second ),
 
   def printStandard( self ):
      """Prints object of class Time in standard format"""

      standardTime = ""

      if self.hour == 0 or self.hour == 12:
         standardTime += "12:"
      else:
         standardTime += "%d:" % ( self.hour % 12 )

      standardTime += "%.2d:%.2d" % ( self.minute, self.second )

      if self.hour < 12:
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
