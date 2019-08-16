
# Making tables using lists of lists and tuples of tuples.

table1 = [ [ 1, 2, 3 ], [ 4, 5, 6 ] ]
table2 = ( ( 1, 2 ), ( 3, ), ( 4, 5, 6 ) )

print("Values in table1 by row are")

for row in table1:

   for item in row:
      print(item,)

   print()

print("\nValues in table2 by row are")

for row in table2:

   for item in row:
      print(item,)

   print()

