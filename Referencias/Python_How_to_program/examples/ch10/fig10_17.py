# Fig. 10.17: fig10_17.py
# Grid layout manager demonstration.

from Tkinter import *

class GridDemo( Frame ):
   """Demonstrate the Grid geometry manager"""
   
   def __init__( self ):
      """Create and grid several components into the frame"""
      
      Frame.__init__( self )
      self.master.title( "Grid Demo" )

      # main frame fills entire container, expands if necessary
      self.master.rowconfigure( 0, weight = 1 )
      self.master.columnconfigure( 0, weight = 1 )
      self.grid( sticky = W+E+N+S )
	
      self.text1 = Text( self, width = 15, height = 5 )

      # text component spans three rows and all available space
      self.text1.grid( rowspan = 3, sticky = W+E+N+S )
      self.text1.insert( INSERT, "Text1" )

      # place button component in first row, second column
      self.button1 = Button( self, text = "Button 1", 
         width = 25 )
      self.button1.grid( row = 0, column = 1, columnspan = 2,
         sticky = W+E+N+S )

      # place button component in second row, second column 
      self.button2 = Button( self, text = "Button 2" )
      self.button2.grid( row = 1, column = 1, sticky = W+E+N+S )

      # configure button component to fill all it allocated space
      self.button3 = Button( self, text = "Button 3" )
      self.button3.grid( row = 1, column = 2, sticky = W+E+N+S )

      # span two columns starting in second column of first row
      self.button4 = Button( self, text = "Button 4" )
      self.button4.grid( row = 2, column = 1, columnspan = 2,
         sticky = W+E+N+S )

      # place text field in fourth row to span two columns
      self.entry = Entry( self )
      self.entry.grid( row = 3, columnspan = 2, 
         sticky = W+E+N+S )
      self.entry.insert( INSERT, "Entry" )

      # fill all available space in fourth row, third column 
      self.text2 = Text( self, width = 2, height = 2 )
      self.text2.grid( row = 3, column = 2, sticky = W+E+N+S )
      self.text2.insert( INSERT, "Text2" )

      # make second row/column expand
      self.rowconfigure( 1, weight = 1 )
      self.columnconfigure( 1, weight = 1 )

def main():
   GridDemo().mainloop()   

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
