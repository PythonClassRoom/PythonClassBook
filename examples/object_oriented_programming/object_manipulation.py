
# Creating and manipulating objects of class Time.

from Time1 import Time  # import class definition from file

time1 = Time()  # create object of class Time

# access object's attributes
print("The attributes of time1 are: ")
print("time1.hour:", time1.hour)
print("time1.minute:", time1.minute)
print("time1.second:", time1.second)

# access object's methods
print("\nCalling method printMilitary:",
time1.printMilitary())

print("\nCalling method printStandard:",
time1.printStandard())

# change value of object's attributes
print("\n\nChanging time1's hour attribute...")
time1.hour = 25
print("Calling method printMilitary after alteration:",
time1.printMilitary())

