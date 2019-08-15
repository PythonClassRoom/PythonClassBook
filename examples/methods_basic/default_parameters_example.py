# Fig. 4.20: default_parameters_example.py
# Using default arguments.

# function definition with default arguments
def boxVolume( length = 1, width = 1, height = 1 ):
   return length * width * height

print("The default box volume is:", boxVolume())
print("\nThe volume of a box with length 10,")
print("width 1 and height 1 is:", boxVolume( 10 ))
print("\nThe volume of a box with length 10,")
print("width 5 and height 1 is:", boxVolume( 10, 5 ))
print("\nThe volume of a box with length 10,")
print("width 5 and height 2 is:", boxVolume( 10, 5, 2 ))

