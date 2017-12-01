import time


TIME_FORMAT = "%b %d %Y - %H:%M:%S"


def timer_format(time_format=TIME_FORMAT):
    def decorator(func):
        def decorated_func(*args, **kwargs):
            print("- Running '{}' on {}".format(
                func.__name__,
                time.strftime(time_format)
            ))
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print("- Finished '{}', execution time = {}'s ".format(
                func.__name__,
                end - start
            ))
            return result
        return decorated_func
    return decorator
