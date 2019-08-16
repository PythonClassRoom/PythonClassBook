# Fig. 5.9: diccionary_example.py
# Creating, accessing and modifying a dictionary.

# create and print an empty dictionary
emptyDictionary = {}
print("The value of emptyDictionary is:", emptyDictionary)

# create and print a dictionary with initial values
grades = { "John": 87, "Steve": 76, "Laura": 92, "Edwin": 89 }
print("\nAll grades:", grades)

# access and modify an existing dictionary
print("\nSteve's current grade:", grades[ "Steve" ])
grades[ "Steve" ] = 90
print("Steve's new grade:", grades[ "Steve" ])

# add to an existing dictionary
grades[ "Michael" ] = 93
print("\nDictionary grades after modification:")
print(grades)

# delete entry from dictionary
del grades[ "John" ]
print("\nDictionary grades after deletion:")
print(grades)
