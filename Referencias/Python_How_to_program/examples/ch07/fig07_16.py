# Fig. 7.16: fig07_16.py
# Demonstrating class attribute access.

from EmployeeWithClassAttribute import Employee

print "Number of employees before instantiation is", \
   Employee.count

# create two Employee objects
employee1 = Employee( "Susan", "Baker" )
employee2 = Employee( "Robert", "Jones" )
employee3 = employee1

print "Number of employees after instantiation is", \
   employee1.count

# explicitly delete employee objects by removing references
del employee1
del employee2
del employee3

print "Number of employees after deletion is", \
   Employee.count

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
