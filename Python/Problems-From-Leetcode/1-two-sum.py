"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


def twoSum(nums, target):
    # most optimal
    indices = []
    # main logic : create tracker whilst iterating and checking for num and diff
    tracker = {}
    for i, num in enumerate(
        nums
    ):  # time:6*O(1)*N = 6*O(N) ~= O(N), space:7*O(1)*N ~= 7*O(N) ~= O(N)
        diff = target - num  # time: O(1), space:O(1)
        if diff in tracker:  # O(1), O(1)
            j = tracker[diff]  # O(1), O(1)
            indices.append((i, j))  # O(1), 2*O(1)
            del tracker[diff]  # O(1), O(1)
        else:
            tracker[num] = i  # O(1), O(1)
    return indices


if __name__ == "__main__":
    nums = [1, 5, 7, 9, 2, 6]
    target = 7
    # indices = two_sum_simple(nums, target)
    # indices = two_sum_traingular(nums, target)
    indices = twoSum(nums, target)
    print(indices)

# More Methods to solve but with less efficiency
'''
def two_sum_simple(nums, target):
    # Since we are searching for two elements in nums we are going to run for loops twice.
    indices = []  # time:O(1), space:2*O(N^2)
    for i, x in enumerate(nums):  # time:O(N), space:2*O(1)
        for j, y in enumerate(nums):  # time:O(N), space:2*O(1)
            if (
                x + y
            ) == target:  # time:2*O(1), space:2*O(1)[One variable will be created as the sum of x and y.Another boolean variable will be created from the comparison of sum and target.]
                indices.append((i, j))  # time:O(1), space:2*O(1)
    if not indices:  # time:O(1), space:O(1)
        print("No such pair found for {}".format(target))  # time:O(1), space:O(1)
    # time:O(1) + 2*O(N^2) + O(1) ~= O(N^2)
    # space:2*O(N^2) + 16*O(1) + O(1) ~= O(N^2)
    return indices


def two_sum_traingular(nums, target):
    # Loooking for a soln which is better than time:O(N^2)
    indices = []  # time:O(1), space:2*O(N^2)
    for i in range(len(nums)):  # time:O(N), space:2*O(1)
        x = nums[i]
        for j in range(i, len(nums)):  # time:O(N)/2, space:2*O(1)
            y = nums[j]
            if (
                x + y
            ) == target:  # time:2*O(1), space:2*O(1)[One variable will be created as the sum of x and y.Another boolean variable will be created from the comparison of sum and target.]
                indices.append((i, j))  # time:O(1), space:2*O(1)
    if not indices:  # time:O(1), space:O(1)
        print("No such pair found for {}".format(target))  # time:O(1), space:O(1)
    # time:O(1) + 2*O(N^2) + O(1) ~= O(N^2) /2 ~= O(N^2)
    # space:2*O(N^2) + 16*O(1) + O(1) ~= O(N^2)
    return indices

'''