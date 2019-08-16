
# Random integers produced by randrange.

import random

for i in range( 1, 21 ):  # simulates 20 die rolls
   print("%10d" % ( random.randrange( 1, 7 ) ),)
   
   if i % 5 == 0:  # print newline every 5 rolls
      print()
 
