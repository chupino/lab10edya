from ejercicio1 import Node

def evalManual():
    node1 = Node(5)
    node2 = Node(3)

    sub1 = Node('-')
    sub1.left = node1
    sub1.right = node2

    node3 = Node(6)
    node4 = Node(4)
    mul = Node('*')
    mul.left = node3
    mul.right = node4

    node5 = Node(2)
    sumNode = Node('+')
    sumNode.left = node4
    sumNode.right = node5

    divNode = Node('/')
    divNode.left = mul
    divNode.right = sumNode

    exp = Node('^')
    exp.left = sub1
    exp.right = divNode

    cuadrado = Node('^')
    cuadrado.left = exp
    cuadrado.right = Node(2)

    # Evaluar la expresión
    result = cuadrado.eval()
    print(result)

evalManual()