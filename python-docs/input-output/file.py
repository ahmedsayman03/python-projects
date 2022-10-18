def file():
    """Reads and writes to file."""

    # READ

    # File name, mode (write, read, append, both)
    # f = open('workfile', 'w')

    # use with
    # It closes the file regardless of exceptions, basically "try-finally f.close()"
    # with open('workfile', 'w') as f:
    #     read_data = f.read()
    # f.closed()

    # To read file:
    # f.read(size)
    # size is chars
    # f.read() reads the whole thing
    # '' (empty string) if end reached

    # f.readline()
    # reads line
    # each line has a /n at the end except when the end of the file is reached
    # '' is returned at the end

    # for loop over to read line by line
    # for line in f:
    #   print(line, end='')

    # to put all lines in a list
    # f.readlines()
    # list(f)

    # WRITE
    # f.write('This is a test\n')
    # returns how many chars is written
    # 15
    # Whatever is written has to be converted to a string - use str(42)

    # f.tell()
    # returns integer location of file

    # f.seek(offset, whence)
    # Moves position of file using whence (0 beginning, 1 current, 2 end) and offest.

    # f = open('workfile', 'rb+')
    # >> > f.write(b'0123456789abcdef')
    # 16
    # >> > f.seek(5)  # Go to the 6th byte in the file
    # 5 # position 5
    # >> > f.read(1)
    # b'5' # what's at current position?
    # >> > f.seek(-3, 2)  # Go to the 3rd byte before the end
    # 13 # position 13
    # >> > f.read(1)
    # b'd' # what's at position 13 / current position?
