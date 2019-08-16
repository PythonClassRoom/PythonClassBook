# Fig. 5.18: list_index_example.py
# Searching a list for an integer.

# Create a list of even integers 0 to 198
aList = range( 0, 199, 2 )

secarhKey = int( input( "Enter integer search key: " ) )

if secarhKey in aList:
   print("Found at index:", aList.index( secarhKey ))
else:
   print("Value not found")
