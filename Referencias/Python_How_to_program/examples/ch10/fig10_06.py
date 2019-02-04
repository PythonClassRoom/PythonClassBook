# Fig. 10.6: fig10_06.py
# Entry components and event binding demonstration.

from Tkinter import *
from tkMessageBox import *

class EntryDemo( Frame ):
   """Demonstrate Entrys and Event binding"""
   
   def __init__( self ):
      """Create, pack and bind events to four Entrys"""
      
      Frame.__init__( self )
      self.pack( expand = YES, fill = BOTH )
      self.master.title( "Testing Entry Components" )
      self.master.geometry( "325x100" )  # width x length

      self.frame1 = Frame( self )
      self.frame1.pack( pady = 5 )
      
      self.text1 = Entry( self.frame1, name = "text1" )

      # bind the Entry component to event
      self.text1.bind( "<Return>", self.showContents )
      self.text1.pack( side = LEFT, padx = 5 )

      self.text2 = Entry( self.frame1, name = "text2" )

      # insert text into Entry component text2
      self.text2.insert( INSERT, "Enter text here" )
      self.text2.bind( "<Return>", self.showContents )
      self.text2.pack( side = LEFT, padx = 5 )

      self.frame2 = Frame( self )
      self.frame2.pack( pady = 5 )
      
      self.text3 = Entry( self.frame2, name = "text3" )
      self.text3.insert( INSERT, "Uneditable text field" )

      # prohibit user from altering text in Entry component text3
      self.text3.config( state = DISABLED )
      self.text3.bind( "<Return>", self.showContents )
      self.text3.pack( side = LEFT, padx = 5 )

      # text in Entry component text4 appears as *
      self.text4 = Entry( self.frame2, name = "text4", 
                          show = "*" )
      self.text4.insert( INSERT, "Hidden text" )
      self.text4.bind( "<Return>", self.showContents )
      self.text4.pack( side = LEFT, padx = 5 )

   def showContents( self, event ):
      """Display the contents of the Entry"""
      
      # acquire name of Entry component that generated event
      theName = event.widget.winfo_name()

      # acquire contents of Entry component that generated event
      theContents = event.widget.get()
      showinfo( "Message", theName + ": " + theContents )

def main():
   EntryDemo().mainloop()

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
