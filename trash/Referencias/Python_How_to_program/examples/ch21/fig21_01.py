# Fig. 21.01: fig21_01.py
# Demonstrating crypto system.

from Tkinter import *
import rotor
import string

class Crypto( Frame ):
   """Demonstrate the cryptosystem"""
   
   def __init__( self ):
      """Create and grid several components into the frame"""
      
      Frame.__init__( self )
      self.grid( sticky = W+E+N+S )
      self.master.title( "Python Encryption and Decryption" )
      self.master.rowconfigure( 0, weight = 1 )
      self.master.columnconfigure( 0, weight = 1 )

      self.button1 = Button( self, text = "Encrypt", 
         width = 15, command = self.encrypt )

      # specify position of Button component button1
      self.button1.grid( row = 0, column = 1, sticky = W+E+N+S )

      self.button2 = Button( self, text = "Decrypt",
         width = 15, command = self.decrypt )
      self.button2.grid( row = 0, column = 2, sticky = W+E+N+S )

      self.text1 = Text( self, width = 30, height = 15 )

      # text component spans three rows and all available space
      self.text1.grid( row = 3, column = 1, columnspan = 2,
         sticky = W+E+N+S )
      self.text1.insert( INSERT, "Text" )

      # makes second row/column expand
      self.rowconfigure( 1, weight = 1 )
      self.columnconfigure( 1, weight = 1 )

      self.ciper = rotor.newrotor( "deitelkey", 12 )

   def encrypt( self ):
      """Encrypt a text"""

      # get text from Text component
      text = self.text1.get( 1.0, END )
      text = string.strip( text )

      # encrypt text
      encryptedText = self.ciper.encrypt( text )
      self.text1.delete( 1.0, END )

      # display encrypted text
      self.text1.insert( END, encryptedText )
      
   def decrypt( self ):
      """Decrypt a text"""

      # get text from Text component
      text = self.text1.get( 1.0, END )
      text = string.strip( text )

      # decrypt text
      decryptedText = self.ciper.decrypt( text )
      self.text1.delete( 1.0, END )

      # display decrypted text
      self.text1.insert( END, decryptedText )
      
def main():
   Crypto().mainloop()   

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
