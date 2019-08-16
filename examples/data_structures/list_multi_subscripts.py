
# Double-subscripted list example.


def printGrades( grades ):
   students = len( grades )     # number of students
   exams = len( grades[ 0 ] )   # number of exams

   # print table headers
   print("The list is:")
   print("          ",)

   for i in range( exams ):
      print("[%d]" % i,)

   print()

   # print scores, by row
   for i in range( students ):
      print("grades[%d]  " % i,)

      for j in range( exams ):
         print(grades[ i ][ j ], "",)

      print()


def minimum( grades ):
   lowScore = 100

   for studentExams in grades:     # loop over students

      for score in studentExams:   # loop over scores

         if score < lowScore:
            lowScore = score

   return lowScore   


def maximum( grades ):
   highScore = 0

   for studentExams in grades:     # loop over students

      for score in studentExams:   # loop over scores

         if score > highScore:
            highScore = score

   return highScore


def average( setOfGrades ):
   total = 0.0

   for grade in setOfGrades:       # loop over student's scores
      total += grade

   return total / len( setOfGrades )


# main program
grades = [ [ 77, 68, 86, 73 ],
           [ 96, 87, 89, 81 ],
           [ 70, 90, 86, 81 ] ]

printGrades( grades )
print("\n\nLowest grade:", minimum( grades ))
print("Highest grade:", maximum( grades ))
print("\n")

# print average for each student
for i in range( len( grades ) ):
   print("Average for student", i, "is", average( grades[ i ] ))

