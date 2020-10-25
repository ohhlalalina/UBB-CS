import random
import threading
import time
from node import MyNode
from anytree import Node, RenderTree, AnyNode


class Tree:
    root = MyNode("27", parent=None)
    node1 = MyNode("27", parent=root)
    node2 = MyNode("12", parent=node1)
    node3 = MyNode("15", parent=node1)
    node4 = MyNode("3", parent=node2)
    node5 = MyNode("7", parent=node2)
    node6 = MyNode("1", parent=node3)
    node7 = MyNode("14", parent=node3)
    node8 = MyNode("2", parent=node2)
    LEAVES = []
    initialTree = RenderTree(root)
    for pre, fill, node in RenderTree(root):
        if len(node.children) == 0:
            LEAVES.append(node)

    def __init__(self):
        self.tree = self.initialTree
        self.leaves = self.LEAVES
        self.__initial_tree = self.initialTree
        self.__str__()

    def get_random_leaf(self):
        return random.choices(self.leaves, k=1)[0]

    def validate_nodes(self):
        check = True
        for pre, fill, node in self.tree:
            if node.validate() is False:
                check = False
        if check is True:
            print("Sums in the tree remained unchanged!")
        else:
            print("!!!Sums changed!!!")

    def __str__(self):
        for pre, _, node in RenderTree(self.root):
            print("%s%s" % (pre, node.value.getValue()))
