# Fig. 14.11: fig14_11.py
# Reads shelve file, updates data
# already written to file, creates data
# to be placed in file and deletes data
# already in file.

import sys
import shelve

# prompt for input menu choice
def enterChoice():
   
   print "\nEnter your choice"
   print "1 - store a formatted text file of accounts"
   print "    called \"print.txt\" for printing"
   print "2 - update an account"
   print "3 - add a new account"
   print "4 - delete an account"
   print "5 - end program"
   
   while 1:
      menuChoice = int( raw_input( "? " ) )
  
      if not 1 <= menuChoice <= 5:
         print >> sys.stderr, "Incorrect choice"

      else:
         break
      
   return menuChoice
   
# create formatted text file for printing
def textFile( readFromFile ):
   
   # open text file
   try:
      outputFile = open( "print.txt", "w" )
   except IOError:
      print >> sys.stderr, "File could not be opened."
      sys.exit( 1 )

   print >> outputFile, "Account".ljust( 10 ),
   print >> outputFile, "Last Name".ljust( 10 ),
   print >> outputFile, "First Name".ljust( 10 ),
   print >> outputFile, "Balance".rjust( 10 )

   # print shelve values to text file
   for key in readFromFile.keys():
      print >> outputFile, key.ljust( 10 ),
      print >> outputFile, readFromFile[ key ][ 0 ].ljust( 10 ),
      print >> outputFile, readFromFile[ key ][ 1 ].ljust( 10 ),
      print >> outputFile, readFromFile[ key ][ 2 ].rjust( 10 )

   outputFile.close()

# update account balance
def updateRecord( updateFile ):
   
   account = getAccount( "Enter account to update" )

   if updateFile.has_key( account ):
      outputLine( account, updateFile[ account ] ) # get record

      transaction = raw_input(
         "\nEnter charge (+) or payment (-): " )

      # create temporary record to alter data
      tempRecord = updateFile[ account ]
      tempBalance = float( tempRecord[ 2 ] )
      tempBalance += float( transaction )
      tempBalance = "%.2f" % tempBalance
      tempRecord[ 2 ] = tempBalance

      # update record in shelve
      del updateFile[ account ]   # remove old record first
      updateFile[ account ] = tempRecord
      outputLine( account, updateFile[ account ] )
   else:
      print >> sys.stderr, "Account #", account, \
         "does not exist."

# create and insert new record
def newRecord( insertInFile ):
   
   account = getAccount( "Enter new account number" )

   if not insertInFile.has_key( account ):
      print "Enter lastname, firstname, balance"
      currentData = raw_input( "? " )
      insertInFile[ account ] = currentData.split()
   else:
      print >> sys.stderr, "Account #", account, "exists."

# delete existing record
def deleteRecord( deleteFromFile ):
   
   account = getAccount( "Enter account to delete" )

   if deleteFromFile.has_key( account ):
      del deleteFromFile[ account ]
      print "Account #", account, "deleted."
   else:
      print >> sys.stderr, "Account #", account, \
         "does not exist."
      

# output line of client information
def outputLine( account, record ):
   
   print account.ljust( 10 ),
   print record[ 0 ].ljust( 10 ),
   print record[ 1 ].ljust( 10 ),
   print record[ 2 ].rjust( 10 )

# get account number from keyboard
def getAccount( prompt ):
   
   while 1:
      account = raw_input( prompt + " (1 - 100): " )
   
      if 1 <= int( account ) <= 100:
         break 

   return account 

# list of functions that correspond to user options
options = [ textFile, updateRecord, newRecord, deleteRecord ] 

# open shelve file
try:
   creditFile = shelve.open( "credit.dat" )
except IOError:
   print >> sys.stderr, "File could not be opened."
   sys.exit( 1 )
 
# process user commands
while 1:

   choice = enterChoice()               # get user menu choice

   if choice == 5:
      break

   options[ choice - 1 ]( creditFile )  # invoke option function
   
creditFile.close()                      # close shelve file


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
