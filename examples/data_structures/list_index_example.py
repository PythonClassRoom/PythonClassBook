
# Searching a list for an integer.

# Create a list of even integers 0 to 198
aList = range( 0, 199, 2 )

searchKey = int( input( "Enter integer search key: " ) )

if searchKey in aList:
   print("Found at index:", aList.index( searchKey ))
else:
   print("Value not found")
