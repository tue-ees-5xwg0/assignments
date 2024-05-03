def double(x):
    return x * 2  # Pure Function: No side effects, always returns the same output for the same input.


def square(x):
    return x ** 2  # Pure Function: No side effects, always returns the same output for the same input.


def apply_function(func, arg):
    return func(arg)  # Higher-order Function: Accepts another function as an argument.


result1 = apply_function(double, 5)  # Output: 10 - Function applied to argument.
result2 = apply_function(square, 3)  # Output: 9 - Function applied to argument.

print(result1)
print(result2)

# Functions as First-Class Citizens: Functions can be assigned to variables, passed as arguments, and returned from other functions.
add = lambda x, y: x + y
print(add(3, 4))  # Output: 7 - Using a lambda function as a first-class citizen.

# Immutability: Although Python allows mutable data types, functional programming encourages immutability.
# We can achieve immutability by avoiding modifying existing data and instead returning new data.
data = 5  # Immutable integer
new_result1 = apply_function(double, data)  # Output: 10 - Function applied to immutable data.
new_result2 = apply_function(square, data)  # Output: 25 - Function applied to immutable data.

print(new_result1)
print(new_result2)
