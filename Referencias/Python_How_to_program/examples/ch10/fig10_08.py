# Fig. 10.8: fig10_08.py
# Checkbuttons demonstration.

from Tkinter import *

class CheckFont( Frame ):
   """An area of text with Checkbutton controlled font"""
   
   def __init__( self ):
      """Create an Entry and two Checkbuttons"""
      
      Frame.__init__( self )
      self.pack( expand = YES, fill = BOTH )
      self.master.title( "Checkbutton Demo" )   
      
      self.frame1 = Frame( self )
      self.frame1.pack()
      
      self.text = Entry( self.frame1, width = 40,
         font = "Arial 10" )
      self.text.insert( INSERT, "Watch the font style change" )
      self.text.pack( padx = 5, pady = 5 )

      self.frame2 = Frame( self )
      self.frame2.pack()
      
      # create boolean variable
      self.boldOn = BooleanVar()

      # create "Bold" checkbutton
      self.checkBold = Checkbutton( self.frame2, text = "Bold", 
         variable = self.boldOn, command = self.changeFont )
      self.checkBold.pack( side = LEFT, padx = 5, pady = 5 )

      # create boolean variable
      self.italicOn = BooleanVar()

      # create "Italic" checkbutton
      self.checkItalic = Checkbutton( self.frame2, 
         text = "Italic", variable = self.italicOn, 
         command = self.changeFont )
      self.checkItalic.pack( side = LEFT, padx = 5, pady = 5 )

   def changeFont( self ):
      """Change the font based on selected Checkbuttons"""
      
      desiredFont = "Arial 10"

      if self.boldOn.get():
         desiredFont += " bold"

      if self.italicOn.get():
         desiredFont += " italic"

      self.text.config( font = desiredFont )

def main():
   CheckFont().mainloop()

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
