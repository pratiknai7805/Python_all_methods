class Pythonfunction:

    def __init__(self):
        self.s="hello world"
        self.text="  hello  "
        self.words=["hello", "world"]
        self.l1 = [1, 2, 3, 4, 5]
        self.t=(22,12,45,2)
        self.s1 = {1, 2, 3, 4}
        self.s2 = {4, 5, 6}
        self.d1 = {"name": "pratik", "age": 21}
        self.y = dict.fromkeys(["a", "b", "c"], 0)
        
    def string_function(self):
        print('String function:')
        print(self.s.upper())
        print(self.s.lower())
        print(self.s.swapcase())
        print(self.s.title())
        print(self.s.capitalize())

        print(self.s.count("l"))
        print(self.s.index("o"))
        print(self.s.find("world"))
        print(self.s.rfind("o"))
        print(self.s.rindex("o"))

        print(self.s.isupper())
        print(self.s.islower())
        print(self.s.startswith("he"))
        print(self.s.endswith("ld"))

        print(self.s.isalpha())
        print(self.s.isalnum())
        print(self.s.isascii())

        print("123".isdecimal())
        print("123".isdigit())

        print("hello_world".isidentifier())

        print("123".isnumeric())

        print("   ".isspace())

        print("Hello World".istitle())

        print(self.s.casefold())
        print(self.s.center(20, "*"))
        print(self.s.encode())

        print(self.s.removeprefix("hello"))
        print(self.s.removesuffix("ld"))
        print(self.s.replace("world", "Python"))

        print(self.s.ljust(20, "*"))
        print(self.s.rjust(20, "*"))

        print("hello\tworld".expandtabs(10))

        print(self.text.strip())
        print(self.text.lstrip())
        print(self.text.rstrip())

        print("Hello {}".format(self.s))

        print("Hello {}".format("Pratik"))

        print("Hello {name}".format_map({"name": "raj"}))

        print(" ".join(self.words))
        print(" ".join(self.s))

        print(self.s.partition(" "))
        print(self.s.rpartition(" "))

        print(self.s.split())

        print("hello world python".rsplit(" ", 1))

        print("hello\nworld".splitlines())

        table = str.maketrans("h", "H")

        print(self.s.translate(table))

        print("5".zfill(3))
    
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
       
    def tuple_function(self):
        print('Tuple function:')
        print(self.t.count(2))
        print(self.t.index(45))
        
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
       

    def dict_function(self):
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
    
obj=Pythonfunction()
obj.string_function()
obj.list_function()
obj.tuple_function()
obj.set_function()
obj.dict_function()
        
