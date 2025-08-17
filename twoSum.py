"""
Given an array of integers nums and an integer target, return indices of the two numbers such that 
they add up to target. You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.
"""

def twoSum(nums, target):

    for i in range(len(nums)):
        rem = target - nums[i]
        if rem in  nums:
            j = nums.index(rem)
            if i != j:
                return [i, j]
    return []

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 260
    result = twoSum(nums, target)
    print(result)  # Expected output: [0, 1] or [1, 0] since nums[0] + nums[1] == 9