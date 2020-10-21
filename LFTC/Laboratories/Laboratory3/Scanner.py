import re


class Scanner:

    @staticmethod
    def is_identifier(token):
        # Combination of numbers, letters and
        # But the first character must be a letter
        return re.match(r"^[a-zA-Z]([a-zA-Z]|[0-9])$", token) is not None

    @staticmethod
    def is_constant(token):
        # Integer or string between "" or character between ''
        return re.match('^(0|[-]?[1-9][0-9]*)$', token) is not None or re.match('^\".*\"$', token) is not None \
               or re.match('^\'.*\'$', token) is not None

    @staticmethod
    def is_operator(token):
        # Could also be part of operator
        # e.g. <, <=
        return token in ["<", "/", ">", "\\", "=", "!"]

