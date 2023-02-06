'''Define a class which has at least two methods: 
getString: to get a string from console input 
printString: to print the string in upper case.'''

class String:
    def __init__(self):
        pass
    def get_string(self):
        self.str = input()
    def print_string(self):
        self.str = print(self.str.upper())

string = String()
string.get_string()
string.print_string()


