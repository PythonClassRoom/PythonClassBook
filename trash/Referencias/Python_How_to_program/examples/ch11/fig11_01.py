# Fig. 11.1: fig11_01.py
# ScrolledListBox to select image.

from Tkinter import *
import Pmw

class ImageSelection( Frame ):
   """List of available images and an area to display them"""
   
   def __init__( self, images ):
      """Create list of PhotoImages and Label to display them"""
      
      Frame.__init__( self )
      Pmw.initialise()
      self.pack( expand = YES, fill = BOTH )
      self.master.title( "Select an image" )

      self.photos = []

      # add PhotoImage objects to list photos
      for item in images:
         self.photos.append( PhotoImage( file = item ) ) 

      # create scrolled list box with vertical scrollbar
      self.listBox = Pmw.ScrolledListBox( self, items = images,
         listbox_height = 3, vscrollmode = "static",
         selectioncommand = self.switchImage )
      self.listBox.pack( side = LEFT, expand = YES, fill = BOTH,
         padx = 5, pady = 5 )

      self.display = Label( self, image = self.photos[ 0 ] )
      self.display.pack( padx = 5, pady = 5 )

   def switchImage( self ):
      """Change image in Label to current selection"""
      
      chosenPicture = self.listBox.curselection()

      if chosenPicture:
         choice = int( chosenPicture[ 0 ] )
         self.display.config( image = self.photos[ choice ] )

def main():
   images = [ "bug1.gif", "bug2.gif",
              "travelbug.gif", "buganim.gif" ]
   ImageSelection( images ).mainloop()   

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
