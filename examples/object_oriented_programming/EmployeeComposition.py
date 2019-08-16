
# Definition of Employee class with composite members.

from Date import Date

class Employee:
   """Employee class with Date attributes"""

   def __init__( self, firstName, lastName, birthMonth,
      birthDay, birthYear, hireMonth, hireDay, hireYear ):
      """Constructor for class Employee"""
       
      self.birthDate = Date( birthMonth, birthDay, birthYear )
      self.hireDate = Date( hireMonth, hireDay, hireYear )

      self.lastName = lastName
      self.firstName = firstName

      print("Employee constructor: %s, %s" \
         % ( self.lastName, self.firstName ))

   def __del__( self ):
      """Called before Employee destruction"""
        
      print("Employee object about to be destroyed: %s, %s" \
         % ( self.lastName, self.firstName ))

   def display( self ):
      """Prints employee information"""
       
      print("%s, %s" % ( self.lastName, self.firstName ))
      print("Hired:", self.hireDate.display())
      print("Birth date:", self.birthDate.display())

