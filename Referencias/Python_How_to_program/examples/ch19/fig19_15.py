# Fig. 19.15: fig19_15.py
# Event objects.

import threading
import random
import time

class VehicleThread( threading.Thread ):
   """Class representing a motor vehicle at an intersection"""

   def __init__( self, threadName, event ):
      """Initializes thread"""

      threading.Thread.__init__( self, name = threadName )

      # ensures that each vehicle waits for a green light
      self.threadEvent = event
      
   def run( self ):
      """Vehicle waits unless/until light is green"""

      # stagger arrival times
      time.sleep( random.randrange( 1, 10 ) )

      # prints arrival time of car at intersection
      print "%s arrived at %s" % \
         ( self.getName(), time.ctime( time.time() ) )

      # wait for green light
      self.threadEvent.wait()

      # displays time that car departs intersection
      print "%s passes through intersection at %s" % \
         ( self.getName(), time.ctime( time.time() ) )

greenLight = threading.Event()
vehicleThreads = []

# creates and starts ten Vehicle threads
for i in range( 1, 11 ):
   vehicleThreads.append( VehicleThread( "Vehicle" + str( i ),
      greenLight ) )

for vehicle in vehicleThreads:
   vehicle.start()

while threading.activeCount() > 1:

   # sets the Event's flag to false -- block all incoming vehicles
   greenLight.clear()
   print "RED LIGHT! at", time.ctime( time.time() )
   time.sleep( 3 )

   # sets the Event's flag to true -- awaken all waiting vehicles
   print "GREEN LIGHT! at", time.ctime( time.time() )
   greenLight.set()
   time.sleep( 1 )
   
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
