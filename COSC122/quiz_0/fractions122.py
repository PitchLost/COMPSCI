def find_gcd(num1, num2):
    """ 
    Returns the Greatest Common Divisor (GCD) of num1 and num2. 
    Assumes num1 and num2 are positive integers. 
    """
    smaller = min(num1, num2)
    for i in range(smaller, 1, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i
    return 1


class Fraction():
    '''Defines a Fraction type that has an integer numerator and a non-zero integer denominator'''

    def __init__(self, num=0, denom=1):
        ''' Creates a new Fraction with numerator num and denominator denom'''
        if isinstance(num, int) and isinstance(denom, int):
            self.numerator = num
            if denom != 0:
                self.denominator = denom
            else:
                raise ZeroDivisionError
        else:
            raise ValueError('Numerator and denominator must be ints')
    def __str__(self):
        '''String method'''
        return f"{self.numerator}/{self.denominator}"
    
    def __repr__(self):
        '''Representation method'''
        return f"Fraction{self.numerator, self.denominator}"
    
    def __add__(self, other):
        num = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        denom = self.denominator * other.denominator
        return Fraction(num, denom)
    
    def __mul__(self, other):
        num = self.numerator * other.numerator
        denom = self.denominator * other.denominator
        return Fraction(num, denom)
    
    def __eq__(self, other):
        a, b, c, d = self.numerator, self.denominator, other.numerator, other.denominator
        return a*d == b*c


class ReducedFraction(Fraction):                  # is a sub-class of the Fraction class
    def __init__(self, numerator, denominator=1):
        super().__init__(numerator, denominator)  # use Fraction.__init__ 
        self._reduce()
    def __repr__(self):
        return f"ReducedFraction{self.numerator, self.denominator}"
    
    def __add__(self, other):
        fraction_result = super().__add__(other)   # uses the __add__ method from Fraction
        reduced_result = super() 
        return reduced_result

    def _reduce(self):
        gcd = find_gcd(self.numerator, self.denominator)
        self.numerator, self.denominator = self.numerator//gcd, self.denominator//gcd

