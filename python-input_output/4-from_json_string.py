#!/usr/bin/python3
#!/usr/bin/python3
"""Append a string to a text file and return char count"""


def append_write(filename="", text=""):
    """Append text and return number of characters added"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
