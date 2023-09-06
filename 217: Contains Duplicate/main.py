def contains_duplicate(nums):
    set_nums = {}
    for num in nums:
        if num not in set_nums:
            set_nums[num] = 1
        else:
            return True

    return False


numbers = [1, 1, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 3, 1]
numbers_3 = [1, 2, 3, 4, 5]

print(contains_duplicate(numbers))  # expected output: True

print(contains_duplicate(numbers_2))  # expected output: True

print(contains_duplicate(numbers_3))  # expected output: False

