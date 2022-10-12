def predefined_cleanup():
    """Some objects have standard cleanup operations.

    e.g.
    for line in open("myfile.txt"):
        print(line, end="")

    file is remained open.

    with allows objects (files) to close properly after use regardless of success

    with open("myfile.txt") as f:
        for line in f:
            print(line, end="")

    f file is always closed regardless of error in the above code.

    Objects like files that have predefined cleanup methods have it written in the documentation.
    """
