def add(x,y):
    return x+y
print(add(2,3))

def subtract(x,y):
    return x-y  
print(subtract(5,2))
def multiply(x,y):
    return x*y      
print(multiply(4,6))


def divide(x,y):
    if y != 0:
        return x/y
    else:
        return "Cannot divide by zero"
print(divide(10,2))
print(divide(10,0))