# Fig. 10.21: fig10_21.py
# Card shuffling and dealing program.

import random
from Tkinter import *

class Card:
   """Class that represents one playing card"""

   faces = [ "Ace", "Deuce", "Three", "Four", "Five",
      "Six", "Seven", "Eight", "Nine", "Ten", "Jack", 
      "Queen", "King" ]
   suits = [ "Hearts", "Diamonds", "Clubs", "Spades" ]   
   

   def __init__( self, face, suit ):
      """Card constructor, takes face and suit as strings"""
      
      self.face = face
      self.suit = suit

   def __str__( self ):
      """String representation of a card"""
      
      return "%s of %s" % ( self.face, self.suit )
      
class Deck( Frame ):
   """Class to represent a GUI card deck shuffler"""
   
   def __init__( self ):
      """Deck constructor"""

      Frame.__init__( self )
      self.master.title( "Card Dealing Program" )

      self.deck = []  # list of card objects
      self.currentCard = 0  # index of current card

      # create deck
      for i in range( 52 ):
         self.deck.append( Card( Card.faces[ i % 13 ],
            Card.suits[ i / 13 ] ) )

      # create buttons
      self.dealButton = Button( self, text = "Deal card",
         width = 10, command = self.dealCard )
      self.dealButton.grid( row = 0, column = 0 )

      self.shuffleButton = Button( self, text = "Shuffle cards",
         width = 10, command = self.shuffle )
      self.shuffleButton.grid( row = 0, column = 1 )

      # create labels
      self.message1 = Label( self, height = 2,
         text = "Welcome to Card Dealer!" )
      self.message1.grid( row = 1, columnspan = 2 )

      self.message2 = Label( self, height = 2,
         text = "Deal card or shuffle deck" )
      self.message2.grid( row = 2, columnspan = 2 )

      self.shuffle()
      self.grid()      

   def shuffle( self ):
      """Shuffle the deck"""

      self.currentCard = 0

      for i in range( len( self.deck ) ):
         j = random.randint( 0, 51 )

         # swap the cards
         self.deck[ i ], self.deck[ j ] = \
            self.deck[ j ], self.deck[ i ]

      self.message1.config( text = "DECK IS SHUFFLED" )   
      self.message2.config( text = "" )
      self.dealButton.config( state = NORMAL )

   def dealCard( self ):
      """Deal one card from the deck"""

      # display the card, if it exists
      if self.currentCard < len( self.deck ):
         self.message1.config(
            text = self.deck[ self.currentCard ] )
         self.message2.config(
            text = "Card #: %d" % self.currentCard )
      else:
         self.message1.config( text = "NO MORE CARDS TO DEAL" )
         self.message2.config( text = "Shuffle cards to continue" )
         self.dealButton.config( state = DISABLED )

      self.currentCard += 1  # increment card for next turn

# main program
def main():
   Deck().mainloop()

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
