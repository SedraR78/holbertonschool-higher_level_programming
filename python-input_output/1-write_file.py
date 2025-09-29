#!usr/bin/python3

"""Function that writes a file """
def write_file(filename="", text=""):
    
     with open (filename,'w' ,encoding='utf-8') as file:
        content = file.write(text)
        return content
