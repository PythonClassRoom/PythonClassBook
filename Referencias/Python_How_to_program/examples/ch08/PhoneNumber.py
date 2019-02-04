# Fig. 8.1: PhoneNumber.py
# Representation of phone number in USA format: (xxx) xxx-xxxx.

class PhoneNumber:
   """Simple class to represent phone number in USA format"""
   
   def __init__( self, number ):
      """Accepts string in form (xxx) xxx-xxxx"""
      
      self.areaCode = number[ 1:4 ]  # 3-digit area code
      self.exchange = number[ 6:9 ]  # 3-digit exchange
      self.line = number[ 10:14 ]  # 4-digit line

   def __str__( self ):
      """Informal string representation"""
      
      return "(%s) %s-%s" % \
         ( self.areaCode, self.exchange, self.line )

def test():

   # obtain phone number from user   
   newNumber = raw_input(
      "Enter phone number in the form (123) 456-7890:\n" )

   phone = PhoneNumber( newNumber )  # create PhoneNumber object
   print "The phone number is:",
   print phone  # invokes phone.__str__()
   
if __name__ == "__main__":
   test()

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
