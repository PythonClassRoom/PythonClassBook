# Fig. 11.3: fig11_03.py
# MenuBars with Balloons demonstration.

from Tkinter import *
import Pmw
import sys

class MenuBarDemo( Frame ):
   """Create window with a MenuBar"""
   
   def __init__( self ):
      """Create a MenuBar with items and a Canvas with text"""
      
      Frame.__init__( self )
      Pmw.initialise()
      self.pack( expand = YES, fill = BOTH )
      self.master.title( "MenuBar Demo" )
      self.master.geometry( "500x200" )

      self.myBalloon = Pmw.Balloon( self )
      self.choices = Pmw.MenuBar( self, balloon = self.myBalloon )
      self.choices.pack( fill = X )

      # create File menu and items
      self.choices.addmenu( "File", "Exit" )
      self.choices.addmenuitem( "File", "command", 
         command = self.closeDemo, label = "Exit" )

      # create Format menu and items
      self.choices.addmenu( "Format", "Change font/color" ) 
      self.choices.addcascademenu( "Format", "Color" )
      self.choices.addmenuitem( "Format", "separator" )
      self.choices.addcascademenu( "Format", "Font" )

      # add items to Format/Color menu
      colors = [ "Black", "Blue", "Red", "Green" ]
      self.selectedColor = StringVar()
      self.selectedColor.set( colors[ 0 ] )

      for item in colors:      
         self.choices.addmenuitem( "Color", "radiobutton", 
            label = item, command = self.changeColor,
            variable = self.selectedColor )

      # add items to Format/Font menu
      fonts = [ "Times", "Courier", "Helvetica" ]
      self.selectedFont = StringVar()
      self.selectedFont.set( fonts [ 0 ] )
      
      for item in fonts:
         self.choices.addmenuitem( "Font", "radiobutton",
            label = item, command = self.changeFont,
            variable = self.selectedFont )

      # add a horizontal separator in Font menu
      self.choices.addmenuitem( "Font", "separator" )

      # associate checkbutton menu item with BooleanVar object
      self.boldOn = BooleanVar()
      self.choices.addmenuitem( "Font", "checkbutton",
         label = "Bold", command = self.changeFont,
         variable = self.boldOn )

      # associate checkbutton menu item with BooleanVar object
      self.italicOn = BooleanVar()
      self.choices.addmenuitem( "Font", "checkbutton",
         label = "Italic", command = self.changeFont,
         variable = self.italicOn )      

      # create Canvas with text
      self.display = Canvas( self, bg = "white" )
      self.display.pack( expand = YES, fill = BOTH )

      self.sampleText = self.display.create_text( 250, 100,
         text = "Sample Text", font = "Times 48" )

   def changeColor( self ):
      """Change the color of the text on the Canvas"""
      
      self.display.itemconfig( self.sampleText,
         fill = self.selectedColor.get() )

   def changeFont( self ):
      """Change the font of the text on the Canvas"""
  
      # get selected font and attach size   
      newFont = self.selectedFont.get() + " 48"

      # determine which checkbutton menu items selected
      if self.boldOn.get():
         newFont += " bold"

      if self.italicOn.get():
         newFont += " italic"

      # configure sample text to be displayed in selected style      
      self.display.itemconfig( self.sampleText, font = newFont )

   def closeDemo( self ):
      """Exit the program"""
      
      sys.exit()
      
def main():
   MenuBarDemo().mainloop()   

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
