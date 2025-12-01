# python3 -m venv venv
# venv\Scripts\activate           (Windows)
# pip install requests numpy


# math_operations.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b

# string_utils.py

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)
# -----------------------------------------
# geometry/circle.py
# -----------------------------------------
# package module: geometry/circle.py

def calculate_area(radius):
    return 3.14159 * radius * radius

def calculate_circumference(radius):
    return 2 * 3.14159 * radius
# package module: file_operations/file_reader.py

def read_file(file_path):
    try:
        with open(file_path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "file not found"


# file_operations/file_writer.py

def write_file(file_path, content):
    with open(file_path, "w") as f:
        f.write(content)
    return "written"
