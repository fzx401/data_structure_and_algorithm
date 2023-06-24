import time
from functools import wraps

#  类装饰器（函数替换）
class timer:
    def __init__(self, print_args: bool):
        self.print_args = print_args

    def __call__(self, func):
        @wraps(func)
        def decorated(*args, **kwargs):
            st = time.perf_counter()
            ret = func(*args, **kwargs)
            if self.print_args:
                print(f'{func.__name__}, args: {args}, kwargs: {kwargs}')
            print(f'time cost: {time.perf_counter() - st} seconds')

            return ret

        return decorated


@timer(True)
def print_hhh():
    print('hhh')

print_hhh()
#  类装饰器（实例替换）
class DelayedStart:
    def __init__(self, func):
        @wraps(func)
        self.func = func

