# menu. accepts user input until "quit" is used.
# a while loop is used for the menu



while True:
    print("Options:")
    print("Enter + to add two numbers")
    print("Enter - to subtract two numbers")
    print("Enter * to multiply two numbers")
    print("Enter / to divide two numbers")
    print("Enter 'Get me out of here' to close program")
    user_input = input("Input calculation type: ")

    if user_input == "Get me out of here":
        break
    elif user_input == "+":
        num1 = float(input("Add: "))
        num2 = float(input("to: "))
        result = str(num1 + num2)
        print ("= " + result)
    elif user_input == "-":
        num1 = float(input("Subtract: "))
        num2 = float(input("by: "))
        result = str(num1 - num2)
        print ("= " + result)
    elif user_input == "*":
        num1 = float(input("Multiply: "))
        num2 = float(input("with: "))
        result = str(num1 * num2)
        print ("= " + result)
    elif user_input == "/":
        num1 = float(input("Divide: "))
        num2 = float(input("by: "))
        result = str(num1 / num2)
        print ("= " + result)
    else:
        print ("Unknown input")
