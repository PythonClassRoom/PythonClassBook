# Fig. 3.26: for_example_range_continue.py
# Using the continue statement in a for/in structure.

for x in range( 1, 11 ):

   if x == 5:
      continue

   print(x,)

print("\nUsed continue to skip printing the value 5")
