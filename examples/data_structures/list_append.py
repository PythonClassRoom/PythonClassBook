
# Appending items to a list.

playList = []     # list of favorite plays

print("Enter your 5 favorite Shakespearean plays.\n")

for i in range( 5 ):
   playName = input( "Play %d: " % ( i + 1 ) )
   playList.append( playName )
   
print("\nSubscript     Value")

for i in range( len( playList ) ):
   print("%9d     %-25s" % ( i + 1, playList[ i ] ))

