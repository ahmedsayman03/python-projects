class MyClass:
    """Classes have statements (normally function definitions)

    A class has it's own namespace, local var assignments go to this namespace

    when class definition is done (object created), local scope goes back to original scope with the class object
    in the new local scope
    """
    i = 43

    def __init__(self, x, y):
        """To make objects have initial state, use this function

        Obj creation / class instantiation invokes this automatically for newly created instance"""
        self.data = []
        self.x = x
        self.y = y

    def f(self):
        """self is the instance object. obj.f is same as MyClass.f(obj)

        Calling f method with arguments is = calling f with obj inserted as first argument"""
        print('hello world')

    def f_twice(self):
        """Calls another function in the class using self."""
        self.f()
        self.f()

    # obj.i
    # obj.f  # a function object


# Create class instance / obj
mc = MyClass(2, 4)
print(mc.x)
print(mc.y)
print(mc.i)


# Instance objects only understand attribute names
# attribute names: attributes, methods

# Add attribute
mc.test = 3
print(mc.test)

# method belongs to obj
# class function objs are methods for instance obj
mc.f()  # method object, not a function objection
mc.f_twice()

# Classes (function objects)
# instances (method objects)
