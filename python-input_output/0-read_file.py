#!usr/bin/python3

class Reading():
    def read_file(filename=""):
        with open (filename, encoding='utf-8') as a_file:
            content = filename.read()
