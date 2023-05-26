from ejercicio8 import postfixConvert
from ejercicio8 import convertIndorToPostfixExp

def convertIndorToPostfixExp():
    indor = "((5-3)-(6*4)/(4-2))^2"
    postfix = postfixConvert(indor) 
    print(postfix)

convertIndorToPostfixExp()