
# Driver for class SimpleDictionary.

from NewDictionary import SimpleDictionary

# create and print SimpleDictionary object
simple = SimpleDictionary()
print("The empty dictionary:", simple)

# add values to simple (invokes simple.__setitem__)
simple[ 1 ] = "one"
simple[ 2 ] = "two"
simple[ 3 ] = "three"
print("The dictionary after adding values:", simple)

del simple[ 1 ]  # remove a value
print("The dictionary after removing a value:", simple)

# use mapping methods
print("Dictionary keys:", simple.keys())
print("Dictionary values:", simple.values())
print("Dictionary items:", simple.items())
