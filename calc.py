def tokenizer(expression):
    token = []
    i = 0
    while i<len(expression):
        char = expression[i]
        if char.isdigit():
            digits = ""
            while i<len(expression) and (expression[i].isdigit() or expression[i] == "."):
                digits += expression[i]
                i += 1
            token.append(digits)
        elif char in "+-*/":
            token.append(char)
            i += 1
        elif char.isspace():
            i += 1
        else:
            raise ValueError(f":Invalid character: {char}")
    return token

expression = input("enter an expression: ")
tokens = tokenizer(expression)
print(tokens)