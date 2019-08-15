# Fig. 9.5: fig09_05.py
# Overriding base-class methods.

class Employee:
   """Class to represent an employee"""

   def __init__( self, first, last ):
      """Employee constructor takes first and last name"""

      self.firstName = first
      self.lastName = last

   def __str__( self ):
      """String representation of an Employee"""

      return "%s %s" % ( self.firstName, self.lastName )

class HourlyWorker( Employee ):
   """Class to represent an employee paid by hour"""

   def __init__( self, first, last, initHours, initWage ):
      """Constructor for HourlyWorker, takes first and last name,
      initial number of hours and initial wage"""

      Employee.__init__( self, first, last )
      self.hours = float( initHours )
      self.wage = float( initWage )

   def getPay( self ):
      """Calculates HourlyWorker's weekly pay"""

      return self.hours * self.wage

   def __str__( self ):
      """String representation of HourlyWorker"""

      print "HourlyWorker.__str__ is executing"""      

      return "%s is an hourly worker with pay of $%.2f" % \
         ( Employee.__str__( self ), self.getPay() )

# main program
hourly = HourlyWorker( "Bob", "Smith", 40.0, 10.00 )

# invoke __str__ method several ways
print "Calling __str__ several ways..."
print hourly  # invoke __str__ implicitly
print hourly.__str__()  # invoke __str__ explicitly
print HourlyWorker.__str__( hourly )  # explicit, unbound call

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
