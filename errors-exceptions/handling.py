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
    x = 1/0


def my_er_f():
    try:
        my_er()
    except ZeroDivisionError:
        print('error')


my_er_f()
