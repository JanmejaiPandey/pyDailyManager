import os

class Align:
    @staticmethod
    def centerAlign(string):
        width = os.get_terminal_size().columns
        print(string.center(width))
