
# Creating and accessing tuples.

# retrieve hour, minute and second from user
hour = int( input( "Enter hour: " ) )
minute = int( input( "Enter minute: " ) )
second = int( input( "Enter second: " ) )

currentTime = hour, minute, second   # create tuple

print("The value of currentTime is:", currentTime)

# access tuple
print("The number of seconds since midnight is", \
   ( currentTime[ 0 ] * 3600 + currentTime[ 1 ] * 60 +
     currentTime[ 2 ] ))

