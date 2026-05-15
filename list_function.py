class List_function:
    def __init__(self):
        self.l1 = [1, 2, 3, 4, 5]
    
    def list_function(self):
        print('List function:')
        self.l1.append(6)
        print(self.l1)
        self.l1.insert(2, 8)
        print(self.l1)
        self.l1.extend([7, 9])
        print(self.l1)
        print(self.l1.count(2))
        print(self.l1.index(8))
        x = self.l1.copy()
        print(x)
        self.l1.pop()
        print(self.l1)
        self.l1.remove(4)
        print(self.l1)
        self.l1.sort()
        print(self.l1)
        self.l1.reverse()
        print(self.l1)
        print(len(self.l1))
        self.l1.clear()
        print(self.l1)


obj=List_function()
obj.list_function()