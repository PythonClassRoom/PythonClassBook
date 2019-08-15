# Fig. 11.7: fig11_07.py
# Scale used to control the size of a circle.

from Tkinter import *

class ScaleDemo( Frame ):
   """Demonstrate Canvas and Scale"""
   
   def __init__( self ):
      """Create a Canvas with a circle controlled by a Scale"""
      
      Frame.__init__( self )
      self.pack( expand = YES, fill = BOTH )
      self.master.title( "Scale Demo" )
      self.master.geometry( "220x270" )

      # create Scale
      self.control = Scale( self, from_ = 0, to = 200,
         orient = HORIZONTAL, command = self.updateCircle )
      self.control.pack( side = BOTTOM, fill = X )
      self.control.set( 10 )

      # create Canvas and draw circle
      self.display = Canvas( self, bg = "white" )
      self.display.pack( expand = YES, fill = BOTH )

   def updateCircle( self, scaleValue ):
      """Delete the circle, determine new size, draw again"""
      
      end = int( scaleValue ) + 10
      self.display.delete( "circle" )
      self.display.create_oval( 10, 10, end, end,
         fill = "red", tags = "circle" )

def main():
   ScaleDemo().mainloop()   

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
