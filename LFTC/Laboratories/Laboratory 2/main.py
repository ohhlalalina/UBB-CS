from SymbolTable import SymbolTable

if __name__ == "__main__":
    _symbolTable = SymbolTable()

    _symbolTable.add("N1")
    _symbolTable.add("N2")
    _symbolTable.add("AB")
    _symbolTable.add("BC")
    _symbolTable.add("N3")
    _symbolTable.add("A3")

    '''
    result = _symbolTable.search("N1")
    if result is None:
        print("None")
    else:
        print(result)

    result = _symbolTable.search("N4")
    if result is None:
        print("None")
    else:
        print(result)

    result = _symbolTable.search("15")
    if result is None:
        print("None")
    else:
        print(result)
        '''

    _symbolTable.print()