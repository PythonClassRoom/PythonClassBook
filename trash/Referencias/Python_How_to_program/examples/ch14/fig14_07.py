# Fig. 14.7: fig14_07.py
# Credit inquiry program.

import sys

# retrieve one user command
def getRequest():
   
   while 1:
      request = int( raw_input( "\n? " ) )
     
      if 1 <= request <= 4:
         break

   return request

# determine if balance should be displayed, based on type 
def shouldDisplay( accountType, balance ):

   if accountType == 2 and balance < 0:     # credit balance
      return 1

   elif accountType == 3 and balance > 0:   # debit balance
      return 1

   elif accountType == 1 and balance == 0:  # zero balance 
      return 1

   else: return 0

# print formatted balance data
def outputLine( account, name, balance ):
   
   print account.ljust( 10 ),
   print name.ljust( 10 ),
   print balance.rjust( 10 )

# open file
try:
   file = open( "clients.dat", "r" )
except IOError:
   print >> sys.stderr, "File could not be opened"
   sys.exit( 1 ) 

print "Enter request"
print "1 - List accounts with zero balances"
print "2 - List accounts with credit balances"
print "3 - List accounts with debit balances"
print "4 - End of run"

# process user request(s)
while 1:

   request = getRequest()   # get user request

   if request == 1:         # zero balances
      print "\nAccounts with zero balances:"
   elif request == 2:       # credit balances
      print "\nAccounts with credit balances:"
   elif request == 3:       # debit balances
      print "\nAccounts with debit balances:"
   elif request == 4:       # exit loop
      break
   else:  # getRequest should never let program reach here
      print "\nInvalid request."

   currentRecord = file.readline()    # get first record

   # process each line
   while ( currentRecord != "" ):
      account, name, balance = currentRecord.split()
      balance = float( balance )
      
      if shouldDisplay( request, balance ):
         outputLine( account, name, str( balance ) )

      currentRecord = file.readline() # get next record

   file.seek( 0, 0 )                  # move to beginning of file
  
print "\nEnd of run."
file.close()                          # close file

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
