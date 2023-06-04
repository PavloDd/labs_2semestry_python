from functools import wraps
import logging
import os


def logged(exception, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                log_file = 'exception.log'
                if os.path.exists(log_file):
                    os.remove(log_file)

                logger = logging.getLogger("exception_logger")
                logger.setLevel(logging.INFO)
                handler = None

                if mode.__eq__("console"):
                    handler = logging.StreamHandler()

                if mode.__eq__("file"):
                    handler = logging.FileHandler("exception.log")

                if handler:
                    logger.addHandler(handler)
                    logger.exception('Exception occurred: %s', str(e))
                    logger.removeHandler(handler)
        return wrapper
    return decorator


def count_args(func):
    """
    Decorator that counts the number of arguments passed to a function and prints the count.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The decorated function.
    """
    @wraps(func)
    def inner(*args, **kwargs):
        count = len(args) + len(kwargs)
        print(f"{func.__name__} accepts {count} args")
        return func(*args, **kwargs)
    return inner


def calls_limit(func):
    """
    Decorator that limits the number of times a function can be called.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The decorated function.
    """
    calls = 0

    def inner(*args, **kwargs):
        nonlocal calls
        if calls < 3:
            calls += 1
            return func(*args, **kwargs)
        else:
            print(f"{func.__name__} was called too many times")
            return None
    return inner
