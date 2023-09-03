repeat = True
while repeat:
    while True:
        try:
            first = float(input("enter first number "))
            break
        except ValueError:
            print("enter a valid numeric value!")

    while True:
        try:
            operation = input("enter the operation ")
            if operation in ["+", "-", "n", "/"]:
                break
            else:
                raise ValueError
        except ValueError:
            print("please enter a valid operator +,-,/,* ")

    while True:
        try:
            second = float(input("enter second number "))
            if second == 0 and operation == "/":
                raise ZeroDivisionError
            break
        except ValueError:
            print("enter a valid numeric value!")
        except ZeroDivisionError:
            print("Cannot divide by zero!! please enter another numeric value")

    # if operation == "+":
    #    result = first + second
    # elif operation == "-":
    #    result = first - second
    # elif operation == "/":
    #    result = first / second
    # elif operation == "*":
    #    result = first * second

    # print(result)

    match operation:
        case "+":
            result = first + second
        case "-":
            result = first - second
        case "/":
            result = first / second
        case "*":
            result = first * second
        case _:
            result = None
    print(result)

    while True:
        try:
            R = input("Do you want to exit now? (enter y or n) ")
            if R == "n":
                repeat = False
            if R in ["y", "n"]:
                break
            else:
                raise ValueError
        except ValueError:
            print("enter a valid answer y or n ")


print("Program ended !! ")
