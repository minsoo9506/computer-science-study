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


class SingleLinkedList:
    nodeHead = ''
    nodeTail = ''
    size = 0

    def __init__(self):
        self.nodeTail = Node(blnTail=True)
        self.nodeHead = Node(blnHead=True, nodeNext=self.nodeTail)

    def insertAt(self, objInsert, idxInsert):
        nodeNew = Node(objValue=objInsert)
        nodePrev = self.get(idxInsert-1)
        nodeNext = nodePrev.getNext()
        nodePrev.setNext(nodeNew)
        nodeNew.setNext(nodeNext)
        self.size += 1

    def removeAt(self, idxRemove):
        nodePrev = self.get(idxRemove-1)
        nodeRemove = nodePrev.getNext()
        nodeNext = nodeRemove.getNext()
        nodePrev.setNext(nodeNext)
        self.size -= 1
        return nodeRemove.getValue()

    def get(self, idxRetrieve):
        nodeReturn = self.nodeHead
        for i in range(idxRetrieve+1):
            nodeReturn = nodeReturn.getNext()
        return nodeReturn

    def printStatus(self):
        nodeCurrent = self.nodeHead
        while nodeCurrent.getNext().isTail() == False:
            nodeCurrent = nodeCurrent.getNext()
            print(nodeCurrent.getValue(), end=' ')
        print('')

    def getSize(self):
        return self.size


LinkedList = SingleLinkedList()
LinkedList.insertAt('a', 0)
LinkedList.insertAt('b', 1)
LinkedList.insertAt('d', 2)
LinkedList.insertAt('e', 3)
LinkedList.printStatus()

LinkedList.insertAt('c', 2)
LinkedList.printStatus()

LinkedList.removeAt(3)
LinkedList.printStatus()
