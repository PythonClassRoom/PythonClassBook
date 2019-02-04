# Fig. 22.10: fig22_10.py
# Driver to test class Stack.

from StackModule import Stack

stack = Stack()

print "Processing a Stack"

for i in range( 4 ):
   stack.push( i )
   print "The stack is:", stack

while not stack.isEmpty():
   pop = stack.pop()
   print pop, "popped from stack"
   print "The stack is:", stack
   
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
