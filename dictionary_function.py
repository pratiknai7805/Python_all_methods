class Dictionary_function:
    def __init__(self):
        self.d1 = {"name": "pratik", "age": 21}
        self.y = dict.fromkeys(["a", "b", "c"], 0)
    
    def dic_function(self):
        print('Dictionary function:')

        print(self.d1.keys())
        print(self.d1.values())
        print(self.d1.items())

        x =self.d1.copy()
        print(x)

        print(self.d1.get("name"))

        self.d1.update({"subject": "Hindi", "roll": 5})
        print(self.d1)

        print(self.d1.setdefault("city", "Ahmedabad"))
        print(self.d1)

        print(self.d1.pop("age"))
        print(self.d1)

        print(self.d1.popitem())
        print(self.d1)

        print(self.y)

        self.d1.clear()
        print(self.d1)
    
obj=Dictionary_function()
obj.dic_function()