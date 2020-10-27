from SymbolTable import SymbolTable
from PIF import PIF
from Validators import StatementValidator


class Scanner:
    """
    Creates a list of scanner exceptions, a new symbol table and using the symbol table, a PIF.
    Also, the path of the file to scan
    """
    def __init__(self):
        self._scanner_exceptions = []
        self._symbol_table = SymbolTable()
        self._pif = PIF(self._symbol_table)
        self._file_path = "input.txt"

    """
    Reads the file line by line and trims the whitesapces between each statement
    @:return prints the Scanner Exceptions if there are any and the Program Internal Form
    """
    def scan_file(self):
        current_line = 0
        statement_validator = StatementValidator()

        file = open(self._file_path, "r")
        lines = file.readlines()
        for line in lines:
            current_line += 1
            line = self.trim_line(line)
            tokens = line.split(' ')
            print(tokens)
            exceptions = statement_validator.get_errors(tokens)
            for exception in exceptions:
                exception.set_line(current_line)
                self._scanner_exceptions.append(exception)
            for token in tokens:
                self._scanner_exceptions.extend(self._pif.add_to_pif(token, current_line))

        print("PIF", self._pif.get_pif())
        print("Symbol table")
        self._symbol_table.print()
        for scanner_exception in self._scanner_exceptions:
            if scanner_exception != []:
                print(scanner_exception)

    """
    Replaces the whitespaces for the line
    @:param line - string line from file
    @:return line - line trimmed
    """
    def trim_line(self, line):
        line = str.lstrip(line)
        line = line.replace("\n", '')
        if ";" in line:
            line = line.replace(";", '')
            line += ' ' + ';'
        line = line.replace(",", ' ,')
        line = line.replace("(", ' ( ')
        line = line.replace(")", ' )')
        line = line.replace("{", ' {')
        line = line.replace("[", ' [ ')
        line = line.replace("]", ' ]')
        line = line.replace("++", ' ++')
        if line[0] != "}":
            line = line.replace("}", ' }')
        line = line.replace("  ", ' ')
        return line