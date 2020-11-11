

class CodificationTable:

    "CREATES A DICTIONARY FOR THE RESERVED SIGNS AND WORDS"
    def __init__(self):
        self.dictionary = {
            "+" : 110,
            "-" : 111,
            "^" : 112,
            "*" : 113,
            "<" : 114,
            "/" : 115,
            "<<":900,
            ">>":901,
            "=" : 116,
            "==":902,
            ">" : 117,
            "\\" : 118,
            "!" : 119,
            "divide" : 120,
            "mod" : 121,
            "not" : 122,
            "[" : 220,
            "]" : 905,
            "{" : 221,
            "}" : 226,
            ",":800,
            "(" : 801,
            ")" : 802,
            ":" : 223,
            ";" : 224,
            "space" : 225,
            "numar_intreg" : 330,
            "caracter" : 331,
            "constant" :332,
            "numar_real" : 333,
            "sir" : 334,
            "asauf" : 335,
            "executa" : 440,
            "in_caz_contrar" : 441,
            "in_caz_ca" : 442,
            "mergand" : 443,
            "arata_ne" : 444,
            "trimite" : 445,
            "scrie_ne" : 446,
            "in_timp_ce" : 447,
            "da_valoarea" : 448,
            "atunci" : 449,
            "and" : 450,
            "++": 451,
            "IDENTIFIER": 0,
            "CONSTANT": 1,
            "main" : 1000
        }

    "CHECKS IF A TOKEN IS AN IDENTIFIER OR CONSTANT, BY CHECKING IF IT IS IN THE DICTIONARY" \
    "WITH RESERVED WORDS" \
    "@return: IF IT IS NOT IN THE DICTIONARY, RETURNS TRUE; ELSE FALSE" \
    "@param: RECEIVES AS PARAMS THE TOKEN THAT WE WILL CHECK"
    def is_identifier_or_constant(self, token):
        try:
            value = self.dictionary[token]
            return False
        except KeyError:
            return True

    """
    Searches for the code of a token 
    @:param token - the token for whom we search the code
    @:return the code of the token
    """
    def get_token_code(self, token):
        return self.dictionary[token]
