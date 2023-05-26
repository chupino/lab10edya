from ejercicio1 import Node

operatorPrecedence = {
    '(' : 0,
    ')' : 0,
    '+' : 1,
    '-' : 1,
    '*' : 2,
    '/' : 2,
    '^' : 3
}

def evalIndorExpressionFromKeyboard():
    indor = input("Input expression => ")
    postfix = postfixConvert(indor)
    rootNode = parserPostfixToBinaryTree(postfix)
    result = rootNode.eval()
    print(result)

def postfixConvert(infix):
    stack = []
    postfix = []
    number = ""

    for char in infix:
        if char.isdigit():
            number += char
        else:
            if number:
                postfix.append(int(number))
                number = ""
            if char not in operatorPrecedence:
                postfix.append(char)
            else:
                if len(stack) == 0:
                    stack.append(char)
                else:
                    if char == "(":
                        stack.append(char)
                    elif char == ")":
                        while stack[-1] != "(":
                            postfix.append(stack.pop())
                        stack.pop()
                    elif operatorPrecedence[char] > operatorPrecedence[stack[-1]]:
                        stack.append(char)
                    else:
                        while len(stack) != 0:
                            if stack[-1] == '(':
                                break
                            postfix.append(stack.pop())
                        stack.append(char)

    if number:
        postfix.append(int(number))

    while len(stack) != 0:
        postfix.append(stack.pop())

    return postfix

def parserPostfixToBinaryTree(postfix):
    stack = []
    for char in postfix:
        if isinstance(char, int):
            node = Node(char)
            stack.append(node)
        else:
            node = Node(char)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)
    return stack.pop()

evalIndorExpressionFromKeyboard()