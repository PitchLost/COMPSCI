'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
'''
def intersection_of_two_arrays(nums1, nums2):
    return list(set(nums1).intersection(set(nums2)))


nums1 = [4,9,5] 
nums2 = [9,4,9,8,4]
print(intersection_of_two_arrays(nums1, nums2))
