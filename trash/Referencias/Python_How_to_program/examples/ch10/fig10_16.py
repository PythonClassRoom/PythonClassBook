# Fig. 10.16: fig10_16.py
# Pack layout manager demonstration.

from Tkinter import *

class PackDemo( Frame ):
   """Demonstrate some options of Pack"""

   def __init__( self ):
      """Create four Buttons with different pack options"""
      
      Frame.__init__( self )
      self.master.title( "Packing Demo" )
      self.master.geometry( "400x150" )
      self.pack( expand = YES, fill = BOTH )

      self.button1 = Button( self, text = "Add Button",
         command = self.addButton )

      # Button component placed against top of window
      self.button1.pack( side = TOP )

      self.button2 = Button( self,
         text = "expand = NO, fill = BOTH" )

      # Button component placed against bottom of window
      # fills all available vertical and horizontal space
      self.button2.pack( side = BOTTOM, fill = BOTH )

      self.button3 = Button( self,
         text = "expand = YES, fill = X" )

      # Button component placed against left side of window
      # fills all available horizontal space
      self.button3.pack( side = LEFT, expand = YES, fill = X )

      self.button4 = Button( self,
         text = "expand = YES, fill = Y" )

      # Button component placed against right side of window
      # fills all available vertical space
      self.button4.pack( side = RIGHT, expand = YES, fill = Y )   

   def addButton( self ):
      """Create and pack a new Button"""
      
      Button( self, text = "New Button" ).pack( pady = 5 )
      
def main():
   PackDemo().mainloop()

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
