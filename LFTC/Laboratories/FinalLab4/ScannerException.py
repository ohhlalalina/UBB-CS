

class ScannerException(Exception):
    """
    Receives a line and a message
    """
    def __init__(self, line, message):
        self._line = line
        self._message = message

    """
    Getter for line
    """
    def get_line(self):
        return self._line

    """
    Getter for message
    """
    def get_message(self):
        return self._message

    """
    Setter for line
    """
    def set_line(self, line):
        self._line = line

    """
    Setter for message
    """
    def set_message(self, message):
        self._message = message

    """
    Prints the exception message using line and message
    """
    def __str__(self):
        return "Exception at line " + str(self._line) + ":" + self._message