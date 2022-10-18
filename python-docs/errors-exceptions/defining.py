class Error(Exception):
    """Base class for exceptions in this module."""
    # Simple inherit the Exception class to define your own exceptions
    pass


class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

# Most Exceptions have names that end with 'Error'
