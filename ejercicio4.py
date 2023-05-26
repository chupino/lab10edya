#################################
# Second Case :  53+6*
# input : postfix
# return : Binary Tree
#################################
from ejercicio1 import Node
operatorPrecedence = {
    '(' : 0,
    ')' : 0,
    '+' : 1,
    '-' : 1,
    '*' : 2,
    '/' : 2,
    '^':3
}

#################################
# Second Case : 
#             Function to convert
#             postfix to binary tree
# input : Postfix
# return : Binary Tree
#################################
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


#################################
# Second Case :  Evaluate Postfix
#                espression
#
#  Binary tree :  (5+3)*6
#
#            *
#
#       +        6
#
#    5     3
#
# Indor expression   : (5+3)*6
# Postfix expression : 53+6*
# Prefix expression  : *+536
#################################
def evalPostfixExpression():

    postfix =  "53+6*"
    rootNode = parserPostfixToBinaryTree(postfix)
    print(rootNode.eval())

#################################
# Main
#################################
if __name__ == '__main__':
    '''
    Este metodo es para 
    '''
   # evalManual()
    evalPostfixExpression()
