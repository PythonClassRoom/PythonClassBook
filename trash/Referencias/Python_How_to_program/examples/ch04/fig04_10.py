# Fig. 4.10: fig04_10.py
# Scoping example.

x = 1 # global variable

# alters the local variable x, shadows the global variable
def a():  
   x = 25

   print "\nlocal x in a is", x, "after entering a"
   x += 1
   print "local x in a is", x, "before exiting a"

# alters the global variable x
def b():
   global x

   print "\nglobal x is", x, "on entering b"
   x *= 10
   print "global x is", x, "on exiting b"

print "global x is", x

x = 7
print "global x is", x

a()
b()
a()
b()

print "\nglobal x is", x
 
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
