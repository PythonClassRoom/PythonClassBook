# Fig. 20.7: fig20_07.py
# Client for Tic-Tac-Toe program.

import socket
import threading
from Tkinter import *
import Pmw

class TicTacToeClient( Frame, threading.Thread ):
   """Client that plays a game of Tic-Tac-Toe"""
   
   def __init__( self ):
      """Create GUI and play game"""
      
      threading.Thread.__init__( self )

      # initialize GUI
      Frame.__init__( self )
      Pmw.initialise()
      self.pack( expand = YES, fill = BOTH )
      self.master.title( "Tic-Tac-Toe Client" )
      self.master.geometry( "250x325" )

      self.id = Label( self, anchor = W )
      self.id.grid( columnspan = 3, sticky = W+E+N+S )

      self.board = []

      # create and add all buttons to the board
      for i in range( 9 ):
         newButton = Button( self, font = "Courier 20 bold",
            height = 1, width = 1, relief = GROOVE,
            name = str( i ) )
         newButton.bind( "<Button-1>", self.sendClickedSquare )
         self.board.append( newButton )

      current = 0

      # display buttons in 3x3 grid beginning with grid's row one
      for i in range( 1, 4 ):

         for j in range( 3 ):
            self.board[ current ].grid( row = i, column = j,
               sticky = W+E+N+S )
            current += 1

      # area for server messages
      self.display = Pmw.ScrolledText( self, text_height = 10,
         text_width = 35, vscrollmode = "static" )
      self.display.grid( row = 4, columnspan = 3 )

      self.start()   # run thread
   
   def run( self ):
      """Control thread to allow continuous updated display"""

      # setup connection to server
      HOST = "127.0.0.1"
      PORT = 5000
      self.connection = socket.socket( socket.AF_INET,
         socket.SOCK_STREAM )
      self.connection.connect( ( HOST, PORT ) )

      # first get player’s mark ( X or O )
      self.myMark = self.connection.recv( 1 )
      self.id.config( text = 'You are player "%s"' % self.myMark )

      self.myTurn = 0

      # receive messages sent to client
      while 1:
         message = self.connection.recv( 34 )

         if not message:
            break
         
         self.processMessage( message )

      self.connection.close()
      self.display.insert( END, "Game over.\n" )
      self.display.insert( END, "Connection closed.\n" )
      self.display.yview( END )

   def processMessage( self, message ):
      """Interpret server message to perform necessary actions"""

      # valid move occurred
      if message == "Valid move.":
         self.display.insert( END, "Valid move, please wait.\n" )
         self.display.yview( END )

         # set mark
         self.board[ self.currentSquare ].config(
            text = self.myMark, bg = "white" )

      # invalid move occurred
      elif message == "Invalid move, try again.":
         self.display.insert( END, message + "\n" )
         self.display.yview( END )
         self.myTurn = 1

      # opponent moved
      elif message == "Opponent moved.":

         # get move location
         location = int( self.connection.recv( 1 ) )

         # update board
         if self.myMark == "X":
            self.board[ location ].config( text = "O", 
               bg = "gray" )
         else:
            self.board[ location ].config( text = "X", 
               bg = "gray" )

         self.display.insert( END, message + " Your turn.\n" )
         self.display.yview( END )
         self.myTurn = 1

      # other player's turn
      elif message == "Other player connected. Your move.":
         self.display.insert( END, message + "\n" )
         self.display.yview( END )
         self.myTurn = 1

      # simply display message
      else:
         self.display.insert( END, message + "\n" )
         self.display.yview( END )

   def sendClickedSquare( self, event ):
      """Send attempted move to server"""

      if self.myTurn:
         name = event.widget.winfo_name()
         self.currentSquare = int( name )

         # send location to server
         self.connection.send( name )
         self.myTurn = 0

def main():
   TicTacToeClient().mainloop()

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
