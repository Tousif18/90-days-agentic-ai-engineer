def calculator(a, b, operation):
    operations = {
        "+": lambda: a + b,
        "-": lambda: a - b,
        "*": lambda: a * b,
        "/": lambda: a / b if b != 0 else "Cannot divide by zero",
    }
    return operations.get(operation, "Invalid operation")()


if __name__ == "__main__":
    print(calculator(10, 5, "+"))
