from BST import BST


class SymbolTable:
    def __init__(self):
        self.bst = BST()
        self.pos = 0

    def add(self, identifier):
        param = [self.pos, str(identifier)]
        self.bst.insert(param)
        self.pos = self.pos + 1

    def search(self, identifier):
        return self.bst.search(str(identifier))

    def print(self):
        self.bst.print()

