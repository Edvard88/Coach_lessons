from functools import wraps
from functools import lru_cache


def my_cache(maxsize=50):
    """ Cache for call our fucntion
    input:
        * maxsize - max size cache
    output:
        * hits - hit in cache
        * misses - miss cache value
        * currsize - current size of cahce

    """

    def _my_cache(func):
        cahe_dict = {}

        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Enter wrapper")

            if args in cahe_dict:
                wrapper.hits += 1
                wrapper.currsize += 1
                print("Get out from cache function with args", *args)
                return cahe_dict[args]
            else:
                if len(cahe_dict) <= wrapper.maxsize:
                    print("Put in cache function with args", *args)
                    cahe_dict[args] = func(*args, **kwargs)
                    wrapper.misses += 1
                    return func(*args, **kwargs)
                else:
                    exit("Cahce is full")

        def cache_info():
            print(
                f'''Current fuction results:  hits {wrapper.hits}, , misses {wrapper.misses}, maxsize {wrapper.maxsize}, currsize {wrapper.currsize}''')

        wrapper.cache_info = cache_info

        wrapper.maxsize = maxsize
        wrapper.hits = 0
        wrapper.misses = 0
        wrapper.currsize = 0

        return wrapper

    return _my_cache


@my_cache(maxsize=50)
def Fib(n):
    """Fibonacci function

    Fibonacci function - is the fuction with difficult calculation
    F1 = 0
    F2 = 0
    Fn = Fn-1 + Fn-2

    """
    print("Fib enter")

    if (n == 1) or (n == 2):
        return 1
    else:
        return Fib(n - 1) + Fib(n - 2)


Fib.__dict__['__wrapped__'](3)


