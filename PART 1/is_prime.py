# این تابع بررسی می‌کند که آیا یک عدد اول است یا خیر
def is_prime(n : int):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(is_prime(7))  # خروجی: True
print(is_prime(10))  # خروجی: False
print(is_prime(1))  # خروجی: False