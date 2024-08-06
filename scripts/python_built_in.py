""" Examples for the built-in functions in Python. """


def main():
    pass


# abs()
a = -4
print(f"The absolute value of {a} is {abs(a)}")


# all() and any()
a = (True, True, True)
b = (True, True, False)
c = (False, False, False)
d = (a, b, c)
for i in d:
    if all(i):
        print(f"For {i} all are True")
    else:
        if any(i):
            print(f"For {i} at least one is True")
        else:
            print(f"For {i} none are True")
for i in d:
    if not any(i):
        print(f"For {i} all are False")
    else:
        if not all(i):
            print(f"For {i} at least one is False")
        else:
            print(f"For {i} none are False")


# ascii()
print(ascii("Escaping the non-ASCII character such as é, à, ö, ñ"))


# bin()
e = -498
print(f"The binary string of {e} is {bin(e)}")


# bool()
f = [True, False, 0, "0", "", 1, 2, -58749, 2 + 7, "Yes", "False", {}, [1]]
for i in f:
    print(f"{i} is {bool(i)}")


# bytearray
g = f"'The binary string of {e}' is {bin(e)}"
h = bytearray(g, "utf-16")
print(f"{g} is: \n{h}\nIn hexidecimal this is: {h.hex()}")

# bytes()
# callable()
# chr()


# classmethod()
class C:
    @classmethod
    def f(cls, arg1, arg2):
        pass


# compile()
# complex()
# dict()
dict()

# dir()
dir()

frozenset()

if __name__ == "__main__":
    main()
