
class FiniteAutomata:
    @staticmethod
    def parseLine(line):
        return [value.strip() for value in line.strip().split(',')]


    '''
    Reads line by line from the file:
    first line shoul contain all states separated by ,
    second line should contain the alphabet(separated by , )
    third line should contain the initial state
    fourth line should contain the final states separated by ,
    from the fifth line til the end of the file should be the transition under the form : 
    
        the state we start from + ',' value + '=' + the state in which we will arrive
    '''
    def fromFile(self,fileName):
        with open(fileName) as file:
            self.Q = FiniteAutomata.parseLine(file.readline())
            self.E = FiniteAutomata.parseLine(file.readline())
            self.q0 = file.readline()
            self.F = FiniteAutomata.parseLine(file.readline())
            self.S = []
            i=-1
            with open(fileName) as openfileobject:
                for line in openfileobject:
                    i = i + 1
                    if i > 3:
                        self.S.append(line.strip())
            self.S = FiniteAutomata.parseTransitions(self.S)

    """
    Here we create a dictionary that has as keys the states, and as value, a list with dictionaries
    having as keys values from the alphabet, and as values the states in which we will arrive
    """
    @staticmethod
    def parseTransitions(parts):
        result = {}
        for line in parts:

            key = line.split(",")
            value = key[1].split("=")
            key = key[0]
            if key in result.keys():
                result[key].append({value[0]:value[1]})
            else:
                result[key]=[{value[0]:value[1]}]

        print(result)
        return result

    def __init__(self):
        self.Q = None
        self.E = None
        self.S = None
        self.q0 = None
        self.F = None
        self.fromFile("automata.txt")
        while True:
            self.menu()

    """
    Prints all the states as a list
    """
    def printStates(self):
        print(self.Q)

    """
    Prints the alphabet as a list
    """
    def printAlphabet(self):
        print(self.E)

    """
    Prints the transitions as a dictionary
    """
    def printTransition(self):
        print(self.S)

    """
    Prints the final states as a list
    """
    def printFinalStates(self):
        print(self.F)

    """
    Checks if a state is final
    """
    def finalState(self, state):
        if state in self.F:
            return True
        return False

    def verifySeq(self, seq):
        currentState = self.q0[0]
        dict = self.S
        while len(seq)!= 0 or not self.finalState(currentState):
            value = seq[0]
            for element in dict[currentState]:
                for key, v in element.items():
                    if int(key) == int(value):
                        currentState = value
                        seq = seq[1:]
                        break

        if len(seq) == 0 and currentState.finalState():
            return 1
        return 0


    def menu(self):
        print("Select your choice\n")
        print("Press 1 to see the set of states\n")
        print("Press 2 to see the alphabet\n")
        print("Press 3 to see the final states\n")
        print("Press 4 to see the transitions\n")
        print("Press 5 to see if a sequence is accepted by the FA\n")

        choice = input()
        if int(choice) == 1:
            self.printStates()
        elif int(choice) == 2:
            self.printAlphabet()
        elif int(choice) == 3:
            self.printFinalStates()
        elif int(choice) == 4:
            self.printTransition()
        elif int(choice) == 5:
            x = input("Input sequence:\n")
            res = self.verifySeq(x)
            if res == 1:
                print("Sequence accepted by the FA\n")
            else:
                print("Sequence not accepted by the FA\n")
        else:
            print("Wrong input!")


if __name__ == "__main__":
    fa = FiniteAutomata()
