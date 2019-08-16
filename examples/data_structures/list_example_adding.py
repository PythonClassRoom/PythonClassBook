# Fig. 5.3: list_example_adding.py
# Creating, accessing and changing a list.

aList = []    # create empty list

# add values to list
for number in range( 1, 11 ):
   aList += [ number ]

print("The value of aList is:", aList)

# access list values by iteration
print("\nAccessing values by iteration:")

for item in aList:
   print(item,)

print()

# access list values by index
print("\nAccessing values by index:")
print("Subscript   Value")

for i in range( len( aList ) ):
   print("%9d %7d" % ( i, aList[ i ] ))

# modify list
print("\nModifying a list value...")
print("Value of aList before modification:", aList)
aList[ 0 ] = -100   
aList[ -3 ] = 19
print("Value of aList after modification:", aList)
