# Fig. 3.25: while_example_break.py
# Using the break statement to avoid repeating code
# in the class-average program.

# initialization phase
total = 0          # sum of grades
gradeCounter = 0   # number of grades entered

while 1:
   grade = input( "Enter grade, -1 to end: " )
   grade = int( grade )

   # exit loop if user inputs -1
   if grade == -1:
      break

   total += grade
   gradeCounter += 1
   
# termination phase
if gradeCounter != 0:
   average = float( total ) / gradeCounter
   print("Class average is", average)
else:
   print("No grades were entered")

