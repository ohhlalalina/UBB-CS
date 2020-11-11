from Node import Node


class BST:
    def __init__(self):
        self.root = None

    def insert(self, param):
        if self.root is None:
            self.root = Node(param)
        else:
            p = None
            ok = 0
            node = self.root
            while node is not None:
                p = node
                if node.getValue()[1] < param[1]:
                    node = node.getLeftSide()
                    ok = 1
                elif node.getValue()[1] > param[1]:
                    node = node.getRightSide()
                    ok = 0
            if ok == 1:
                p.setLeftSide(Node(param))
            else:
                p.setRightSide(Node(param))

    def search(self, val):
        if self.root is None:
            return None

        node = self.root
        while node is not None:
            if node.getValue()[1] < val:
                node = node.getLeftSide()
            elif node.getValue()[1] > val:
                node = node.getRightSide()
            else:
                return node.getValue()
        return None

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.getLeftSide(), level + 1)
            print(' ' * 4 * level + '->', node.getValue())
            self.printTree(node.getRightSide(), level + 1)

    def print(self):
        self.printTree(self.root)