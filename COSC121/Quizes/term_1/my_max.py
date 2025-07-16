'''
Use the accumulator pattern to write a function my_max(data),
 which returns the maximum number in the list data. You may 
 assume the list data contains at least one number. You are not 
 allowed to use the max function. It is not necessary to sort the 
 data and any calls to sort or sorted are disallowed.
 '''

def my_max(data):
    '''Pre nasty code tbh'''
    max_num = data[0]
    for number in data:
        if number > max_num:
            max_num = number
    return max_num

print(my_max([11, 99, 3, -6]))
print(my_max([-3, -5, -9, -10]))