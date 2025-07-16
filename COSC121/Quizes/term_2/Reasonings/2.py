'''Find a value for silly2() so it outputs:
2 2
We're dead, Fred
'''

def silly2(nums, indices, extra=None):
    print(len(nums), len(indices))

    new_indices = []
    for i in indices:
        if i >= 0 and i < len(nums):
            new_indices.append(i)

    if extra is not None:
        new_indices.append(extra)

    try:
        for index in new_indices:
            if index < len(nums):
                print(nums[index])
    except IndexError:
        print("We're dead, Fred")
        
silly2()