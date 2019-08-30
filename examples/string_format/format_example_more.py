class A(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


a = A(2,3)

print('x is {0.x}, y is {0.y}'.format(a))