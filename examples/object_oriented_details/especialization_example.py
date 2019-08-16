
# Program that uses SingleList

from NewList import SingleList

duplicates = [ 1, 2, 2, 3, 4, 3, 6, 9 ]
print("List with duplicates is:", duplicates)

single = SingleList( duplicates )  # create SingleList object
print("SingleList, created from duplicates, is:", single)
print("The length of the list is:", len( single ))

# search for values in list
print("\nThe value 2 appears %d times in list" % single.count( 2 ))
print("The value 5 appears %d times in list" % single.count( 5 ))
print("The index of 9 in the list is:", single.index( 9 ))

if 4 in single:
   print("The value 4 was found in list")

# add values to list
single.append( 10 )
single += [ 20 ]
single.insert( 3, "hello" )
single.extend( [ -1, -2, -3 ] )
single.merge( [ "hello", 2, 100 ] )
print("\nThe list, after adding elements is:", single)

# remove values from list
popValue = single.pop()
print("\nRemoved", popValue, "from list:", single)
single.append( popValue )
print("Added", popValue, "back to end of list:", single)

# slice list
print("\nThe value of single[ 1:4 ] is:", single[ 1:4 ])
