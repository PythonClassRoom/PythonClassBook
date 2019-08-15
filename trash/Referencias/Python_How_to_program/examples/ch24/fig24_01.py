# Fig 24.1: fig24_01.py
# Colored, rotating box (with open top and bottom).

from Tkinter import *
from OpenGL.GL import *
from OpenGL.Tk import *

class ColorBox( Frame ):
   """A colorful, rotating box"""

   def __init__( self ):
      """Initialize GUI and OpenGL"""
      
      Frame.__init__( self )
      self.master.title( "Color Box" )
      self.master.geometry( "300x300" )
      self.pack( expand = YES, fill = BOTH )

      # create and pack Opengl -- use double buffering
      self.openGL = Opengl( self, double = 1 )
      self.openGL.pack( expand = YES, fill = BOTH )

      self.openGL.redraw = self.redraw  # set redraw function
      self.openGL.set_eyepoint( 20 )    # move away from object

      self.amountRotated = 0   # total degrees of rotation
      self.increment = 2       # rotate amount in degrees
      self.update()            # begin rotation

   def redraw( self, openGL ):
      """Draw box on black background"""

      # clear background and disable lighting      
      glClearColor( 1.0, 1.0, 1.0, 0.0 )  # set clearing color
      glClear( GL_COLOR_BUFFER_BIT )      # clear background
      glDisable( GL_LIGHTING )         

      # constants   
      red = ( 1.0, 0.0, 0.0 )
      green = ( 0.0, 1.0, 0.0 )
      blue = ( 0.0, 0.0, 1.0 )
      purple = ( 1.0, 0.0, 1.0 )

      vertices = \
         [ ( ( -3.0, 3.0, -3.0 ), red ),
           ( ( -3.0, -3.0, -3.0 ), green ),
           ( ( 3.0, 3.0, -3.0 ), blue ),
           ( ( 3.0, -3.0, -3.0 ), purple ),
           ( ( 3.0, 3.0, 3.0 ), red ),
           ( ( 3.0, -3.0, 3.0 ), green ),
           ( ( -3.0, 3.0, 3.0 ), blue ),
           ( ( -3.0, -3.0, 3.0 ), purple ),
           ( ( -3.0, 3.0, -3.0 ), red ),
           ( ( -3.0, -3.0, -3.0 ), green ) ]
   
      glBegin( GL_QUAD_STRIP )   # begin drawing

      # change color and plot point for each vertex
      for vertex in vertices:
         location, color = vertex
         apply( glColor3f, color )
         apply( glVertex3f, location )

      glEnd()  # stop drawing

   def update( self ):
      """Rotate box"""

      if self.amountRotated >= 500:   # change rotation direction
         self.increment = -2          # rotate left
      elif self.amountRotated <= 0:   # change rotation direction
         self.increment = 2           # rotate right

      # rotate box around x, y, z axis ( 1.0, 1.0, 1.0 )
      glRotate( self.increment, 1.0, 1.0, 1.0 )
      self.amountRotated += self.increment

      self.openGL.tkRedraw()                # redraw geometry
      self.openGL.after( 10, self.update )  # call update in 10ms

def main():
   ColorBox().mainloop()

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
