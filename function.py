def string_function():
    print('String function:')
    s = "hello world"

    print(s.upper())
    print(s.lower())
    print(s.swapcase())
    print(s.title())
    print(s.capitalize())

    print(s.count("l"))
    print(s.index("o"))
    print(s.find("world"))
    print(s.rfind("o"))
    print(s.rindex("o"))

    print(s.isupper())
    print(s.islower())
    print(s.startswith("he"))
    print(s.endswith("ld"))

    print(s.isalpha())
    print(s.isalnum())
    print(s.isascii())
    print(s.isdecimal())
    print(s.isdigit())
    print(s.isidentifier())
    print(s.isnumeric())
    print(s.isspace())
    print(s.istitle())

    print(s.casefold())
    print(s.center(20, "*"))
    print(s.encode())

    print(s.removeprefix("hello"))
    print(s.removesuffix("ld"))
    print(s.replace("world", "Python"))

    print(s.ljust(20, "*"))
    print(s.rjust(20, "*"))

    l = "hello\tworld"
    print(l.expandtabs(10))

    text = "   hello   "

    print(text.strip())
    print(text.lstrip())

    text = "hello   "
    print(text.rstrip())

    print("Hello {}".format(s))

    name = "Pratik"
    print("Hello {}".format(name))

    data = {"name": "raj"}
    print("Hello {name}".format_map(data))

    words = ["hello", "world"]

    print(" ".join(words))
    print(" ".join(s))

    print(s.partition(" "))
    print(s.rpartition(" "))

    print(s.split())

    p = "hello world python"
    print(p.rsplit(" ", 1))

    text = "hello\nworld"
    print(text.splitlines())    

    table = str.maketrans("h", "H")
    print(s.translate(table))

    print("5".zfill(3))

string_function()


def list_function():

    print('List function:')
    l = [1, 2, 3, 4, 5]
    l.append(6)
    print(l)
    l.insert(2, 8)
    print(l)
    l.extend([7, 9])
    print(l)
    print(l.count(2))
    print(l.index(8))
    x = l.copy()
    print(x)
    l.pop()
    print(l)
    l.remove(4)
    print(l)
    l.sort()
    print(l)
    l.reverse()
    print(l)
    print(len(l))
    l.clear()
    print(l)

list_function()


def tuple_function():
    print('Tuple function:')
    t=(22,12,45,2)
    print(t.count(2))
    print(t.index(45))

tuple_function()


def set_function():
    
    print('Set function:')
    s1 = {1, 2, 3, 4}
    s2 = {4, 5, 6}

    s1.add(9)
    print(s1)

    x = s1.copy()
    print(x)

    print(s1.difference(s2))

    a = {1, 2, 3}
    b = {3, 4, 5}

    a.difference_update(b)
    print(a)

    s1.discard(2)
    print(s1)

    print(s1.intersection(s2))

    c = {1, 2, 3}
    d = {2, 3, 4}

    c.intersection_update(d)
    print(c)

    print(s1.isdisjoint(s2))

    print({1, 2}.issubset({1, 2, 3}))

    print({1, 2, 3}.issuperset({1, 2}))

    e = {10, 20, 30}
    print(e.pop())
    print(e)

    s1.remove(1)
    print(s1)

    print(s1.symmetric_difference(s2))

    f = {1, 2, 3}
    g = {3, 4, 5}

    f.symmetric_difference_update(g)
    print(f)

    print(s1.union(s2))

    s2.update({7, 8, 9})
    print(s2)

    s2.clear()
    print(s2)

set_function()


def dict_function():
    print('Dictionary function:')

    d = {"name": "pratik", "age": 21}

    print(d.keys())
    print(d.values())
    print(d.items())

    x = d.copy()
    print(x)

    print(d.get("name"))

    d.update({"subject": "Hindi", "roll": 5})
    print(d)

    print(d.setdefault("city", "Ahmedabad"))
    print(d)

    print(d.pop("age"))
    print(d)

    print(d.popitem())
    print(d)

    y = dict.fromkeys(["a", "b", "c"], 0)
    print(y)

    d.clear()
    print(d)

dict_function()