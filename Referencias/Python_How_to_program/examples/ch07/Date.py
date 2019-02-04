# Fig. 7.17: Date.py
# Definition of class Date.

class Date:
   """Class that represents dates"""

   # class attribute lists number of days in each month
   daysPerMonth = [
      0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

   def __init__( self, month, day, year ):
      """Constructor for class Date"""
        
      if 0 < month <= 12:   # validate month
         self.month = month
      else:
         raise ValueError, "Invalid value for month: %d" % month

      if year >= 0:         # validate year
         self.year = year
      else:
         raise ValueError, "Invalid value for year: %y" % year
      
      self.day = self.checkDay( day )   # validate day

      print "Date constructor:",
      self.display()

   def __del__( self ):
      """Prints message when called"""
        
      print "Date object about to be destroyed:",
      self.display()

   def display( self ):
      """Prints Date information"""

      print "%d/%d/%d" % ( self.month, self.day, self.year )

   def checkDay( self, testDay ):
      """Validates day of the month"""
    
      # validate day, test for leap year
      if 0 < testDay <= Date.daysPerMonth[ self.month ]:
         return testDay
      elif self.month == 2 and testDay == 29 and \
         ( self.year % 400 == 0 or
           self.year % 100 != 0 and self.year % 4 == 0 ):
         return testDay
      else:
         raise ValueError, "Invalid day: %d for month: %d" % \
            ( testDay, self.month )

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
