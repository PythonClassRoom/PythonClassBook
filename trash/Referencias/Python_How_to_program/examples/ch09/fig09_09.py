# Fig 9.9: fig09_09.py
# Creating a class hierarchy with an abstract base class.

class Employee:
   """Abstract base class Employee"""

   def __init__( self, first, last ):
      """Employee constructor, takes first name and last name.
      NOTE: Cannot create object of class Employee."""

      if self.__class__ == Employee:
         raise NotImplementedError, \
            "Cannot create object of class Employee"

      self.firstName = first
      self.lastName = last

   def __str__( self ):
      """String representation of Employee"""

      return "%s %s" % ( self.firstName, self.lastName )

   def _checkPositive( self, value ):
      """Utility method to ensure a value is positive"""

      if value < 0:
         raise ValueError, \
            "Attribute value (%s) must be positive" % value
      else:
         return value

   def earnings( self ):
      """Abstract method; derived classes must override"""

      raise NotImplementedError, "Cannot call abstract method"

class Boss( Employee ):
   """Boss class, inherits from Employee"""

   def __init__( self, first, last, salary ):
      """Boss constructor, takes first and last names and salary"""

      Employee.__init__( self, first, last )
      self.weeklySalary = self._checkPositive( float( salary ) )

   def earnings( self ):
      """Compute the Boss's pay"""

      return self.weeklySalary

   def __str__( self ):
      """String representation of Boss"""

      return "%17s: %s" % ( "Boss", Employee.__str__( self ) )

class CommissionWorker( Employee ):
   """CommissionWorker class, inherits from Employee"""

   def __init__( self, first, last, salary, commission, quantity ):
      """CommissionWorker constructor, takes first and last names,
      salary, commission and quantity"""

      Employee.__init__( self, first, last )
      self.salary = self._checkPositive( float( salary ) )
      self.commission = self._checkPositive( float( commission ) )
      self.quantity = self._checkPositive( quantity )

   def earnings( self ):
      """Compute the CommissionWorker's pay"""

      return self.salary + self.commission * self.quantity

   def __str__( self ):
      """String representation of CommissionWorker"""

      return "%17s: %s" % ( "Commission Worker",
         Employee.__str__( self ) )

class PieceWorker( Employee ):
   """PieceWorker class, inherits from Employee"""

   def __init__( self, first, last, wage, quantity ):
      """PieceWorker constructor, takes first and last names, wage
      per piece and quantity"""

      Employee.__init__( self, first, last )
      self.wagePerPiece = self._checkPositive( float( wage ) )
      self.quantity = self._checkPositive( quantity )

   def earnings( self ):
      """Compute PieceWorker's pay"""

      return self.quantity * self.wagePerPiece

   def __str__( self ):
      """String representation of PieceWorker"""

      return "%17s: %s" % ( "Piece Worker",
         Employee.__str__( self) )

class HourlyWorker( Employee ):
   """HourlyWorker class, inherits from Employee"""

   def __init__( self, first, last, wage, hours ):
      """HourlyWorker constructor, takes first and last names,
      wage per hour and hours worked"""

      Employee.__init__( self, first, last )
      self.wage = self._checkPositive( float( wage ) )
      self.hours = self._checkPositive( float( hours ) )

   def earnings( self ):
      """Compute HourlyWorker's pay"""

      if self.hours <= 40:
         return self.wage * self.hours
      else:
         return 40 * self.wage + ( self.hours - 40 ) *\
           self.wage * 1.5

   def __str__( self ):
      """String representation of HourlyWorker"""

      return "%17s: %s" % ( "Hourly Worker",
         Employee.__str__( self ) )

# main program

# create list of Employees
employees = [ Boss( "John", "Smith", 800.00 ),
              CommissionWorker( "Sue", "Jones", 200.0, 3.0, 150 ),
              PieceWorker( "Bob", "Lewis", 2.5, 200 ),
              HourlyWorker( "Karen", "Price", 13.75, 40 ) ]

# print Employee and compute earnings
for employee in employees:
   print "%s earned $%.2f" % ( employee, employee.earnings() )

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
