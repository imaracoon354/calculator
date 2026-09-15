x = float(input("enter number 1: "))
y = float(input("enter number 2: "))
oper = input("enter operator: ")

match oper:
    case "+":
        print(x+y)
    case "-":
        print(x-y)
    case "*":
        print(x*y)
    case "/":
        print(x/y)
