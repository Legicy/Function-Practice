# Functions with varaible number of parameters 
def sum(*values):
    result = 0 
    for one in values:
        result = result + one
    return result

result = sum(1, 2, 3, 4, 5, 6)
print(result)