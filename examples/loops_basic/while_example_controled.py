# Fig. 3.15: while_example_controled.py
# Analysis of examination results.

# initialize variables
passes = 0                  # number of passes
failures = 0                # number of failures
studentCounter = 1          # student counter

# process 10 students; counter-controlled loop
while studentCounter <= 10:
   result = input( "Enter result (1=pass,2=fail): " )
   result = int( result )   # one exam result

   if result == 1:
      passes = passes + 1
   else:
      failures = failures + 1

   studentCounter = studentCounter + 1

# termination phase
print("Passed", passes)
print("Failed", failures)

if passes > 8:
   print("Raise tuition")

