'''Hello!'''
class Rectangle(object):
    """ Rectangle class """
    def __init__(self, width=1, height=2):
        '''Doc'''
        self.width = width
        self.height = height
    
    def __str__(self):
        '''Scuffed'''
        shape = ''
        for line in range(self.height):
            shape = shape + ('#' * self.width + '\n')
        return shape
    
    def area(self):
        '''Doc'''
        return self.width * self.height
    
    def perimeter(self):
        '''Doc'''
        return 2* self.width + 2 * self.height

