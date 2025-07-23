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

class ReducedFraction(Fraction):
    '''Hey sigmas'''
    def __init__(self, numerator, denominator=1):
        '''Erm what the flip'''
        super().__init__(numerator, denominator)  # use Fraction.__init__ 
        self._reduce()
    def __repr__(self):
        '''Represent!!!'''
        return f"ReducedFraction({self.numerator}, {self.denominator})"

    
    def __add__(self, other):
        '''Addition'''
        fraction_result = super().__add__(other)  # Returns a Fraction
        return ReducedFraction(fraction_result.numerator, fraction_result.denominator)


    def _reduce(self):
        '''Reduce'''
        gcd = find_gcd(self.numerator, self.denominator)
        self.numerator, self.denominator = self.numerator//gcd, self.denominator//gcd

    def __mul__(self, other):
        '''Multiplication!!'''
        fraction_result = super().__mul__(other)
        return ReducedFraction(fraction_result.numerator, fraction_result.denominator)


class MixedNumber():
    '''My class G'''
    def __init__(self, whole_num, fraction_num):
        '''Fuck meee'''
        fraction_num = ReducedFraction(fraction_num.numerator, fraction_num.denominator)
        if fraction_num.numerator >= fraction_num.denominator:
            sigma_value = fraction_num.numerator // fraction_num.denominator
            whole_num = whole_num + sigma_value
            new_numerator = fraction_num.numerator % fraction_num.denominator
            self.fraction = ReducedFraction(new_numerator, fraction_num.denominator)
        else:
            self.fraction = fraction_num
        self.whole_num = whole_num
    
    def __repr__(self):
        whole = self.whole_num
        fraction_n = self.fraction.numerator
        fraction_d = self.fraction.denominator
        reduced_frac = ReducedFraction(fraction_n, fraction_d)
        return f"MixedNumber({whole}, ReducedFraction({fraction_n}, {fraction_d}))"

    def __str__(self):
        return f"{self.whole_num} and {self.fraction}"

    def __add__(self, other):
        whole_sum = self.whole_num + other.whole_num
        fraction_sum = self.fraction + other.fraction
        if fraction_sum.numerator >= fraction_sum.denominator:
            extra_whole = fraction_sum.numerator // fraction_sum.denominator
            whole_sum += extra_whole
            new_numerator = fraction_sum.numerator % fraction_sum.denominator
            fraction_sum = ReducedFraction(new_numerator, fraction_sum.denominator)
        self.whole_num = whole_sum
        self.fraction = fraction_sum

        return MixedNumber(whole_sum, fraction_sum)



	
x = MixedNumber(3, Fraction(1, 3))
y = MixedNumber(-1, Fraction(2, 5))
z = x + y
print(z)
print(repr(z))