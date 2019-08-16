
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

def ttest():

   # obtain phone number from user   
   newNumber = input(
      "Enter phone number in the form (123) 456-7890:\n" )

   phone = PhoneNumber( newNumber )  # create PhoneNumber object
   print("The phone number is:",)
   print(phone)  # invokes phone.__str__()
   
if __name__ == "__main__":
   ttest()
