# Fig. 20.2: fig20_02.py
# Set up a server that will receive a connection
# from a client, send a string to the client,
# and close the connection.

import socket
import sys

HOST = "127.0.0.1"
PORT = 5000
counter = 0

# step 1: create socket
mySocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

# step 2: bind the socket to address
try:
   mySocket.bind( ( HOST, PORT ) ) 
except socket.error:
   sys.exit( "Call to bind failed" )

while 1:

   # step 3: wait for connection request
   print "Waiting for connection"
   mySocket.listen( 1 )

   # step 4: establish connection for request
   connection, address = mySocket.accept()
   counter += 1
   print "Connection", counter, "received from:", address[ 0 ]

   # step 5: send and receive data via connection
   connection.send( "SERVER>>> Connection successful" )
   clientMessage = connection.recv( 1024 )

   while clientMessage != "CLIENT>>> TERMINATE":

      if not clientMessage:
         break

      print clientMessage
      serverMessage = raw_input( "SERVER>>> " )
      connection.send( "SERVER>>> " + serverMessage )
      clientMessage = connection.recv( 1024 )

   # step 6: close connection
   print "Connection terminated"
   connection.close()

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
