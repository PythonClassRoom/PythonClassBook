# Fig. 17.30: fig17_30.py
# Inserts into, updates and searches a database.

import MySQLdb
from Tkinter import *
from tkMessageBox import *
import Pmw

class AddressBook( Frame ):
   """GUI Database Address Book Frame"""

   def __init__( self ):
      """Address Book constructor"""
      
      Frame.__init__( self )
      Pmw.initialise()
      self.pack( expand = YES, fill = BOTH )
      self.master.title( "Address Book Database Application" )

      # buttons to execute commands
      self.buttons = Pmw.ButtonBox( self, padx = 0 )
      self.buttons.grid( columnspan = 2 )
      self.buttons.add( "Find", command = self.findAddress )
      self.buttons.add( "Add", command = self.addAddress )
      self.buttons.add( "Update", command = self.updateAddress )
      self.buttons.add( "Clear", command = self.clearContents )
      self.buttons.add( "Help", command = self.help, width = 14 )
      self.buttons.alignbuttons()
      
   
      # list of fields in an address record
      fields = [ "ID", "First name", "Last name", 
        "Address", "City", "State Province", "Postal Code",
        "Country", "Email Address", "Home phone", "Fax Number" ]

      # dictionary with Entry components for values, keyed by
      # corresponding addresses table field names
      self.entries = {}

      self.IDEntry = StringVar()   # current address id text
      self.IDEntry.set( "" )
      
      # create entries for each field
      for i in range( len( fields ) ):
         label = Label( self, text = fields[ i ] + ":" )
         label.grid( row = i + 1, column = 0 )
         entry = Entry( self, name = fields[ i ].lower(),
            font = "Courier 12" )
         entry.grid( row = i + 1 , column = 1,
            sticky = W+E+N+S, padx = 5 )

         # user cannot type in ID field
         if fields[ i ] == "ID":
            entry.config( state = DISABLED,
               textvariable = self.IDEntry, bg = "gray" )
         
         # add entry field to dictionary
         key = fields[ i ].replace( " ", "_" )
         key = key.upper()
         self.entries[ key ] = entry

   def addAddress( self ):
      """Add address record to database"""

      if self.entries[ "LAST_NAME" ].get() != "" and \
         self.entries[ "FIRST_NAME"].get() != "":

         # create INSERT query command
         query = """INSERT INTO addresses (  
                 FIRST_NAME, LAST_NAME, ADDRESS, CITY,
                 STATE_PROVINCE, POSTAL_CODE, COUNTRY,
                 EMAIL_ADDRESS, HOME_PHONE, FAX_NUMBER
                 ) VALUES (""" + \
                 "'%s', " * 10 % \
                 ( self.entries[ "FIRST_NAME" ].get(),
                   self.entries[ "LAST_NAME" ].get(),
                   self.entries[ "ADDRESS" ].get(),
                   self.entries[ "CITY" ].get(),
                   self.entries[ "STATE_PROVINCE" ].get(),
                   self.entries[ "POSTAL_CODE" ].get(),
                   self.entries[ "COUNTRY" ].get(),
                   self.entries[ "EMAIL_ADDRESS" ].get(),
                   self.entries[ "HOME_PHONE" ].get(),
                   self.entries[ "FAX_NUMBER" ].get() )
         query = query[ :-2 ] + ")"

         # open connection, retrieve cursor and execute query
         try:      
            connection = MySQLdb.connect( db = "AddressBook" )
            cursor = connection.cursor()
            cursor.execute( query ) 
         except MySQLdb.OperationalError, message:
            errorMessage = "Error %d:\n%s" % \
               ( message[ 0 ], message[ 1 ] )
            showerror( "Error", errorMessage )
         else:
            cursor.close()
            connection.close()
	    self.clearContents()

      else:   # user has not filled out first/last name fields
         showwarning( "Missing fields", "Please enter name" )

   def findAddress( self ):
      """Query database for address record and display results"""

      if self.entries[ "LAST_NAME" ].get() != "":

         # create SELECT query
         query = "SELECT * FROM addresses " + \
                 "WHERE LAST_NAME = '" + \
                 self.entries[ "LAST_NAME" ].get() + "'"

         # open connection, retrieve cursor and execute query
         try:      
            connection = MySQLdb.connect( db = "AddressBook" )
            cursor = connection.cursor()
            cursor.execute( query )
         except MySQLdb.OperationalError, message:
            errorMessage = "Error %d:\n%s" % \
               ( message[ 0 ], message[ 1 ] )
            showerror( "Error", errorMessage )
            self.clearContents()
         else:   # process results
            results = cursor.fetchall()
            fields = cursor.description

            if not results:   # no results for this person
               showinfo( "Not found", "Nonexistent record" )
            else:             # display person's info. in GUI
               self.clearContents()

               # display results
               for i in range( len( fields ) ):

                  if fields[ i ][ 0 ] == "ID":
                     self.IDEntry.set( str( results[ 0 ][ i ] ) )
                  else:
                     self.entries[ fields[ i ][ 0 ] ].insert( 
                        INSERT, str( results[ 0 ][ i ] ) )
            
            cursor.close()
            connection.close()

      else:   # user did not enter last name
         showwarning( "Missing fields", "Please enter last name" )

   def updateAddress( self ):
      """Update address record in database"""

      if self.entries[ "ID" ].get() != "":

         # create UPDATE query command
         entryItems = self.entries.items()
         query = "UPDATE addresses SET"

         for key, value in entryItems:
            
            if key != "ID":
               query += " %s='%s'," % ( key, value.get() )

         query = query[ :-1 ] + " WHERE ID=" + self.IDEntry.get()

         # open connection, retrieve cursor and execute query
         try:      
            connection = MySQLdb.connect( db = "AddressBook" )
            cursor = connection.cursor()
            cursor.execute( query ) 
         except MySQLdb.OperationalError, message:
            errorMessage = "Error %d:\n%s" % \
               ( message[ 0 ], message[ 1 ] )
            showerror( "Error", errorMessage )
            self.clearContents()
         else:
            showinfo( "database updated", "Database Updated." )
            cursor.close()
            connection.close()
 
      else:   # user has not specified ID
         showwarning( "No ID specified", """
            You may only update an existing record.
            Use Find to locate the record,
            then modify the information and press Update.""" )
             
   def clearContents( self ):
      """Clear GUI panel"""

      for entry in self.entries.values():
         entry.delete( 0, END )

      self.IDEntry.set( "" )         

   def help( self ):
      """Display help message to user"""
      
      showinfo( "Help", """Click Find to locate a record.
         Click Add to insert a new record.
         Click Update to update the information in a record.
         Click Clear to empty the Entry fields.\n""" )

def main():
   AddressBook().mainloop()

if __name__ == "__main__":
   main()

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
