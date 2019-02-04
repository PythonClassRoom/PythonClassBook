# Fig. 11.5: fig11_05.py
# Canvas paint program.

from Tkinter import *

class PaintBox( Frame ):
   """Demonstrate drawing on a Canvas"""
   
   def __init__( self ):
      """Create Canvas and bind paint method to mouse dragging"""
      
      Frame.__init__( self )
      self.pack( expand = YES, fill = BOTH )
      self.master.title( "A simple paint program" )
      self.master.geometry( "300x150" )

      self.message = Label( self, text = "Drag the mouse to draw" )
      self.message.pack( side = BOTTOM )
      
      # create Canvas component
      self.myCanvas = Canvas( self )
      self.myCanvas.pack( expand = YES, fill = BOTH )

      # bind mouse dragging event to Canvas
      self.myCanvas.bind( "<B1-Motion>", self.paint )

   def paint( self, event ):
      """Create an oval of radius 4 around the mouse position"""
      
      x1, y1 = ( event.x - 4 ), ( event.y - 4 )
      x2, y2 = ( event.x + 4 ), ( event.y + 4 )
      self.myCanvas.create_oval( x1, y1, x2, y2, fill = "black" )
   
def main():
   PaintBox().mainloop()

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
