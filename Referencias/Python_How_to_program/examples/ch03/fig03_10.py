# Fig. 3.10: fig03_10.py
# Class average program with counter-controlled repetition.

# initialization phase
total = 0         # sum of grades
gradeCounter = 1  # number of grades entered

# processing phase
while gradeCounter <= 10:               # loop 10 times
   grade = raw_input( "Enter grade: " ) # get one grade
   grade = int( grade )   # convert string to an integer
   total = total + grade
   gradeCounter = gradeCounter + 1

# termination phase
average = total / 10                    # integer division
print "Class average is", average

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
