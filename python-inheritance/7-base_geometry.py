#!/usr/bin/python3
"""Public Instance Method """
class BaseGeometry:
    """Public instance method: def area(self): that raises an Exception with the message area() is not implemented"""    
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Validates that value is an integer greater than 0.

        Args:
            name (str): the name of the value (always a string).
            value: the value to validate.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
