
# Class Employee with class attribute count.

class Employee:
   """Represents an employee"""
   
   count = 0       # class attribute
   
   def __init__( self, first, last ):
      """Initializes firstName, lastName and increments count"""
      
      self.firstName = first
      self.lastName = last

      Employee.count += 1    # increment class attribute

      print("Employee constructor for %s, %s" \
         % ( self.lastName, self.firstName ))

   def __del__( self ):
      """Decrements count and prints message"""
      
      Employee.count -= 1    # decrement class attribute

      print("Employee destructor for %s, %s" \
         % ( self.lastName, self.firstName ))

