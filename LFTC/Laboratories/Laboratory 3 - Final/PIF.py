from CodificationTable import CodificationTable
from ScannerException import ScannerException
from Validators import *


class PIF:
    """
    Creates a list in which we will add the token coresponding to PIF
    @:param symbol_table - the table that we will use
    """
    def __init__(self, symbol_table):
        self._pif = []
        self._symbol_table = symbol_table

    """
    Checks whether there token is an identifier or constant of statement and adds it to the list after 
    validating and adding it to the symbol table
    @:param token, string that gives the current token to be scanned
    @:param current_line - int - gives the current line of the file
    @:return scannerExceptions - returns a list of ScannerExceptions
    """
    def add_to_pif(self, token, current_line):
        codification_table = CodificationTable()
        constant_validator = ConstantValidator()
        identifier_validator = IdentifierValidator()
        scanner_exceptions = []

        if codification_table.is_identifier_or_constant(token):
            if constant_validator.is_valid(token):
                identifier_id = self._symbol_table.get_identifier_id(token)
                if identifier_id != -1:
                    self._pif.append([0, identifier_id])
                else:
                    self._symbol_table.add(token)
                    self._pif.append([0, self._symbol_table.get_identifier_id(token)])
            elif identifier_validator.is_valid(token):
                identifier_id = self._symbol_table.get_identifier_id(token)
                if identifier_id != -1:
                    self._pif.append([1, identifier_id])
                else:
                    self._symbol_table.add(token)
                    self._pif.append([1, self._symbol_table.get_identifier_id(token)])
            else:
                scanner_exceptions = identifier_validator.get_scanner_exceptions()
                for error in scanner_exceptions:
                    error.set_line(current_line)

        else:
            try:
                token_id = codification_table.dictionary[token]
                self._pif.append([token_id, token])
            except Exception:
                exception = ScannerException(current_line,  "")
                scanner_exceptions.append(exception)

        for exception in scanner_exceptions:
            exception.set_line(current_line)
        return scanner_exceptions

    """
    Returns the PIF list
    @:return self._pif
    """
    def get_pif(self):
        return self._pif
