
# Recursive factorial function.

# Recursive definition of function factorial
def factorial( number ):

   if number <= 1:   # base case
      return 1
   else:
      return number * factorial( number - 1 )  # recursive call

for i in range( 11 ):
   print("%2d! = %d" % ( i, factorial( i ) ))
 
