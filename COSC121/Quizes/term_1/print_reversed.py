'''
Write a function print_reversed(filename) that reads a file then prints out 
the lines from the file in reversed order, i.e. the last line is written first, 
then the second to last, and so on.
'''

def print_reversed(filename, outfilename):
      '''Docstring'''
      infile = open(filename, 'r')
      outfile = open(outfilename, 'w')
      content = infile.readlines()
      for word in content[::-1]:
         # print(word.rstrip())
         outfile.write(word.rstrip())


print_reversed('data.txt', 'results.txt')