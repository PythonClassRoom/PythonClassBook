# Fig. 10.14: fig10_14.py
# Binding keys to keyboard events.

from Tkinter import *

class KeyDemo( Frame ):
   """Demonstrates keystroke events"""
   
   def __init__( self ):
      """Create two Labels and bind keystroke events"""
      
      Frame.__init__( self )
      self.pack( expand = YES, fill = BOTH )
      self.master.title( "Demonstrating Keystroke Events" )
      self.master.geometry( "350x50" )

      self.message1 = StringVar()
      self.line1 = Label( self, textvariable = self.message1 )
      self.message1.set( "Type any key or shift" )
      self.line1.pack()

      self.message2 = StringVar()
      self.line2 = Label( self, textvariable = self.message2 )
      self.message2.set( "" )
      self.line2.pack()

      # binding any key
      self.master.bind( "<KeyPress>", self.keyPressed )
      self.master.bind( "<KeyRelease>", self.keyReleased )

      # binding specific key
      self.master.bind( "<KeyPress-Shift_L>", self.shiftPressed )
      self.master.bind( "<KeyRelease-Shift_L>",
         self.shiftReleased )

   def keyPressed( self, event ):
      """Display the name of the pressed key"""
      
      self.message1.set( "Key pressed: " + event.char )
      self.message2.set( "This key is not left shift" )

   def keyReleased( self, event ):
      """Display the name of the released key"""
      
      self.message1.set( "Key released: " + event.char )
      self.message2.set( "This key is not left shift" )
   
   def shiftPressed( self, event ):
      """Display a message that left shift was pressed"""
      
      self.message1.set( "Shift pressed" )
      self.message2.set( "This key is left shift" )

   def shiftReleased( self, event ):
      """Display a message that left shift was released"""
      
      self.message1.set( "Shift released" )
      self.message2.set( "This key is left shift" )
   
def main():
   KeyDemo().mainloop()

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
