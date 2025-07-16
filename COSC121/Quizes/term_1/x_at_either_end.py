def x_at_either_end(param):
    '''
    Write a function x_at_either_end(string) that takes a string string as a parameter, 
    which may be empty, and returns a boolean. 
    It returns True if and only if the string 
    string starts or ends with the lower-case character x.
    We recommend using the startswith and endswith methods of str.'''


    return param.startswith('x') or param.endswith('x')

x_at_either_end('')
print(x_at_either_end('xylophone'))
print(x_at_either_end('rex'))
print(x_at_either_end('hello'))