# You start defining a function with def followed
# by a name, and function variables in brackets
# You can also set a default for funtion variables
# as seen below 
def foo(foo = "foo"):
    print(foo)

# Functions often return a value
def add (x, y):
    return x + y

if __name__ == '__main__':
    string_to_print = "Twelve: " + str(add(4,8))
    foo(string_to_print)
