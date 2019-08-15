# Fig. 20.4: fig20_04.py
# Set up a server that will receive packets from a
# client and send packets to a client. 

import socket

HOST = "127.0.0.1"
PORT = 5000

# step 1: create socket
mySocket = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )

# step 2: bind socket
mySocket.bind( ( HOST, PORT ) )

while 1:
   
   # step 3: receive packet
   packet, address = mySocket.recvfrom( 1024 )

   print "Packet received:"
   print "From host:", address[ 0 ]
   print "Host port:", address[ 1 ]
   print "Length:", len( packet )
   print "Containing:"
   print "\t" + packet

   # step 4: echo packet back to client
   print "\nEcho data to client...",
   mySocket.sendto( packet, address )
   print "Packet sent\n"

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
