
# Class average program with sentinel-controlled repetiton.

# initialization phase
total = 0          # sum of grades
gradeCounter = 0   # number of grades entered

# processing phase
grade = input( "Enter grade, -1 to end: " )   # get one grade
grade = int( grade )   # convert string to an integer

while grade != -1:
   total = total + grade
   gradeCounter = gradeCounter + 1
   grade = input( "Enter grade, -1 to end: " )
   grade = int( grade )

# termination phase
if gradeCounter != 0:
   average = float( total ) / gradeCounter
   print("Class average is", average)
else:
   print("No grades were entered")

