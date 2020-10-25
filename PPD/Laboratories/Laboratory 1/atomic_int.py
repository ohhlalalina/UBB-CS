import threading


class AtomicInteger:
    def __init__(self, value):
        self.__value = value
        self.__mutex: threading.Lock = threading.Lock()

    def modify(self, v):
        with self.__mutex:
            self.__value += v
            return self.__value

    def getValue(self):
        return self.__value
