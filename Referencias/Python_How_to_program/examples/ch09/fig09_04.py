# Fig 9.4: fig09_04.py
# Derived class inheriting from a base class.

import math

class Point:
   """Class that represents geometric point"""

   def __init__( self, xValue = 0, yValue = 0 ):
      """Point constructor takes x and y coordinates"""

      self.x = xValue
      self.y = yValue

class Circle( Point ):
   """Class that represents a circle"""

   def __init__( self, x = 0, y = 0, radiusValue = 0.0 ):
      """Circle constructor takes x and y coordinates of center
      point and radius"""

      Point.__init__( self, x, y )  # call base-class constructor
      self.radius = float( radiusValue )

   def area( self ):
      """Computes area of a Circle"""

      return math.pi * self.radius ** 2

# main program

# examine classes Point and Circle
print "Point bases:", Point.__bases__
print "Circle bases:", Circle.__bases__

# demonstrate class relationships with built-in function issubclass
print "\nCircle is a subclass of Point:", \
   issubclass( Circle, Point )
print "Point is a subclass of Circle:", issubclass( Point, Circle )

point = Point( 30, 50 )  # create Point object
circle = Circle( 120, 89, 2.7 )   # create Circle object

# demonstrate object relationship with built-in function isinstance
print "\ncircle is a Point object:", isinstance( circle, Point )
print "point is a Circle object:", isinstance( point, Circle )

# print Point and Circle objects
print "\npoint members:\n\t", point.__dict__
print "circle members:\n\t", circle.__dict__

print "\nArea of circle:", circle.area()
