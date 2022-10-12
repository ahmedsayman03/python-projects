def json():
    """JSON (JavaScript Object Notation) (data interchange format) serialization."""

    # reading / writing strings, easy
    # with numbers, you have to convert to int() when reading, convert to str() when writing
    # complicated, especially when working with complex data types like dicts or nested lists

    # json - standard module
    # converts python data-types to strings (serialization)
    # string representation to data-type (deserialization)

    import json
    print(json.dumps([1, 'simple', 'list']))

    # json.dump(x, f)
    # dump serialized string x into text file open for writing f

    # to decode
    # x = json.load(f)
    # f is a text-file object



json()

