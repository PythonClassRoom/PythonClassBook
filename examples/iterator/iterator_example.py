class MyNumbers:
    def __init__(self,size):
        self.size = size
        self.value = 0

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value <= 2 ** self.size:
            x = self.value
            self.value += 1
            return 2 ** x
        else:
            raise StopIteration

myclass = MyNumbers(6)
myiter = iter(myclass)

for x in myiter:
    print(x)