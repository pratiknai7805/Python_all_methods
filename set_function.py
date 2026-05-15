class SetFunction:

    def __init__(self):
        self.s1 = {1, 2, 3, 4}
        self.s2 = {4, 5, 6}

    def set_function(self):

        print('Set function:')
        self.s1.add(9)
        print(self.s1)
        print(self.s1.copy())

        print(self.s1.difference(self.s2))

        self.s1.difference_update(self.s2)
        print(self.s1)

        self.s1 = {1, 2, 3, 4}

        self.s1.discard(2)
        print(self.s1)

        print(self.s1.intersection(self.s2))

        self.s1.intersection_update(self.s2)
        print(self.s1)

        self.s1 = {1, 2, 3, 4}

        print(self.s1.isdisjoint(self.s2))

        print({1, 2}.issubset({1, 2, 3}))

        print({1, 2, 3}.issuperset({1, 2}))

        print(self.s1.pop())
        print(self.s1)

        self.s1.remove(2)
        print(self.s1)

        print(self.s1.symmetric_difference(self.s2))

        self.s1.symmetric_difference_update(self.s2)
        print(self.s1)

        self.s1 = {1, 2, 3, 4}

        print(self.s1.union(self.s2))

        self.s2.update({7, 8, 9})
        print(self.s2)

        self.s2.clear()
        print(self.s2)


obj = SetFunction()
obj.set_function()