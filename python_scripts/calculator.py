# Program make a simple calculator
print("""
          __     __    _     __    _     _    _____  ___   ___  
/ /`   / /\  | |   / /`  | | | | |    | |  / / \ | |_) 
\_\_, /_/--\ |_|__ \_\_, \_\_/ |_|__  |_|  \_\_/ |_| \                                             """)

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("【Ｓｅｌｅｃｔ　ｏｐｅｒａｔｉｏｎ】")

print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # input the choice of user
    choice = input("Enter choice from(1/2/3/4): ")

    # checking if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        
        next_calculation = input("want to do another calcultion? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")
