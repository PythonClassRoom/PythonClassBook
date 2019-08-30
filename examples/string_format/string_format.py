name = 'Carlos'
print("hi there %s" % name)

name = ('Carlos', 'Andres')
print("hi there %s" % (name,))

print("%(a)s, %(a)s" % {'a':'test'})

print('{0}, {0}'.format('test'))

tu = (12,45,22222,103,6)
print('{0} {2} {1} {2} {3} {2} {4} {2}'.format(*tu))

li = [12,45,78,784,2,69,1254,4785,984]
print(list(map('the number is {}'.format,li)))

