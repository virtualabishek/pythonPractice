class Complex:
    # using __init__() to create attributes
    def __init__(self, real, imag):
        self.real = real
        self.imaginary = imag
 
    # method to add complex numbers
    def add(self, number):
        result_real = self.real + number.real
        result_imaginary = self.imaginary + number.imaginary
        
        # create another object of Complex
        result = Complex(result_real, result_imaginary)  
        return result
 
n1 = Complex(5, 6)
n2 = Complex(-4, 2)
 
# The return value from the add() method
# is assigned to the n3 variable
n3 = n1.add(n2)
 
# printing n3 attributes
print('real part =', n3.real)
print('imaginary part =', n3.imaginary)

