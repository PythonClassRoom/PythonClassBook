# Fig. 10.4: fig10_04.py
# Label demonstration.

from Tkinter import *

class LabelDemo( Frame ):
   """Demonstrate Labels"""
   
   def __init__( self ):
      """Create three Labels and pack them"""
      
      Frame.__init__( self )   # initializes Frame instance

      # frame fills all available space
      self.pack( expand = YES, fill = BOTH )
      self.master.title( "Labels" )

      self.Label1 = Label( self, text = "Label with text" )

      # resize frame to accommodate Label
      self.Label1.pack()

      self.Label2 = Label( self,
         text = "Labels with text and a bitmap" )

      # insert Label against left side of frame
      self.Label2.pack( side = LEFT )

      # using default bitmap image as label
      self.Label3 = Label( self, bitmap = "warning" )
      self.Label3.pack( side = LEFT )

def main():
   LabelDemo().mainloop()  # starts event loop

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
