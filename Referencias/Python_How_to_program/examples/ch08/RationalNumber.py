# Fig. 8.9: RationalNumber.py
# Definition of class Rational.

def gcd( x, y ):
   """Computes greatest common divisor of two values"""

   while y:
      z = x
      x = y
      y = z % y

   return x

class Rational:
   """Representation of rational number"""

   def __init__( self, top = 1, bottom = 1 ):
      """Initializes Rational instance"""

      # do not allow 0 denominator
      if bottom == 0:
         raise ZeroDivisionError, "Cannot have 0 denominator"

      # assign attribute values
      self.numerator = abs( top )
      self.denominator = abs( bottom )
      self.sign = ( top * bottom ) / ( self.numerator *
         self.denominator )

      self.simplify()  # Rational represented in reduced form

   # class interface method
   def simplify( self ):
      """Simplifies a Rational number"""
      
      common = gcd( self.numerator, self.denominator )
      self.numerator /= common
      self.denominator /= common
         
   # overloaded unary operator
   def __neg__( self ):
      """Overloaded negation operator"""

      return Rational( -self.sign * self.numerator,
                       self.denominator )
      
   # overloaded binary arithmetic operators
   def __add__( self, other ):
      """Overloaded addition operator"""

      return Rational(
         self.sign * self.numerator * other.denominator +
         other.sign * other.numerator * self.denominator,
         self.denominator * other.denominator )

   def __sub__( self, other ):
      """Overloaded subtraction operator"""

      return self + ( -other )

   def __mul__( self, other ):
      """Overloaded multiplication operator"""

      return Rational( self.numerator * other.numerator,
                       self.sign * self.denominator *
                       other.sign * other.denominator )

   def __div__( self, other ):
      """Overloaded / division operator."""

      return Rational( self.numerator * other.denominator,
                       self.sign * self.denominator *
                       other.sign * other.numerator )

   def __truediv__( self, other ):
      """Overloaded / division operator. (For use with Python
      versions (>= 2.2) that contain the // operator)"""

      return self.__div__( other )

   # overloaded binary comparison operators
   def __eq__( self, other ):
      """Overloaded equality operator"""

      return ( self - other ).numerator == 0

   def __lt__( self, other ):
      """Overloaded less-than operator"""

      return ( self - other ).sign < 0

   def __gt__( self, other ):
      """Overloaded greater-than operator"""

      return ( self - other ).sign > 0

   def __le__( self, other ):
      """Overloaded less-than or equal-to operator"""

      return ( self < other ) or ( self == other )

   def __ge__( self, other ):
      """Overloaded greater-than or equal-to operator"""

      return ( self > other ) or ( self == other )

   def __ne__( self, other ):
      """Overloaded inequality operator"""

      return not ( self == other )      
   
   # overloaded built-in functions
   def __abs__( self ):
      """Overloaded built-in function abs"""

      return Rational( self.numerator, self.denominator )
   
   def __str__( self ):
      """String representation"""

      # determine sign display
      if self.sign == -1:
         signString = "-"
      else:
         signString = ""

      if self.numerator == 0:
         return "0"
      elif self.denominator == 1:
         return "%s%d" % ( signString, self.numerator )
      else:
         return "%s%d/%d" % \
            ( signString, self.numerator, self.denominator )
            
   # overloaded coercion capability
   def __int__( self ):
      """Overloaded integer representation"""

      return self.sign * divmod( self.numerator,
         self.denominator )[ 0 ]

   def __float__( self ):
      """Overloaded floating-point representation"""

      return self.sign * float( self.numerator ) / self.denominator

   def __coerce__( self, other ):
      """Overloaded coercion. Can only coerce int to Rational"""

      if type( other ) == type( 1 ):
         return ( self, Rational( other ) )
      else:
         return None

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
