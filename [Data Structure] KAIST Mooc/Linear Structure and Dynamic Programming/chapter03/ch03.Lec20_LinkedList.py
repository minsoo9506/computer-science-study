class Node:
    nodeNext = ''
    objValue = ''
    blnHead = False
    blnTail = False

    def __init__(self, objValue='', nodeNext='', blnHead=False, blnTail=False):
        self.nodeNext = nodeNext
        self.objValue = object
        self.blnHead = blnHead
        self.blnTail = blnTail

    def getValue(self):
        return self.objValue

    def setValue(self, objValue):
        self.objValue = objValue

    def getNext(self):
        return self.nodeNext

    def setNext(self, nodeNext):
        self.nodeNext = nodeNext

    def isHead(self):
        return self.blnHead

    def isTail(self):
        return self.blnTail


node1 = Node(objValue='a')
nodeTail = Node(blnTail=True)
nodeHead = Node(blnHead=True, nodeNext=node1)
