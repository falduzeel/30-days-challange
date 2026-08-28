print("Day 15: Error Handling and Decorators")

import time


def timer_decorator(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.5f} seconds")
        return result

    return wrapper


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    except TypeError:
        print("Error: Inputs must be numerical!")
        return None


@timer_decorator
def process_data_list(numbers):
    return [num**2 for num in numbers if isinstance(num, (int, float))]


print("Testing Safe Division:")
print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")

print("\nTesting Decorator Function:")
dataset = list(range(1, 100000))
processed_result = process_data_list(dataset)
print(f"Processed {len(processed_result)} items.")