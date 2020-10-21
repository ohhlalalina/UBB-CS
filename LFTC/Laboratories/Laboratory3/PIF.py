

class PIF:
    def __init__(self):
        self.__data = []

    def insert(self, id, el):
        self.__data.append((id, el))

    def __str__(self):
        return str(self.__data)