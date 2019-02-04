# Fig. 3.25: fig03_25.py
# Using the break statement to avoid repeating code
# in the class-average program.

# initialization phase
total = 0          # sum of grades
gradeCounter = 0   # number of grades entered

while 1:
   grade = raw_input( "Enter grade, -1 to end: " )   
   grade = int( grade )

   # exit loop if user inputs -1
   if grade == -1:
      break

   total += grade
   gradeCounter += 1
   
# termination phase
if gradeCounter != 0:
   average = float( total ) / gradeCounter
   print "Class average is", average
else:
   print "No grades were entered"

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
