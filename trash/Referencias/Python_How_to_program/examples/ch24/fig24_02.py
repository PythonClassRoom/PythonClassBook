# Fig. 24.2: fig24_02.py
# Demonstrating various GLUT shapes.

from Tkinter import *
import Pmw
from OpenGL.GL import *
from OpenGL.Tk import *
from OpenGL.GLUT import *

class ChooseShape( Frame ):
   """Allow user to preview different shapes and colors"""

   def __init__( self ):
      """Initialize GUI and OpenGL"""

      Frame.__init__( self )
      Pmw.initialise()
      self.master.title( "Choose a shape and color" )
      self.master.geometry( "300x300" )
      self.pack( expand = YES, fill = BOTH )

      # create and pack MenuBar        
      self.choices = Pmw.MenuBar( self )
      self.choices.pack( fill = X )

      # create and pack Opengl -- use double buffering
      self.openGL = Opengl( self, double = 1 )
      self.openGL.pack( expand = YES, fill = BOTH )

      self.openGL.redraw = self.redraw     # set redraw function
      self.openGL.set_eyepoint( 20 )       # move away from object
      self.openGL.autospin_allowed = 1     # allow auto-spin

      self.choices.addmenu( "Shape", None )   # Shape submenu

      # possible shapes and arguments
      self.shapes = { "glutWireCube" : ( 3, ),
                      "glutSolidCube": ( 3, ),
                      "glutWireIcosahedron" : (),
                      "glutSolidIcosahedron" : (),
                      "glutWireCone" : ( 3, 3, 50, 50 ),
                      "glutSolidCone" : ( 3, 3, 50, 50 ),
                      "glutWireTorus" : ( 1, 3, 50, 50 ),
                      "glutSolidTorus" : ( 1, 3, 50, 50 ),
                      "glutWireTeapot" : ( 3, ),
                      "glutSolidTeapot" : ( 3, ) }
      
      self.selectedShape = StringVar()
      self.selectedShape.set( "glutWireCube" )

      sortedShapes = self.shapes.keys()
      sortedShapes.sort()   # sort names before adding to menu

      # add items to Shape menu
      for shape in sortedShapes:
         self.choices.addmenuitem( "Shape", "radiobutton",
            label = shape, variable = self.selectedShape,
            command = self.refresh )

      self.choices.addmenu( "Color", None )   # Color submenu

      # possible colors and their values
      self.colors = { "Black" : ( 0.0, 0.0, 0.0 ),
                      "Blue" : ( 0.0, 0.0, 1.0 ),
                      "Red" : ( 1.0, 0.0, 0.0 ),
                      "Green" : ( 0.0, 1.0, 0.0 ),
                      "Magenta" : ( 1.0, 0.0, 1.0 ) }

      self.selectedColor = StringVar()
      self.selectedColor.set( "Black" )

      # add items to Color menu
      for color in self.colors.keys():
         self.choices.addmenuitem( "Color", "radiobutton",
            label = color, variable = self.selectedColor,
            command = self.refresh )
        
   def redraw( self, openGL ):
      """Draw selected shape on white background"""

      # clear background and disable lighting 
      glClearColor( 1.0, 1.0, 1.0, 0.0 ) # select clearing color
      glClear( GL_COLOR_BUFFER_BIT )     # clear background
      glDisable( GL_LIGHTING )

      # obtain and set selected color   
      color = self.selectedColor.get()        
      apply( glColor3f, self.colors[ color ] )

      # obtain and draw selected shape
      shape = self.selectedShape.get()       
      apply( eval( shape ), self.shapes[ shape ] )

   def refresh( self ):
      self.openGL.tkRedraw()

def main():
   ChooseShape().mainloop()

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
