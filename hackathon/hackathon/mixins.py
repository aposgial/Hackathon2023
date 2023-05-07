import time

class ReversableList(list):
    def reverse(self):
        return list(reversed(self))

def calculate_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000
        print(f"Execution time: {execution_time:.2f} ms")
        return result
    return wrapper
