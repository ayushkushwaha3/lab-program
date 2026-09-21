def find_max(a, b):
    if a > b:
        return a
    else:
        return b


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


print("Greater number:", find_max(num1, num2))