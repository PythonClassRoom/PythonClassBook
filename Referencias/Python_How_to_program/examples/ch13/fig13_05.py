# Fig. 13.5: fig13_05.py
# Searching strings for a substring.

# counting the occurrences of a substring
string1 = "Test1, test2, test3, test4, Test5, test6"

print '"test" occurs %d times in \n\t%s' % \
   ( string1.count( "test" ), string1 )
print '"test" occurs %d times after 18th character in \n\t%s' % \
   ( string1.count( "test", 18, len( string1 ) ), string1 )
print

# finding a substring in a string
string2 = "Odd or even"

print '"%s" contains "or" starting at index %d' % \
   ( string2, string2.find( "or" ) )

# find index of "even"
try:
   print '"even" index is', string2.index( "even" )
except ValueError:
   print '"even" does not occur in "%s"' % string2

if string2.startswith( "Odd" ):
   print '"%s" starts with "Odd"' % string2

if string2.endswith( "even" ):
   print '"%s" ends with "even"\n' % string2

# searching from end of string 
print 'Index from end of "test" in "%s" is %d' \
   % ( string1, string1.rfind( "test" ) )
print

# find rindex of "Test"
try:
   print 'First occurrence of "Test" from end at index', \
      string1.rindex( "Test" )
except ValueError:
   print '"Test" does not occur in "%s"' % string1

print

# replacing a substring
string3 = "One, one, one, one, one, one"

print "Original:", string3
print 'Replaced "one" with "two":', \
   string3.replace( "one", "two" )
print "Replaced 3 maximum:", string3.replace( "one", "two", 3 )

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
