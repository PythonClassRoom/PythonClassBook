# Fig. 10.15: fig10_15.py
# Creating a multiple selection list.

from Tkinter import *
import Pmw

class choiceBox( Frame ):
   def __init__( self, listItems ):
      Frame.__init__( self )
      self.pack( expand = YES, fill = BOTH )
      self.master.title( "Select colors" )

      self.listBox = Pmw.ScrolledListBox( self,
                                          items = listItems,
                                          listbox_height = 5,
                                          vscrollmode = "static",
                                          listbox_selectmode = \
                                          EXTENDED )
      self.listBox.pack( side = LEFT, expand = YES, fill = BOTH,
                         padx = 5, pady = 5 )

      self.copyButton = Button( self,
                                text = "Copy >>>", 
                                command = self.addColor )
      self.copyButton.pack( side = LEFT, padx = 5, pady = 5 )

      self.chosen = Pmw.ScrolledText( self,
                                      text_height = 6,
                                      text_width = 20 )
      self.chosen.pack( side = LEFT, expand = YES, fill = BOTH,
                        padx = 5, pady = 5 )

   def addColor( self ):
      self.chosen.clear()
      selected = self.listBox.getcurselection()

      if selected:

         for item in selected:
            self.chosen.insert( END, item + "\n" )

def main():
   colorNames = ( "cyan", "green", "grey", "magenta", \
                  "orange", "pink", "red", "white", "yellow" )
   choiceBox( colorNames ).mainloop()

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
