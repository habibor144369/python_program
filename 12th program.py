terminate_program = False
while not terminate_program:
    number1 = input("please enter a first number: ")
    number1 = int(number1)
    number2 = input("please enter a second number: ")
    number2 = int(number2)
    while True:
        operator = input("please press any one operator [+ - * / % ] or [quit] press exit to program: ")

        if operator == "quit":
            terminate_program = True
            break
        if operator not in['+', '-', '*', '/', '%']:
            print("unknown operator! please press the correct operator.")
            continue
        if operator == "+":
            print("Result is: ", number1 + number2)
            break
        if operator == "-":
            print("Result is: ", number1 - number2)
            break
        if operator == "*":
            print("Result is: ", number1 * number2)
            break
        if operator == "/":
            print("Result is: ", number1 / number2)
            break
        if operator == "%":
            print("Result is: ", number1 % number2)
            break
