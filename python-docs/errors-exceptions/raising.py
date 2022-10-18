def raising():
    """Raising errors."""

    raise NameError('Hello There')

    # If an Exception Class is passed to raise, it calls the classes constructor
    raise ValueError  # shorthand for 'raise ValueError()'


def add_to_error():
    """If you want to know if exception raised but not handle it, just use raise."""
    try:
        raise NameError('Hello There')
    except NameError:
        print('Just want to add this to the error')
        raise


add_to_error()
