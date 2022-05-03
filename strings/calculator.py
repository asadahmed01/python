first_num = float(input("Enter first number: "))
second_num = float(input("Enter second number: "))
operator = input("Choose operator: ")


def calculate(first, second, op):
    if op == "+":
        return first + second
    elif op == "-":
        return first - second
    elif op == "*":
        return first * second
    elif op == "/":
        return first / second
    else:
        print("invalid operator")


print(calculate(first_num, second_num, operator))
