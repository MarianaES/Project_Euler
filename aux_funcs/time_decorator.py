from functools import wraps
from time import time

def timer(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        print(f'Elapsed time {f.__name__}: {end-start}')
        return result
    return wrapper
