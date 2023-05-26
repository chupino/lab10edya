from ejercicio1 import Node

operatorPrecedence = {
    '(' : 0,
    ')' : 0,
    '+' : 1,
    '-' : 1,
    '*' : 2,
    '/' : 2
}

def parserPostfixToBinaryTree(postfix):
    stack = []
    for char in postfix:
        if char not in operatorPrecedence:
            node = Node(char)
            stack.append(node)
        else:
            node = Node(char)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)
    return stack.pop()
def evalPostfixExpression():

    postfix =  "2363/+"
    rootNode = parserPostfixToBinaryTree(postfix)
    print(rootNode.eval())

evalPostfixExpression()