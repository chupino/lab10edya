from ejercicio1 import Node

def evalManual():
    opeNodeA=Node(5)
    opeNodeB=Node(3)

    resNode=Node('-')
    resNode.left=opeNodeA
    resNode.right=opeNodeB

    opeNodeC=Node(6)
    opeNodeD=Node(4)
    mulNode=Node('*')
    mulNode.left=opeNodeC
    mulNode.right=opeNodeD

    opeNodeE=Node(4)
    opeNodeF=Node(2)
    sumNode=Node('+')
    sumNode.left=opeNodeE
    sumNode.right=opeNodeF

    divNode=Node('/')
    divNode.left=mulNode
    divNode.right=sumNode

    res2Node=Node('-')
    res2Node.left=resNode
    res2Node.right=divNode

    print(res2Node.eval())
    

evalManual()