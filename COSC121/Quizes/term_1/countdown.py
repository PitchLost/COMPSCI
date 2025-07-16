'''
Write a function countdown321(nums) that takes a list of one or more ints nums 
and returns True if the sequence 3, 2, 1 appears in the list somewhere and False 
otherwise. The numbers 3, 2, and 1 must appear contiguously, i.e. with no intervening 
numbers.
'''

def countdown321(nums):
    """checks if the sequence 3, 2, 1 is in a list"""

    new_nums = []
    for i in range(len(nums) - 2):
        new_nums.append(nums[i: i+3])
    
    return [3, 2, 1] in new_nums


print(countdown321([3, 3, 2, 1, 3]))
print(countdown321([3, 3, 2, 8, 3]))