class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def display(self):
        return f"{self.real}+{self.imag}i"
def add_complex(c1,c2):
    real_part=c1.real+c2.real
    imag_part=c1.imag+c2.imag
    return Complex(real_part,imag_part)
n=int(input("Enter the number of complex numbers(n>=2):"))
print("Enter the complex numbers:")
real=float(input("Real part #1:"))
imag=float(input("Imaginary part #1:"))
result=Complex(real,imag)
for i in range(2,n+1):
    real=float(input(f"Real part #{i}:"))
    imag=float(input(f"Imaginary part #{i}:"))
    temp=Complex(real,imag)
    result=add_complex(result,temp)
print("the sum of complex numbers is:",result.display())
