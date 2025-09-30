import os
import psutil
from time import time

from flemmarr.logger import setup_logging

logger = setup_logging(__name__)
logger.debug(f"Logger initialized for {__name__} module")

base = 1024
kilobyte = base
megabyte = kilobyte * base


# inner psutil function
def process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss


def profile(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        mem_before = process_memory()
        result = func(*args, **kwargs)
        t2 = time()
        mem_after = process_memory()
        logger.debug(f"Function {func.__name__!r} executed in {(t2 - t1):.4f}s")
        logger.debug(
            f"Function {func.__name__!r} consumed memory: {((mem_after - mem_before) / megabyte)} MB"
        )

        return result

    return wrap_func
