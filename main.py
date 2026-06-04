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

if __name__ == "__main__":
    print("--- Simple Calculator ---")
    print("1. Add | 2. Subtract | 3. Multiply | 4. Divide")
    
    choice = input("Choose a number (1-4): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"Result: {add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Result: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid Choice!")