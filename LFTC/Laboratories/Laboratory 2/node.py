class Node:
    def __init__(self, v):
        self.__value = v
        self.__leftSide = None
        self.__rightSide = None

    def getValue(self):
        return self.__value

    def getRightSide(self):
        return self.__rightSide

    def getLeftSide(self):
        return self.__leftSide

    def setRightSide(self, r):
        self.__rightSide = r

    def setLeftSide(self, l):
        self.__leftSide = l

    def __str__(self):
        return str(self.__value)
