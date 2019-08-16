
# Demonstrating class attribute access.

from EmployeeWithClassAttribute import Employee

print("Number of employees before instantiation is", \
   Employee.count)

# create two Employee objects
employee1 = Employee( "Susan", "Baker" )
employee2 = Employee( "Robert", "Jones" )
employee3 = employee1

print("Number of employees after instantiation is", \
   employee1.count)

# explicitly delete employee objects by removing references
del employee1
del employee2
del employee3

print("Number of employees after deletion is", \
   Employee.count)


