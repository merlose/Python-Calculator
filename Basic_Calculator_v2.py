while True:
    num1 = float(input("Input 1st number then hit ENTER: "))
    mathType = ["Select function:","(add)      +","(subtract) -","(multiply) *","(divide)   /"]
    for type in mathType:
        print (type)
    mathFunction = input("then hit ENTER: ")
    num2 = float(input("Input 2nd number then hit ENTER: "))
    if mathFunction == "+":
        answer = str(num1 + num2)
        print ("Answer = " + answer)
    elif mathFunction == "-":
        answer = str(num1 - num2)
        print ("Answer = " + answer)
    elif mathFunction == "*":
        answer = str(num1 * num2)
        print ("Answer = " + answer)
    elif mathFunction == "/":
        answer = str(num1 / num2)
        print ("Answer = " + answer)
