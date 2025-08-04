'''Simple program for processing trace files to test arrays.'''
# Import all three classes so we can test them all
# Remember the sorted array won't count anything until you add your code
import sys
import time

from arrays import LinearArray, SortedArray, BitVectorArray

# NOTE: We recommend running in Python v3.8 or later to be consistent with
# lab machines.

# Get the time units given by the perf_counter
# Note: time.clock has been deprecated in Python 3.3
# and replaced with the more precise perf_counter method
# time.perf_counter returns time as seconds since some arbitrary time
# so only the difference between two times is useful...
REZ = time.get_clock_info('perf_counter').resolution
print('Smallest time resolution is ' + str(REZ) + ' seconds')


def process_file(filename, array):
    """
    Loads the array from a file. Files contain lines in the format:
        [instruction] [value]
    Valid instructions are:
        i : Insert [value]
        c : Contains [value]?
        d : Delete [value]
    [value] must be a valid positive integer.
    """
    file = open(filename)
    for i, line in enumerate(file):
        print(f'{i:>4}: ', end='')
        instruction, value = line.split(' ')
        value = int(value)
        if instruction == 'i':
            array.insert(value)
            print(f'{"insert":>10}{value:>5d}{
                  array.comparisons:>8d} comparisons')
        elif instruction == 'c':
            print(f'{"contains":>10}{value:>5d}', end='')
            if array.contains(value):
                print(f'{array.comparisons:>8d} comparisons (found)')
            else:
                print(f'{array.comparisons:>8d} comparisons (not found)')
        elif instruction == 'd':
            array.remove(value)
            print(f'{"removed":>10}{value:>5d}{
                  array.comparisons:>8d} comparisons')
        else:
            print('Whoops. Unknown command........')
    file.close()


def time_sorted_trial(filename):
    """ Times how long it takes to processes the
    given file with a SortedArray
    """
    test_array = SortedArray()
    print('\nRunning trial on sorted array with', filename)
    start_time = time.perf_counter()
    process_file(filename, test_array)
    end_time = time.perf_counter()
    time_taken = end_time - start_time
    print(f"Took {time_taken:.3f} seconds.")
    return time_taken


def time_linear_trial(filename):
    """ Times how long it takes to processes the
    given file with a LinearArray
    """
    # ---start student section---
    start_time = time.perf_counter() 
    liner_array = LinearArray()
    process_file(filename, liner_array)  
    end_time = time.perf_counter() 
    time_taken = end_time - start_time
    print(f"Took {time_taken:.3f} seconds.")
    return time_taken
    # ===end student section===


def time_bva_trial(filename, array_size):
    """ Times how long it takes to processes the
    given file with a BitVectorArray
    """
    start_time = time.perf_counter()
    bit_array = BitVectorArray(array_size)
    process_file(filename, bit_array)
    end_time = time.perf_counter()
    time_taken = end_time - start_time
    print(f"Took {time_taken:.3f} seconds.")
    return time_taken


def main_tests(filen):
    '''Do some file processing here...'''

    # for example, process file0 with a LinearArray
    filename = filen
    print('Processing', filename, 'with a linear array')
    test_array = LinearArray()  # initialise a LinearArray
    # process_file(filename, test_array)

    # Add more tests here:)

    # call timing tests here when ready
    time_taken = time_linear_trial(filename)
    return time_taken


def sorted_tests(filen):
    '''Do some file processing here...'''

    # for example, process file0 with a LinearArray
    filename = filen
    print('Processing', filename, 'with a sorted array')
    test_array = SortedArray()  # initialise a LinearArray
    # process_file(filename, test_array)

    # Add more tests here:)

    # call timing tests here when ready
    time_taken = time_sorted_trial(filename)
    return time_taken



def bitvector_tests(filen, maxint):
    '''Do some file processing here...'''

    # for example, process file0 with a LinearArray
    filename = filen
    print('Processing', filename, 'with a bit vector array')


    #test_array = BitVectorArray(filen, maxint)  # initialise a bit vector array
    # call timing tests here when ready
    time_taken = time_bva_trial(filename, maxint)
    return time_taken




if __name__ == '__main__':
    liner_time = main_tests('file3.txt')
    sorted_time = sorted_tests('file3.txt')
    bva_time = bitvector_tests('file3.txt', 10000)

    print(f"Linear array time: {liner_time} seconds.")
    print(f"Sorted array time: {sorted_time} seconds.")
    print(f"Bit vector array time: {bva_time} seconds.")
