import time
from functools import wraps
from django.core.cache import cache

def log_execution_time(func):
    @wraps(func)
    async def async_wrapper(*args, **kwargs):
        start = time.time()
        result = await func(*args, **kwargs)
        print(f"{func.__name__} executed in {time.time() - start:.2f} sec")
        return result
    return async_wrapper

def cache_result(key_prefix, timeout=3600):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            cache_key = f"{key_prefix}:{args}:{kwargs}"
            result = cache.get(cache_key)
            if not result:
                result = await func(*args, **kwargs)
                cache.set(cache_key, result, timeout)
            return result
        return wrapper
    return decorator