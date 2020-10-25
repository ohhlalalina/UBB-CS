from Tree import Tree


class Change:
    def __init__(self, leaf, parents, new):
        self.__leaf = leaf
        self.__parents = parents
        self.__new_value = new

    def execute(self):
        value = self.__leaf.get_value_node().getValue()
        difference = self.__new_value - value
        self.__leaf.modify_node(difference)
        for p in self.__parents:
            p.modify_node(difference)
