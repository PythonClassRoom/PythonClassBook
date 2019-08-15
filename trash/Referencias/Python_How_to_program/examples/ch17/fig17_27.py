#!/usr/local/bin/python
# Fig. 17.27: fig17_27.py
# Displays contents of the Authors table,
# ordered by a specified field.

import MySQLdb
import cgi
import sys

def printHeader( title ):
   print """Content-type: text/html

<?xml version = "1.0" encoding = "UTF-8"?>    
<!DOCTYPE html PUBLIC
   "-//W3C//DTD XHTML 1.0 Transitional//EN"
   "DTD/xhtml1-transitional.dtd">
<html xmlns = "http://www.w3.org/1999/xhtml"
   xml:lang = "en" lang = "en">
<head><title>%s</title></head>

<body>""" % title

# obtain user query specifications
form = cgi.FieldStorage()

# get "sortBy" value
if form.has_key( "sortBy" ):
   sortBy = form[ "sortBy" ].value
else:
   sortBy = "firstName"

# get "sortOrder" value
if form.has_key( "sortOrder" ):
   sortOrder = form[ "sortOrder" ].value
else:
   sortOrder = "ASC"

printHeader( "Authors table from Books" )

# connect to database and retrieve a cursor
try:
   connection = MySQLdb.connect( db = "Books", user = "liperi",
      passwd = "liperi" )
# error connecting to database
except MySQLdb.OperationalError, error:
   print "Error:", error
   sys.exit( 1 )

# retrieve cursor
else:
   cursor = connection.cursor()
   
# query all records from Authors table
cursor.execute( "SELECT * FROM Authors ORDER BY %s %s" %
   ( sortBy, sortOrder ) )

allFields = cursor.description  # get field names
allRecords = cursor.fetchall()  # get records

# close cursor and connection
cursor.close()
connection.close()

# output results in a table
print """\n<table border = "1" cellpadding = "3" >
      <tr bgcolor = "silver" >"""

# create table header
for field in allFields:
   print "<td>%s</td>" % field[ 0 ]

print "</tr>"

# display each record as a row
for author in allRecords:
   print "<tr>"

   for item in author:
      print "<td>%s</td>" % item

   print "</tr>"

print "</table>"

# obtain sorting method from user
print """
      \n<form method = "post" action = "/cgi-bin/fig17_27.py">
      Sort By:<br />"""

# display sorting options
for field in allFields:
   print """<input type = "radio" name = "sortBy"
      value = "%s" />""" % field[ 0 ]
   print field[ 0 ]
   print "<br />"

print """<br />\nSort Order:<br />
      <input type = "radio" name = "sortOrder"
      value = "ASC" checked = "checked" />
      Ascending
      <input type = "radio" name = "sortOrder"
      value = "DESC" />
      Descending
      <br /><br />\n<input type = "submit" value = "SORT" />
      </form>\n\n</body>\n</html>"""
 
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
