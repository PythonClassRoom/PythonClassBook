class MyNumbers:
    def __init__(self,size):
        self.size = size

    def __iter__(self):
        self.value = 1
        return self

    def __next__(self):
        if self.value <= 2 ** self.size:
            x = self.value
            self.value *= 2
            return x
        else:
            raise StopIteration

myclass = MyNumbers(6)
myiter = iter(myclass)

for x in myiter:
    print(x)