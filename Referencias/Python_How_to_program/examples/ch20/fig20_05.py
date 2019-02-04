# Fig. 20.5: fig20_05.py
# Set up a client that will send packets to a
# server and receive packets from a server.

import socket

HOST = "127.0.0.1"
PORT = 5000

# step 1: create socket
mySocket = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )

while 1:
   
   # step 2: send packet
   packet = raw_input( "Packet>>>" )
   print "\nSending packet containing:", packet
   mySocket.sendto( packet, ( HOST, PORT ) )
   print "Packet sent\n"

   # step 3: receive packet back from server
   packet, address = mySocket.recvfrom( 1024 )
   
   print "Packet received:"
   print "From host:", address[ 0 ]
   print "Host port:", address[ 1 ]
   print "Length:", len( packet )
   print "Containing:"
   print "\t" + packet + "\n"

mySocket.close()

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
