def cleanup():
    """try has a finally clause that runs regardless of error or not."""
    while True:
        try:
            # break  # Note: If try reaches break continue return, finally will execute right before it
            raise KeyboardInterrupt
        except KeyboardInterrupt:
            raise
        finally:
            print('Clean up, always runs even if error')
            # Note: Exception is reraised after finally is executed, regardless of it is
            # caught with an except clause
            # Note: If return value here and in try clause, this return value is used


cleanup()

# In the real world, finally is useful for closing connections, releasing external resources regardless of success.
