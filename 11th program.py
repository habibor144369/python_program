terminate_program = False
while not terminate_program:
    number1 = input("Please enter a value: ")
    number1 = int(number1)
    number2 = input("Please enter the value:  ")
    number2 = int(number2)

    while True:
        operation = input("Please enter add/sub or quit the exit: ")

        if operation == "quit":
            terminate_program = True
            break
        if operation not in ["add", "sub"]:
            print("Unknown Operation")
            continue
        if operation == 'add':
            print("result is:", number1 + number2)
            break
        if operation == 'sub':
            print("result is:", number1 - number2)
            break





