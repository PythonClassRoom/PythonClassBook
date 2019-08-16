# Fig. 5.17: list_example_sort.py
# Sorting a list.

aList = [ 2, 6, 4, 8, 10, 12, 89, 68, 45, 37 ]

print("Data items in original order")

for item in aList:
   print(item,)

aList.sort()

print("\n\nData items after sorting")

for item in aList:
   print(item,)

print()

