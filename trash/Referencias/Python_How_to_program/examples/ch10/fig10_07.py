# Fig. 10.7: fig10_07.py
# Button demonstration.

from Tkinter import *
from tkMessageBox import *

class PlainAndFancy( Frame ):
   """Create one plain and one fancy button"""
   
   def __init__( self ):
      """Create two buttons, pack them and bind events"""
      
      Frame.__init__( self )
      self.pack( expand = YES, fill = BOTH )
      self.master.title( "Buttons" )

      # create button with text
      self.plainButton = Button( self, text = "Plain Button",
         command = self.pressedPlain )
      self.plainButton.bind( "<Enter>", self.rolloverEnter )
      self.plainButton.bind( "<Leave>", self.rolloverLeave )
      self.plainButton.pack( side = LEFT, padx = 5, pady = 5 )

      # create button with image
      self.myImage = PhotoImage( file = "logotiny.gif" )
      self.fancyButton = Button( self, image = self.myImage,
         command = self.pressedFancy )
      self.fancyButton.bind( "<Enter>", self.rolloverEnter )
      self.fancyButton.bind( "<Leave>", self.rolloverLeave )
      self.fancyButton.pack( side = LEFT, padx = 5, pady = 5 )

   def pressedPlain( self ):
      showinfo( "Message", "You pressed: Plain Button" )

   def pressedFancy( self ):
      showinfo( "Message", "You pressed: Fancy Button" )

   def rolloverEnter( self, event ):
      event.widget.config( relief = GROOVE )

   def rolloverLeave( self, event ):
      event.widget.config( relief = RAISED )

def main():
   PlainAndFancy().mainloop()

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
