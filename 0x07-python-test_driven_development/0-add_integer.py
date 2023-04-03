#!/usr/bin/python3
    """ 
    Adding the sum of two integers.
    """


    def add_integer(a, b=98):
        """Return the sum of two int or two float.
        Args:
            a:first argument.Must be an integer else throw an error.
            b:second argument.default int =98.
        
        Returns:sum of two integers or float.

        Raises:Type error
        """
        if type (a) is int or type (a) is float:
            if type (b) is int or type (b) is float:
                return int(a+b)
            else:
                raise TypeError("b must be an integer or float")
        else:
            raise TyperError ("a must be an integer or float")

