def two_sum(nums, target):
    numbers = {}
    for i, j in enumerate(nums):
        difference = target - j
        if difference in numbers:
            return i, numbers[difference]
        else:
            numbers[j] = i


tgt = 9
numbs = [2, 7, 11, 15]

print(two_sum(numbs, tgt))  # expected output: [0, 1] or [1, 0]
