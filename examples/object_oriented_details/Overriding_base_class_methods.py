
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

      print("HourlyWorker.__str__ is executing""")

      return "%s is an hourly worker with pay of $%.2f" % \
         ( Employee.__str__( self ), self.getPay() )

# main program
hourly = HourlyWorker( "Bob", "Smith", 40.0, 10.00 )

# invoke __str__ method several ways
print("Calling __str__ several ways...")
print(hourly)  # invoke __str__ implicitly
print(hourly.__str__())  # invoke __str__ explicitly
print(HourlyWorker.__str__( hourly ))  # explicit, unbound call

