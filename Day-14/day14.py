from functools import reduce


def add_ten(x):
    return x + 10


add_ten_lambda = lambda x: x + 10

print("Lambda Addition:", add_ten_lambda(5))

multiply = lambda a, b: a * b
print("Lambda Multiplication:", multiply(4, 6))


numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda x: x ** 2, numbers))
print("\nOriginal Numbers:", numbers)
print("Squared Numbers (map):", squared_numbers)


numbers_list = [10, 15, 20, 25, 30, 35, 40]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers_list))
print("\nAll Numbers:", numbers_list)
print("Even Numbers (filter):", even_numbers)


data = [1, 2, 3, 4, 5]

total_sum = reduce(lambda acc, current: acc + current, data)
print("\nData List:", data)
print("Total Sum (reduce):", total_sum)

max_value = reduce(lambda a, b: a if a > b else b, data)
print("Maximum Value (reduce):", max_value)


def apply_operation(func, values):
    return [func(val) for val in values]

def uppercase(text):
    return text.upper()

words = ["python", "day", "fourteen", "coding"]
transformed_words = apply_operation(uppercase, words)

print("\nOriginal Words:", words)
print("Transformed Words:", transformed_words)