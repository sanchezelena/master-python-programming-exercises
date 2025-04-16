# Your code here
class InputOutString: 
    def __init__(self):
        self.text = ""

    def get_string(self):
        self.text = input("Cual es tu nombre? ")

    def print_string(self):
        print(self.text.upper())

nombre = InputOutString()
nombre.get_string()
nombre.print_string()