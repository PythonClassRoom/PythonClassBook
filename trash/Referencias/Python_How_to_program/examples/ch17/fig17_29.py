# Fig. 17.29: fig17_29.py
# Displays results returned by a
# query on Books database.

import MySQLdb
from Tkinter import *
from tkMessageBox import *
import Pmw

class QueryWindow( Frame ):
   """GUI Database Query Frame"""

   def __init__( self ):
      """QueryWindow Constructor"""
      
      Frame.__init__( self )
      Pmw.initialise()
      self.pack( expand = YES, fill = BOTH )
      self.master.title(  
         "Enter Query, Click Submit to See Results." )
      self.master.geometry( "525x525" )

      # scrolled text pane for query string
      self.query = Pmw.ScrolledText( self, text_height = 8 )
      self.query.pack( fill = X )
   
      # button to submit query
      self.submit = Button( self, text = "Submit query",
         command = self.submitQuery )
      self.submit.pack( fill = X )

      # frame to display query results
      self.frame = Pmw.ScrolledFrame( self,
         hscrollmode = "static", vscrollmode = "static" )
      self.frame.pack( expand = YES, fill = BOTH )
      
      self.panes = Pmw.PanedWidget( self.frame.interior(),
         orient = "horizontal" )
      self.panes.pack( expand = YES, fill = BOTH )

   def submitQuery( self ):
      """Execute user-entered query agains database"""

      # open connection, retrieve cursor and execute query
      try:      
         connection = MySQLdb.connect( db = "Books" )
         cursor = connection.cursor()
         cursor.execute( self.query.get() )
      except MySQLdb.OperationalError, message:
         errorMessage = "Error %d:\n%s" % \
            ( message[ 0 ], message[ 1 ] )
         showerror( "Error", errorMessage )
         return
      else:   # obtain user-requested information
         data = cursor.fetchall()
         fields = cursor.description   # metadata from query
         cursor.close()
         connection.close()

      # clear results of last query
      self.panes.destroy()   
      self.panes = Pmw.PanedWidget( self.frame.interior(),
         orient = "horizontal" )
      self.panes.pack( expand = YES, fill = BOTH )

      # create pane and label for each field
      for item in fields:
         self.panes.add( item[ 0 ] )
         label = Label( self.panes.pane( item[ 0 ] ),
            text = item[ 0 ], relief = RAISED )
         label.pack( fill = X )

      # enter results into panes, using labels
      for entry in data:

         for i in range( len( entry ) ):
            label = Label( self.panes.pane( fields[ i ][ 0 ] ),
               text = str( entry[ i ] ), anchor = W,
               relief = GROOVE, bg = "white" )
            label.pack( fill = X )

      self.panes.setnaturalsize()

def main():
   QueryWindow().mainloop()

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
