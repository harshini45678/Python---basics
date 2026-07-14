a = float(input("Enter first number: "))
operator = input("Enter operator: ")
b = float(input("Enter second number: "))

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    print(a / b)
elif operator == "**":
    print(a ** b)
elif operator == "%":
    print(a % b)
else:
    print("invalid operator")


