"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""



def twoSum(nums, target):
    num_dict = {}

    for index, num in enumerate(nums):
        # Save a dictionary of number iterations with indices
        num_dict[num] = index


    for index, num in enumerate(nums):
        # Locate the second number
        second_number = target - num

        if index == num_dict.get(second_number):
            continue

        if second_number in num_dict.keys():
            # print('found ', num, second_number)
            print(index, num_dict.get(second_number))
            return [index, num_dict.get(second_number)]
    print(num_dict)


# Testcase for twosum
twoSum([1,2,3,4,5,6], 6)