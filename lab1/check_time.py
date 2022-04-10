import time

def check_time(func):
    def wrapper(*arg, **kw):
        t1 = time.process_time()
        list_sorted = func(*arg, **kw)
        t2 = time.process_time()
        return ((t2 - t1),list_sorted)
    return wrapper
