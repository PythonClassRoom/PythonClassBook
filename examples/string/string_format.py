txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))


txt1 = "My name is {fname}, I'am {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'am {1}".format("John",36)
txt3 = "My name is {}, I'am {}".format("John",36)

#Use "<" to left-align the value:

txt = "We have {:<8} chickens."
print(txt.format(49))

#Use ">" to right-align the value:

txt = "We have {:>8} chickens."
print(txt.format(49))


#Use "^" to center-align the value:

txt = "We have {:^8} chickens."
print(txt.format(49))


#Use "=" to place the plus/minus sign at the left most position:

txt = "The temperature is {:=8} degrees celsius."

print(txt.format(-5))



#Use "+" to always indicate if the number is positive or negative:

txt = "The temperature is between {:+} and {:+} degrees celsius."

print(txt.format(-3, 7))


#Use "-" to always indicate if the number is negative (positive numbers are displayed without any sign):

txt = "The temperature is between {:-} and {:-} degrees celsius."

print(txt.format(-3, 7))


#Use " " (a space) to insert a space before positive numbers and a minus sign before negative numbers:

txt = "The temperature is between {: } and {: } degrees celsius."

print(txt.format(-3, 7))


#Use "," to add a comma as a thousand separator:

txt = "The universe is {:,} years old."

print(txt.format(13800000000))


#Use "_" to add a underscore character as a thousand separator:

txt = "The universe is {:_} years old."

print(txt.format(13800000000))



#Use "b" to convert the number into binary format:

txt = "The binary version of {0} is {0:b}"

print(txt.format(5))


#Use "d" to convert a number, in this case a binary number, into decimal number format:

txt = "We have {:d} chickens."
print(txt.format(0b101))


#Use "e" to convert a number into scientific number format (with a lower-case e):

txt = "We have {:e} chickens."
print(txt.format(5))


#Use "E" to convert a number into scientific number format (with an upper-case E):

txt = "We have {:E} chickens."
print(txt.format(5))














