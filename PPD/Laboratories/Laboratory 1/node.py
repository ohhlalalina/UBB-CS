import time

from anytree import Node
import threading
from atomic_int import AtomicInteger


class MyNode(Node):
    def __init__(self, name, parent):
        super().__init__(name=name, parent=parent)
        self.value = AtomicInteger(int(name))
        self.mutex: threading.Lock = threading.Lock()

    def get_value_node(self):
        return self.value

    def get_parents_leaf(self):
        current_leaf = self
        parents = []
        while current_leaf.parent is not None:
            parents.append(current_leaf.parent)
            current_leaf = current_leaf.parent
        return parents

    def modify_node(self, value):
        while not self.mutex.acquire(blocking=False):
            time.sleep(0.1)
        self.value.modify(value)
        self.mutex.release()

    def validate(self):
        with self.mutex:
            sum = 0
            for child in self.children:
                sum = sum + child.value.getValue()
            if sum != self.value.getValue() and sum != 0:
                return False
            return True