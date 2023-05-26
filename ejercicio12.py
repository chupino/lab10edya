#################################
# Fourth Case :  Evaluate Indor Expression
# Indor expression   : (5+3)*6
#################################
from ejercicio4 import parserPostfixToBinaryTree
from ejercicio8 import postfixConvert


def evalIndorExpression():
    indor = "(5+3)*6"
    postfix = postfixConvert(indor)
    rootNode = parserPostfixToBinaryTree(postfix)
    print(rootNode.eval())

#################################
# Fifth Case : Input Indor Expression 
#              from Keyboard
# 
#################################
def evalIndorExpressionFromKeyboard():
    indor = input("Input expression => ")
    postfix = postfixConvert(indor)
    #rootNode = parserPostfixToBinaryTree(postfix)
    print(postfix)
    #print(rootNode.eval())

evalIndorExpressionFromKeyboard()