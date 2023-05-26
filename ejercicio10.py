from ejercicio8 import postfixConvert
from ejercicio8 import convertIndorToPostfixExp

def convertIndorToPostfixExp():
    indor = "((2+4)*(8-9/3)) "
    postfix = postfixConvert(indor) 
    print(postfix)

convertIndorToPostfixExp()