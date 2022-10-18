def handling():
    """Handling exceptions."""

    while True:
        try:
            x = int(input('Enter number: '))

        # Only if this exception occurs, run code below
        except ValueError:
            print('Not number')

        # If a different exception, it checks outside of try statement
        # If unhandled, execution stops, unhandled exception

        except (RuntimeError, TypeError, NameError):  # Tuple of Exceptions
            pass

        # Runs if try is good with no exceptions
        else:
            print('Nice, thanks')
            break


def exception_args():
    """Exceptions have arguments for clarity. You can access them by printing the exception or doing Exception.args"""

    try:
        raise Exception('spam', 'eggs')
    except Exception as inst:
        print(type(inst))  # Exception
        print(inst.args)   # arguments stored in .args, spam eggs
        print(inst)        # __str__ allows args to be printed directly, so spam eggs
                           # but may be overridden in exception subclasses

        x, y = inst.args  # unpack args

        print('x =', x)   # spam

        print('y =', y)   # eggs


def my_er():
    """An error (cannot divide by 0). Used to demonstrate that try errors if the function it calls raises an error."""
    x = 1/0


def my_er_f():
    """Calls a function that raises an error. The except clause in this function catches it."""
    try:
        my_er()
    except ZeroDivisionError:
        print('error')


my_er_f()
