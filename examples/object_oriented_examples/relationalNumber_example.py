
# Driver for class Rational.

from RationalNumber import Rational

# create objects of class Rational
rational1 = Rational()  # 1/1
rational2 = Rational( 10, 30 )  # 10/30 (reduces to 1/3)
rational3 = Rational( -7, 14 )  # -7/14 (reduces to -1/2)

# print objects of class Rational
print("rational1:", rational1)
print("rational2:", rational2)
print("rational3:", rational3)
print()

# test mathematical operators
print(rational1, "/", rational2, "=", rational1 / rational2)
print(rational3, "-", rational2, "=", rational3 - rational2)
print(rational2, "*", rational3, "-", rational1, "=", \
   rational2 * rational3 - rational1)

# overloading + implicitly overloads +=
rational1 += rational2 * rational3
print("\nrational1 after adding rational2 * rational3:", rational1)
print()

# test comparison operators
print(rational1, "<=", rational2, ":", rational1 <= rational2)
print(rational1, ">", rational3, ":", rational1 > rational3)
print()

# test built-in function abs
print("The absolute value of", rational3, "is:", abs( rational3 ))
print()

# test coercion
print(rational2, "as an integer is:", int( rational2 ))
print(rational2, "as a float is:", float( rational2 ))
print(rational2, "+ 1 =", rational2 + Rational(1))

