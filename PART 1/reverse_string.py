# This function takes a string and returns its reverse
def reverse_string(s : str):
    result = ""
    for char in s:
        result = char + result
    return result
print(reverse_string("Hello, World!"))  # خروجی: !dlroW ,olleH