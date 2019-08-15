# Fig. 25.17: fig25_17.py 
# Subclass of the Page servlet. 

from WebKit.Page import Page
from __future__ import division

class fig25_17( Page ):

   def calculate( self, operand1, operator, operand2 ):
      """ perform calculation """

      if operator == "+":      # addition operation
         result = operand1 + operand2
      elif operator == "-":    # subtraction operation
         result = operand1 - operand2
      elif operator == "*":    # multiplication operation
         result = operand1 * operand2
      elif operator == "/":    # division operation
         result = operand1 / operand2
      elif operator == "//":   # floor division
         result = operand1 // operand2
      else:                    # unrecognizable operator
         result = None
      return result
      
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
