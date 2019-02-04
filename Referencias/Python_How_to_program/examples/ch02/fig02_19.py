# Fig. 2.19: fig02_19.py
# String formatting.

integerValue = 4237
print "Integer ", integerValue
print "Decimal integer %d" % integerValue 
print "Hexadecimal integer %x\n" % integerValue

floatValue = 123456.789
print "Float", floatValue
print "Default float %f" % floatValue
print "Default exponential %e\n" % floatValue

print "Right justify integer (%8d)" % integerValue
print "Left justify integer  (%-8d)\n" % integerValue

stringValue = "String formatting"
print "Force eight digits in integer %.8d" % integerValue
print "Five digits after decimal in float %.5f" % floatValue
print "Fifteen and five characters allowed in string:"
print "(%.15s) (%.5s)" % ( stringValue, stringValue )

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
