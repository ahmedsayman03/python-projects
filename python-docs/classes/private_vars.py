class A:
    """Private vars do not exist in python (vars that can't be accessed from outside an object, only inside).

    _spam can be used, but it is basically just seen as an implementation detail (subject to change)

    __update() = _classname__update()
    This is used to avoid name clashes.

    So multiple inheritance methods can have __update() without a name clash since __update() turns into
    _classname__update()"""
