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
        f = open("prerr.out", "w")
        f.close()
        file = open(self._file_path, "r")
        lines = file.readlines()
        for line in lines:
            current_line += 1
            line = self.trim_line(line)
            tokens = line.split(' ')
            f = open("prerr.out", "a")
            for tok in tokens :
                if tok == '':
                    tokens.remove('')
                f.write(tok)
                f.write("\n")
            f.close()
            print(tokens)
            exceptions = statement_validator.get_errors(tokens)
            for exception in exceptions:
                exception.set_line(current_line)
                self._scanner_exceptions.append(exception)
            for token in tokens:
                self._scanner_exceptions.extend(self._pif.add_to_pif(token, current_line))

        f = open("prerr.out", "a")
        f.write("PIF" + "\n")
        for el in self._pif.get_pif():
            string = "" + str(el[0]) + " : " + str(el[1])+"\n"
            f.write(string)
        f.write("Symbol table" + "\n")
        for scanner_exception in self._scanner_exceptions:
            if scanner_exception != []:
                f.write(str(scanner_exception) + "\n")
        f.close()
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
        elems = [",", "(", ")", "{", "[", "]", "-", "++", "--", "+"]
        for e in elems:
            line = line.replace(e, " " + e+ " ")
        if line[0] != "}":
            line = line.replace("}", ' }')
        line = line.replace("  ", ' ')
        return line