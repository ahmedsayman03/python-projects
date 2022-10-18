class A(B):
    """This code does not run. It's just for learning.

    class A(modname.B): # Also works
    B has to be in the scope.

    Checking for attribute? Check A first. Not there? Check B next. because B base class is remembered.

    Not B? Check base class of B. etc.

    """

    def f(self):
        """an override methods in B. Suppose f is in B, A can override it.
        Can also extend it.

        For A to call B method, do B.method(self, args)"""

    """Python has 2 built in inheritance functions.
    1) isinstance(obj, int)
    checks if obj is int or derived from int
    
    2) issubclass(bool, int) True because bool subclass of int
    issubclass(float, int) False because float not sublass of int"""
