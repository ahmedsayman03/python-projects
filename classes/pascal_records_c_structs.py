class Employee:
    """Empty class is basically a record / C struct."""
    pass


# Fill fields of record
john = Employee()
john.name = 'John'
john.dept = 'computer lab'
john.salary = 1000


"""instance method objects have
m.__self__ 
    instance object with m() method

m.__function__
    function object corresponding to method"""
