
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
         raise ValueError("Invalid value for month: %d" % month)

      if year >= 0:         # validate year
         self.year = year
      else:
         raise ValueError("Invalid value for year: %y" % year)
      
      self.day = self.checkDay( day )   # validate day

      print("Date constructor:",)
      self.display()

   def __del__( self ):
      """Prints message when called"""
        
      print("Date object about to be destroyed:",)
      self.display()

   def display( self ):
      """Prints Date information"""

      print("%d/%d/%d" % ( self.month, self.day, self.year ))

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
         raise ValueError("Invalid day: %d for month: %d" % \
                          (testDay, self.month))
