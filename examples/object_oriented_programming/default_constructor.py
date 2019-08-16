
# Demonstrating default constructor method for class Time.

from Time3 import Time

def printTimeValues( timeToPrint ):
    timeToPrint.printMilitary()
    print()
    timeToPrint.printStandard()
    print()

time1 = Time()             # all default 
time2 = Time( 2 )          # minute, second default
time3 = Time( 21, 34 )     # second default
time4 = Time( 12, 25, 42 ) # all specified

print("Constructed with:")

print("\nall arguments defaulted:")
printTimeValues( time1 )

print("\nhour specified; minute and second defaulted:")
printTimeValues( time2 )

print("\nhour and minute specified; second defaulted:")
printTimeValues( time3 )

print("\nhour, minute and second specified:")
printTimeValues( time4 )
