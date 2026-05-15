class String_function:
    def __init__(self):
        self.s="hello world"
        self.text="  hello  "
        self.words=["hello", "world"]

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

obj=String_function()
obj.string_function()
