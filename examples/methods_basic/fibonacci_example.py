
# Recursive fibonacci function.

def fibonacci( n ):

   if n == 0 or n == 1:  # base case
      return n
   else:

      # two recursive calls
      return fibonacci( n - 1 ) + fibonacci( n - 2 )

number = int( input( "Enter an integer: " ) )

if number > 0:
   result = fibonacci( number )
   print("Fibonacci(%d) = %d" % ( number, result ))
else:
   print("Cannot find the fibonacci of a negative number")

