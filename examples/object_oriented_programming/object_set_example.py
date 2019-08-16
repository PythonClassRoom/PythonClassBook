
# Driver to test class TimeControl.

from Time2 import Time

time1 = Time()

# print initial time
print("The initial military time is",)
time1.printMilitary()
print("\nThe initial standard time is",
time1.printStandard())

# change time
time1.setTime( 13, 27, 6 )
print("\n\nMilitary time after setTime is",
time1.printMilitary())
print("\nStandard time after setTime is",
time1.printStandard())

time1.setHour( 4 )
time1.setMinute( 3 )
time1.setSecond( 34 )
print("\n\nMilitary time after setHour, setMinute, setSecond is",
time1.printMilitary())
print("\nStandard time after setHour, setMinute, setSecond is",
time1.printStandard())

