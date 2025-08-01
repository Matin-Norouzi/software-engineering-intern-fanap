# This function finds the most frequent number in a list
def most_frequent(nums : list):
    max_count = 0
    most_common = None
    for num in nums:
        count = nums.count(num)
        if count > max_count:
            max_count = count
            most_common = num
    return most_common
print(most_frequent([1, 2, 3, 2, 4, 2, 5]))  # خروجی: 2