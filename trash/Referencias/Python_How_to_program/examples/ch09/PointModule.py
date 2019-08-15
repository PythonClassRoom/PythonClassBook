# Fig 9.6: PointModule.py
# Definition and test function for class Point.

class Point:
   """Class that represents a geometric point"""

   def __init__( self, xValue = 0, yValue = 0 ):
      """Point constructor takes x and y coordinates"""

      self.x = xValue
      self.y = yValue

   def __str__( self ):
      """String representation of a Point"""

      return "( %d, %d )" % ( self.x, self.y )      

# main program
def main():
   point = Point( 72, 115 )  # create object of class Point

   # print point attributes
   print "X coordinate is:", point.x
   print "Y coordinate is:", point.y

   # change point attributes and output new location
   point.x = 10
   point.y = 10

   print "The new location of point is:", point   

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
