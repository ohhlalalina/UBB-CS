import re
from ScannerException import ScannerException


class ConstantValidator:
    '''
    Check if the received string is a constant using a regex expression
    @:param string
    @:return true - if the value is a number
             false - otherwise
    '''
    def is_valid(self, string):
        return re.search('^(0|[+-]?[1-9][0-9]*)$', string) is not None or re.match('^\".*\"$', string) is not None


class IdentifierValidator:
    """
    Creates a list of exceptions
    """
    def __init__(self):
        self.exceptions = []


    '''
    Checks is a string send as parameter is an identifier using a regex expression
    @:param string
    @:return true if the identifier begins with letter or upper case letter
    '''
    def is_valid(self, string):

        identifier = re.search(r"^[a-zA-Z]([a-zA-Z]){0,}([0-9]){0,}$", string)
        if identifier:
            return True
        else:
            self.exceptions.append(ScannerException(-1, "Constant or identifier contains mistakes!"))
        return False

    """
    Getter for the exceptions found
    """
    def get_scanner_exceptions(self):
        return self.exceptions


class StatementValidator:

    '''
    Validates every statement that we can obtain
    @:param tokens - list of tokens
    @:return scannerExceptions
    '''
    def get_errors(self, tokens):
        exceptions = []
        if self._get_statement(tokens) == "ReadStatement":
            print(tokens)
            if tokens[len(tokens)-1] != ";":
                exceptions.append(ScannerException(-1, "Missing semicolon at the end of statement!"))
            if tokens[2] != "scrie-ne":
                exceptions.append(ScannerException(-1, "Badly written scan statement!"))

        elif self._get_statement(tokens) == "WriteStatement":
            if tokens[len(tokens)-1] != ";":
                exceptions.append(ScannerException(-1, "Missing semicolon at the end of statement!"))
            if not("arata-ne" in tokens[0]):
                exceptions.append(ScannerException(-1, "Badly written show statement!"))

        elif self._get_statement(tokens) == "IfStatement":
            if not(tokens[0]) == "in_caz_ca" and not(tokens[0] == "in_caz_contrar") and not(tokens[len(tokens)-1] == "{"):
                exceptions.append(ScannerException(-1, "Badly written is statement!"))

        elif self._get_statement(tokens) == "ForStatement":
            if not(tokens[0] == "mergand"):
                exceptions.append(ScannerException(-1, "Badly written repeatill statement"))

        elif self._get_statement(tokens) == "ReturnStatement":
            if tokens[len(tokens) - 1] != ";":
                exceptions.append(ScannerException(-1, "Missing semicolon at the end of statement!"))
            if not(tokens[0]) == "trimite":
                exceptions.append(ScannerException(-1, "Badly written send statement!"))

        elif self._get_statement(tokens) == "DeclarationStatement":
            if tokens[len(tokens) - 1] != ";" and tokens[len(tokens) - 1] != "{":
                exceptions.append(ScannerException(-1, "Missing semicolon or { at the end of statement!"))
            if not(tokens[0] == "numar_intreg") and not(tokens[0] == "numar_real") and not(tokens[0] == "sir") and not(tokens[0] == "caracter") and not(tokens[0] == "asauf"):
                exceptions.append(ScannerException(-1, "Badly written declaration statement!"))

        elif self._get_statement(tokens) == "AssignmentStatement":
            if tokens[len(tokens) - 1] != ";":
                exceptions.append(ScannerException(-1, "Missing semicolon at the end of statement!"))
        else:
            pass

        return exceptions


    '''
    Does a regex search for every statement
    @:param tokens - list of string
    @:return return a string defining the type of the statement
    '''
    def _get_statement(self, tokens):
        line = ''
        for token in tokens:
            if token != ' ':
                line += token

        if re.search("^\w+=spune-ne\(\)(;)?", line):
            return "ReadStatement"

        elif re.search("^arata-ne(<<)\((\w+|\d+|\[\d+\]|\[(\d+,)+\d+\])\)(;)?", line):
            return "WriteStatement"

        elif re.search("^in_caz_ca\((\w+|\d+|[<>]|=:=|<=|/=|>=)+\)?({)", line):
            return "IfStatement"

        elif re.search("^in_caz_contrar({)?", line):
            return "IfStatement"

        elif re.search("^mergand\((\w+|\d+|[<>]|=:=|<=|/=|>=)+\)?", line):
            return "ForStatement"

        elif re.search("^trimite(\d+|\w+|[+\-*\/]|\[\d+\]|\[(\d+,)+\d+\])+(;)?", line):
            return "ReturnStatement"

        elif re.search("^(numar_intreg|caracter|sir|numar_real|asauf)(\w+|(numar_intreg|asauf|sir|caracter|numar_real)\[ \d+ \])(;)?", line):
            return "DeclarationStatement"

        elif re.search("^\w+=(\d+|\w+|[+\-*\/]|\[ \d+\]|\[(\d+,)+\d+\])+(;)?", line):
            return "AssignmentStatement"
        else:
            return "UnknownStatement"



