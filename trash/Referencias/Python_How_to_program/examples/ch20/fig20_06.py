# Fig. 20.6: fig20_06.py
# Class TicTacToeServer maintains a game of Tic-Tac-Toe
# for two clients, each managed by a Player thread.

import socket
import threading

class Player( threading.Thread ):
   """Thread to manage each Tic-Tac-Toe client individually"""

   def __init__( self, connection, server, number ):
      """Initialize thread and setup variables"""
      
      threading.Thread.__init__( self )

      # specify player's mark
      if number == 0:
         self.mark = "X"
      else:
         self.mark = "O"

      self.connection = connection
      self.server = server
      self.number = number

   def otherPlayerMoved( self, location ):
      """Notify client of opponent’s last move"""
      
      self.connection.send( "Opponent moved." )
      self.connection.send( str( location ) )

   def run( self ):
      """Play the game"""
      
      # send client message indicating its mark (X or O)  
      self.server.display( "Player %s connected." % self.mark ) 
      self.connection.send( self.mark )

      # wait for another player to arrive
      if self.mark == "X":
         self.connection.send( "Waiting for another player..." )
         self.server.gameBeginEvent.wait()
         self.connection.send(
            "Other player connected. Your move." )
      else:
         self.server.gameBeginEvent.wait()   # wait for server
         self.connection.send( "Waiting for first move..." )
         
      # play game until over
      while not self.server.gameOver():
   
         # get more location from client
         location = self.connection.recv( 1 )
   
         if not location:
            break
         
         # check for valid move
         if self.server.validMove( int( location ), self.number ):
            self.server.display( "loc: " + location )
            self.connection.send( "Valid move." )
         else:
            self.connection.send( "Invalid move, try again." )

      # close connection to client
      self.connection.close()
      self.server.display( "Game over." )
      self.server.display( "Connection closed." )

class TicTacToeServer:
   """Server that maintains a game of Tic-Tac-Toe for two clients"""
   
   def __init__( self ):
      """Initialize variables and setup server"""
      
      HOST = ""
      PORT = 5000

      self.board = []
      self.currentPlayer = 0
      self.turnCondition = threading.Condition()
      self.gameBeginEvent = threading.Event()

      for i in range( 9 ):
         self.board.append( None )

      # setup server socket
      self.server = socket.socket( socket.AF_INET,
         socket.SOCK_STREAM )
      self.server.bind( ( HOST, PORT ) )
      self.display( "Server awaiting connections..." )

   def execute( self ):
      """Play the game--create and start both Player threads"""

      self.players = []

      # wait for and accept two client connections
      for i in range( 2 ):
         self.server.listen( 2 )
         connection, address = self.server.accept()

         # assign each client to a Player thread
         self.players.append( Player( connection, self, i ) )
         self.players[ -1 ].start()

      self.server.close()   # no more connections to wait for

      # players are suspended until player O connects
      # resume players now
      self.gameBeginEvent.set()
   
   def display( self, message ):
      """Display a message on the server"""

      print message

   def validMove( self, location, player ):
      """Determine if a move is valid--if so, make move"""

      # only one move can be made at a time      
      self.turnCondition.acquire()

      # while not current player, must wait for turn
      while player != self.currentPlayer:
         self.turnCondition.wait()

      # make move if location is not occupied
      if not self.isOccupied( location ):

         # set move on board
         if self.currentPlayer == 0:
            self.board[ location ] = "X"
         else:
            self.board[ location ] = "O"

         # change current player
         self.currentPlayer = ( self.currentPlayer + 1 ) % 2
         self.players[ self.currentPlayer ].otherPlayerMoved(
            location )

         # tell waiting player to continue
         self.turnCondition.notify()
         self.turnCondition.release()

         # valid move
         return 1

      # invalid move     
      else:
         self.turnCondition.notify()
         self.turnCondition.release()
         return 0

   def isOccupied( self, location ):
      """Determine if a space is occupied"""

      return self.board[ location ]   # an empty space is None

   def gameOver( self ):
      """Determine if the game is over"""

      # place code here testing for a game winner
      # left as an exercise for the reader
      return 0

def main():
   TicTacToeServer().execute()

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
