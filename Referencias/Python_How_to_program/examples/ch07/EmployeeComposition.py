# Fig. 7.18: EmployeeComposition.py
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

      print "Employee constructor: %s, %s" \
         % ( self.lastName, self.firstName )

   def __del__( self ):
      """Called before Employee destruction"""
        
      print "Employee object about to be destroyed: %s, %s" \
         % ( self.lastName, self.firstName )

   def display( self ):
      """Prints employee information"""
       
      print "%s, %s" % ( self.lastName, self.firstName )
      print "Hired:",
      self.hireDate.display()
      print "Birth date:",
      self.birthDate.display()

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
