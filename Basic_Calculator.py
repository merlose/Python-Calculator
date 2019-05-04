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
        add1 = float(input("Add: "))
        add2 = float(input("to: "))
        result = str(add1 + add2)
        print ("= " + result)
    elif user_input == "-":
        sub1 = float(input("Subtract: "))
        sub2 = float(input("by: "))
        result = str(sub1 - sub2)
        print ("= " + result)
    elif user_input == "*":
        multi1 = float(input("Multiply: "))
        multi2 = float(input("with: "))
        result = str(multi1 * multi2)
        print ("= " + result)
    elif user_input == "/":
        div1 = float(input("Divide: "))
        div2 = float(input("by: "))
        result = str(div1 / div2)
        print ("= " + result)
    else:
        print ("Unknown input")