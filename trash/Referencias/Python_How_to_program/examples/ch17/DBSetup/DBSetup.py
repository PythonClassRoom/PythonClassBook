#!/usr/local/bin/python

copyright = \
"""
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
"""

import cPickle
import os
import sys
import getpass

# try to import MySQLdb
try:
   import MySQLdb
except ImportError:
   sys.exit( "Module MySQLdb is not installed or is not in the Python module search path" )

def user_loop( instructions, options ):

   optionNumbers = options.keys()
   optionNumbers.sort()

   while 1:
      print "\n", instructions

      # display available options
      for optionNumber in optionNumbers:
         print "%d) %s" % ( optionNumber, options[optionNumber][0] )

      # retrieve user's choice
      try:
         choice = int( raw_input( "\n? " ) )
      except ValueError:
         print "ERROR: Please enter an integer menu choice"
         continue

      # attempt to execute menu command
      try:
         commandEntry = options[ choice ]
      except KeyError:
         print "ERROR: Invalid menu choice\n"
         continue
      else:
         commandEntry[1]()

def retrieveDatabaseDefinition( name ):

   try:
      file = open( name + ".def" )
   except IOError, error:
      sys.exit( "Unable to open file: %s" % error )

   results = {}

   results[ "name" ] = file.readline().strip()
   results[ "createfile" ] = file.readline().strip()

   if not (results["name"] and results["createfile"]):
      raise TypeError

   results[ "tables" ] = {}   

   while 1:

      currentLine = file.readline()

      if not currentLine:
         break
      else:
         tableName, tableFile = currentLine.split()
         results[ "tables" ][ tableName ] = tableFile

   return results     

def getSQLStatementsFromFile( filename ):
   file = open( filename )
   data = file.read()
   statements = filter( lambda x: x, [statement.strip() for statement in data.split( ";" ) ] )
   return statements

def buildDatabase( databaseName ):

   username = raw_input( "Enter MySQL user name: " )
   password = getpass.getpass( "Enter user password: " )

   print "Creating database %s:" % databaseName

   # retrieve database description from file
   print "\tRetrieving database definition:",

   try:
      databaseDefinition = retrieveDatabaseDefinition( databaseName )
   except TypeError:
      sys.exit( "ERROR\nThe database definition in %s.def is invalid" % databaseName )
   else:
      print "DONE"

   # get a cursor for MySQL
   print "\tConnecting to MySQL:",
   try:
      cursor = MySQLdb.connect( user = username, passwd = password ).cursor()
   except MySQLdb.OperationalError, error:
      sys.exit( "ERROR\nCould not connect to MySQL (%s)" % error )
   else:
      print "DONE"

   dbName = databaseDefinition["name"]

   cursor.execute( "show databases" )
   allDatabases = [record[0] for record in cursor.fetchall()]

   # drop database, if it exists and recreate
   if dbName in allDatabases:
      cursor.execute( "DROP DATABASE %s" % dbName )

   cursor.execute( "CREATE DATABASE %s" % dbName )

   # create new database tables
   print "\tRetrieving table definitions:",
   dbSQLFile = databaseDefinition[ "createfile" ]
   
   try:
      statements = getSQLStatementsFromFile( dbSQLFile )
   except IOError, error:
      sys.exit( "ERROR\nCould not read SQL file %s (%s)" % ( dbSQLFile, error ) )
   else:
      print "DONE"
   
   # execute statements to create database
   print "\tCreating database:",
   cursor.execute( "USE %s" % dbName )
   errorHappened = 0  # true if an error occurs

   for statement in statements:

      try:
         cursor.execute( statement )
      except MySQLdb.OperationalError, error:

         errorHappened += 1

         if errorHappened == 1:
            print "ERROR"

         sys.stderr.write( "\tError executing SQL\n\t%s" % error )

   # warn user if an error occured
   if errorHappened:
      print "\nAn error occured while creating the database. Database may not have been created."
   else:
      print "DONE"
      
   cursor.close()

   # connect to new database
   print "\tAttempting to connect to new database:", 
   try:
      newDBCursor = MySQLdb.connect( db = databaseName, user = username, passwd = password ).cursor()
   except MySQLdb.OperationalError, error:
      sys.exit( "\nCould not connect to database %s (%s)" % ( databaseName, error ) )
   else:
      print "DONE"

   # populate tables
   loadStatement = 'LOAD DATA LOCAL INFILE "%s" INTO TABLE %s'
   errorHappened = 0  # true if an error occurs

   for tableName, tableFilename in databaseDefinition[ "tables" ].items():
      print "\t\tCreating table %s from %s: " % ( tableName, tableFilename ),

      try:      
         newDBCursor.execute( loadStatement % ( tableFilename, tableName ) )
      except MySQLdb.OperationalError, error:
         errorHappened += 1

         if errorHappened == 1:         
            print "ERROR"

         print "\t\t", error

      if not errorHappened:
         print "DONE"

   cursor.close()
   
def createDatabases():
   databases = [ filename[:-4] for filename in os.listdir(os.getcwd()) if filename.endswith(".def") ]

   options = {}
   numberOfDatabases = 1

   for database in databases:
      options[ numberOfDatabases ] = \
         ( database, lambda db = database: buildDatabase( db ) )  # < 2.2 has no nested scopes
      numberOfDatabases += 1

   options[ numberOfDatabases ] = ( "<QUIT>", sys.exit )      

   user_loop( "Select a database to create", options )      
     
if __name__ == "__main__":
   print copyright
   createDatabases()
