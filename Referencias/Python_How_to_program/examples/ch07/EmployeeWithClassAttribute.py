# Fig. 7.15: EmployeeWithClassAttribute.py
# Class Employee with class attribute count.

class Employee:
   """Represents an employee"""
   
   count = 0       # class attribute
   
   def __init__( self, first, last ):
      """Initializes firstName, lastName and increments count"""
      
      self.firstName = first
      self.lastName = last

      Employee.count += 1    # increment class attribute

      print "Employee constructor for %s, %s" \
         % ( self.lastName, self.firstName )

   def __del__( self ):
      """Decrements count and prints message"""
      
      Employee.count -= 1    # decrement class attribute

      print "Employee destructor for %s, %s" \
         % ( self.lastName, self.firstName )

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
