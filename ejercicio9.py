from ejercicio8 import postfixConvert
from ejercicio8 import convertIndorToPostfixExp

def convertIndorToPostfixExp():
    indor = "((2*3)+(6/3))"
    postfix = postfixConvert(indor) 
    print(postfix)

convertIndorToPostfixExp()
