# Fig. 11.4: fig11_04.py
# Popup menu demonstration.

from Tkinter import *

class PopupMenuDemo( Frame ):
   """Demonstrate popup menus"""
   
   def __init__( self ):
      """Create a Menu but do not add it to the Frame"""
      
      Frame.__init__( self )
      self.pack( expand = YES, fill = BOTH )
      self.master.title( "Popup Menu Demo" )
      self.master.geometry( "300x200" )

      # create and pack frame with initial white background
      self.frame1 = Frame( self, bg = "white" )
      self.frame1.pack( expand= YES, fill = BOTH )
      
      # create menu without packing it
      self.menu = Menu( self.frame1, tearoff = 0 )

      colors = [ "White", "Blue", "Yellow", "Red" ]
      self.selectedColor = StringVar()
      self.selectedColor.set( colors[ 0 ] )
      
      for item in colors:
         self.menu.add_radiobutton( label = item,
            variable = self.selectedColor,
            command = self.changeBackgroundColor )

      # popup menu on right-mouse click      
      self.frame1.bind( "<Button-3>", self.popUpMenu )

   def popUpMenu( self, event ):
      """Add the Menu to the Frame"""
      
      self.menu.post( event.x_root, event.y_root )

   def changeBackgroundColor( self ):
      """Change the Frame background color"""
      
      self.frame1.config( bg = self.selectedColor.get() )
      
def main():
   PopupMenuDemo().mainloop()   

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
