def namespace():
    """Namespace:
    map: name -> obj
    implementation: python dicts
    e.g. set of attributes of an obj form namespace

    names in different namespaces have no relation
    e.g. two modules, same function name, just prefix it with module name

    attributes are read only or writable. writable attributes can be deleted.
    e.g.
    modname.answer = 42
    del modname.answer
    # deletes attribute answer for that object

    namespaces created at different times, last different times too
    e.g.
    module namespace created when mod file read, and ends when interpreter session ends

    for function, namespace created when called, deleted when function returns or raises exception

    difference between scope and namespace:
    function scope is function and module, function namespace is just the function"""

    pass
