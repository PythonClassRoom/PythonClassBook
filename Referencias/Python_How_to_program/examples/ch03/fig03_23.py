# Fig. 3.23: fig03_23.py
# Calculating compound interest.

principal = 1000.0   # starting principal
rate = .05           # interest rate

print "Year %21s" % "Amount on deposit"

for year in range( 1, 11 ):
   amount = principal * ( 1.0 + rate ) ** year
   print "%4d%21.2f" % ( year, amount )

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
