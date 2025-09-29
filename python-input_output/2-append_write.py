#!/usr/bin/python3

def append_write(filename="", text=""):

    with open (filename,'w' ,encoding='utf-8') as file:
        content = file.write(text)
        return content
