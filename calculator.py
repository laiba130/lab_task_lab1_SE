def my_calculator():
    no_val = 1
    value = []
    while no_val != 3:
        while True:
            try:
                value1 = int(input(f"Enter {no_val} value: "))
            except Exception as a:
                print("Value Error. Enter only integer numbers")
            else:
                no_val += 1
                value.append(value1)
                break
    operation = input("Enter operation(+, -, *, /, %): ")
    while operation not in ('+', '-', '*', '/', '%'):
        print("Enter only those operations given in option")
        operation = input("Enter operation(+, -, *, /, %): ")
    result = 0
    if operation == "+":
        result = value[0] + value[1]
    elif operation == '-':
        result = value[0] - value[1]
    elif operation == "*":
        result = value[0] * value[1]
    elif operation == "/":
        result = value[0] / value[1]
    else:
        result = value[0] % value[1]

    return result


print(f"Your output = {my_calculator(g)}")

