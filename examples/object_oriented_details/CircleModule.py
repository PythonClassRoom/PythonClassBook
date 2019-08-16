
# Definition and test function for class Circle.

import math
from PointModule import Point

class Circle( Point ):
   """Class that represents a circle"""

   def __init__( self, x = 0, y = 0, radiusValue = 0.0 ):
      """Circle constructor takes center point and radius"""

      Point.__init__( self, x, y )  # call base-class constructor
      self.radius = float( radiusValue )

   def area( self ):
      """Computes area of a Circle"""

      return math.pi * self.radius ** 2

   def __str__( self ):
      """String representation of a Circle"""

      # call base-class __str__ method
      return "Center = %s Radius = %f" % \
         ( Point.__str__( self ), self.radius )

# main program
def main():
   circle = Circle( 37, 43, 2.5 )  # create Circle object

   # print circle attributes
   print("X coordinate is:", circle.x)
   print("Y coordinate is:", circle.y)
   print("Radius is:", circle.radius)

   # change circle attributes and print new values
   circle.radius = 4.25
   circle.x = 2
   circle.y = 2

   print("\nThe new location and radius of circle are:", circle)
   print("The area of circle is: %.2f" % circle.area())

   print("\ncircle printed as a Point is:", Point.__str__( circle ))

if __name__ == "__main__":
   main()

