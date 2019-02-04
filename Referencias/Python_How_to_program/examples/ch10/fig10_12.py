# Fig. 10.12: fig10_12.py
# Mouse button differentiation.

from Tkinter import *

class MouseDetails( Frame ):
   """Demonstrate mouse events for different buttons"""
   
   def __init__( self ):
      """Create a Label, pack it and bind mouse events"""
      
      Frame.__init__( self )
      self.pack( expand = YES, fill = BOTH )
      self.master.title( "Mouse clicks and buttons" )
      self.master.geometry( "350x150" )

      # create mousePosition variable
      self.mousePosition = StringVar()
      positionLabel = Label( self,
         textvariable = self.mousePosition )
      self.mousePosition.set( "Mouse not clicked" )
      positionLabel.pack( side = BOTTOM )

      # bind event handler to events for each mouse button
      self.bind( "<Button-1>", self.leftClick )
      self.bind( "<Button-2>", self.centerClick )
      self.bind( "<Button-3>", self.rightClick )

   def leftClick( self, event ):
      """Display coordinates and indicate left button clicked"""
      
      self.showPosition( event.x, event.y )
      self.master.title( "Clicked with left mouse button" )

   def centerClick( self, event ):
      """Display coordinates and indicate center button used"""
      
      self.showPosition( event.x, event.y )
      self.master.title( "Clicked with center mouse button" )

   def rightClick( self, event ):
      """Display coordinates and indicate right button clicked"""
      
      self.showPosition( event.x, event.y )
      self.master.title( "Clicked with right mouse button" )

   def showPosition( self, x, y ):
      """Display coordinates of button press"""
      
      self.mousePosition.set( "Pressed at [ " + str( x ) + ", " +
         str( y ) + " ]" )     

def main():
   MouseDetails().mainloop()

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
