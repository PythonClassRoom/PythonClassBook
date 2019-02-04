# Fig. 10.11: fig10_11.py
# Mouse events example.

from Tkinter import *

class MouseLocation( Frame ):
   """Demonstrate binding mouse events"""
   
   def __init__( self ):
      """Create a Label, pack it and bind mouse events"""
      
      Frame.__init__( self )
      self.pack( expand = YES, fill = BOTH )
      self.master.title( "Demonstrating Mouse Events" )
      self.master.geometry(  "275x100" )
      
      self.mousePosition = StringVar() # displays mouse position
      self.mousePosition.set( "Mouse outside window" )
      self.positionLabel = Label( self,
         textvariable = self.mousePosition )
      self.positionLabel.pack( side = BOTTOM )

      # bind mouse events to window
      self.bind( "<Button-1>", self.buttonPressed )
      self.bind( "<ButtonRelease-1>", self.buttonReleased )   
      self.bind( "<Enter>", self.enteredWindow )
      self.bind( "<Leave>", self.exitedWindow )
      self.bind( "<B1-Motion>", self.mouseDragged )

   def buttonPressed( self, event ):
      """Display coordinates of button press"""
      
      self.mousePosition.set( "Pressed at [ " + str( event.x ) + 
         ", " + str( event.y ) + " ]" )

   def buttonReleased( self, event ):
      """Display coordinates of button release"""
      
      self.mousePosition.set( "Released at [ " + str( event.x ) + 
         ", " + str( event.y ) + " ]" )

   def enteredWindow( self, event ):
      """Display message that mouse has entered window"""
      
      self.mousePosition.set( "Mouse in window" )

   def exitedWindow( self, event ):
      """Display message that mouse has left window"""
      
      self.mousePosition.set( "Mouse outside window" )

   def mouseDragged( self, event ):
      """Display coordinates of mouse being moved"""
      
      self.mousePosition.set( "Dragged at [ " + str( event.x ) + 
         ", " + str( event.y ) + " ]" )

def main():
   MouseLocation().mainloop()

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
