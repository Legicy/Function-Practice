# Functions that use default values (intitial values for parameters)

def add(x, y=10):
    print(x)
    print(y)
    return x + y

print(add(1, 2))
print (add(1))