from SymbolTable import SymbolTable
from Scanner import *
from PIF import *


def generate_dict(file):
    f = open(file, "r")
    dict = {}
    for line in f:
        l = line.split(" ")
        dict[l[0]] = l[1][:-1]
    return dict


if __name__ == '__main__':
    token = generate_dict("specification.in")
    file = open('input.txt', 'r')
    st = SymbolTable()
    pif = PIF()
    line_index = 0

    actual_string = ""

    while file is not None:
        while file.read(1) != " ":
            actual_string.join(file.read(1))
        if Scanner.is_identifier(actual_string):
            pif.insert(0, actual_string)
            actual_string = ""
        elif Scanner.is_constant(actual_string):
            pif.insert(1, actual_string)
            actual_string = ""
        elif actual_string in token.keys():
            st.add(actual_string)
            pos = st.search(actual_string)
            pif.insert(pos, actual_string)
            actual_string = ""
        else:
            print("Unknown token '{}'!".format(actual_string))

