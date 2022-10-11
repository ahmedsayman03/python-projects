def pyc_cache():
    """Explains why python creates .pyc files and pycache directory (compiled files load faster)."""

    # .pyc are compiled files
    # Python caches compiled version of each module in __pycache__ directory.
    # modname.pythonversion.pyc
    # This speeds up loading modules.

    # Python checks if modification date == compiled file date
    # to see if the .pyc file is up-to-date.

    # .pyc files load faster, not run faster.
