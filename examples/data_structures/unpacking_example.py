
# Unpacking sequences.

# create sequences
aString = "abc"
aList = [ 1, 2, 3 ]
aTuple = "a", "A", 1

# unpack sequences to variables
print("Unpacking string...")
first, second, third = aString
print("String values:", first, second, third)

print("\nUnpacking list...")
first, second, third = aList
print("List values:", first, second, third)

print("\nUnpacking tuple...")
first, second, third = aTuple
print("Tuple values:", first, second, third)

# swapping two values
x = 3
y = 4

print("\nBefore swapping: x = %d, y = %d" % ( x, y ))
x, y = y, x     # swap variables
print("After swapping: x = %d, y = %d" % ( x, y ))

