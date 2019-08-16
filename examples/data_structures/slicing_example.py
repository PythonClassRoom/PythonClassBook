
# Slicing sequences.

# create sequence
sliceString = "abcdefghij"
sliceTuple = ( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 )
sliceList = [ "I", "II", "III", "IV", "V",
              "VI", "VII", "VIII", "IX", "X" ]

# print strings
print("sliceString: ", sliceString)
print("sliceTuple: ", sliceTuple)
print("sliceList: ", sliceList)
print()

# get slices
start = int( input( "Enter start: " ) )
end = int( input( "Enter end: " ) )

# print slices
print("\nsliceString[", start, ":", end, "] = ", \
   sliceString[ start:end ])

print("sliceTuple[", start, ":", end, "] = ", \
   sliceTuple[ start:end ])

print("sliceList[", start, ":", end, "] = ", \
   sliceList[ start:end ])
