# Fig. 10.9: fig10_09.py
# Radiobuttons demonstration.

from Tkinter import *

class RadioFont( Frame ):
   """An area of text with Radiobutton controlled font"""
   
   def __init__( self ):
      """Create an Entry and four Radiobuttons"""
      
      Frame.__init__( self )
      self.pack( expand = YES, fill = BOTH )
      self.master.title( "Radiobutton Demo" ) 

      self.frame1 = Frame( self )
      self.frame1.pack()
      
      self.text = Entry( self.frame1, width = 40,
         font = "Arial 10" )
      self.text.insert( INSERT, "Watch the font style change" )
      self.text.pack( padx = 5, pady = 5 )

      self.frame2 = Frame( self )
      self.frame2.pack()
      
      fontSelections = [ "Plain", "Bold", "Italic",
                         "Bold/Italic" ]
      self.chosenFont = StringVar()

      # initial selection
      self.chosenFont.set( fontSelections[ 0 ] ) 

      # create group of Radiobutton components with same variable
      for style in fontSelections:
         aButton = Radiobutton( self.frame2, text = style,
            variable = self.chosenFont, value = style,
            command = self.changeFont )
         aButton.pack( side = LEFT, padx = 5, pady = 5 )

   def changeFont( self ):
      """Change the font based on selected Radiobutton"""
      
      desiredFont = "Arial 10"

      if self.chosenFont.get() == "Bold":
         desiredFont += " bold"
      elif self.chosenFont.get() == "Italic":
         desiredFont += " italic"
      elif self.chosenFont.get() == "Bold/Italic":
         desiredFont += " bold italic"

      self.text.config( font = desiredFont )

def main():
   RadioFont().mainloop()

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
