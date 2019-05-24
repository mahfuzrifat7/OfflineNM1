import numpy as np
from matplotlib import pyplot as plt

def lnFunc(x, n):
    
    value = 0
    term = 0
    sign = 1
    power = 1
    
    while n > 0:     
        term = sign * (x ** power) / power
        value = value + term
        sign = - 1 * sign
        power = power + 1
        n = n - 1
        
    return value


def relApproxError(n):
    
    current = lnFunc(0.5, n)
    previous = lnFunc(0.5, n - 1)
    error = abs( (current - previous) ) * 100 / current
    print('Value of ln(1.5) for', n, 'terms:', current)
    
    return error


#1(a)

x = float(input("Enter the Value of x: "))
n = int(input("Enter the Number of Terms: "))

lnApprox = lnFunc(x, n)

print("Approx. value of ln(1+x) =", lnApprox, "where x =", x, "and n =", n)
print()


#1(b)

x = np.arange(-1, 1, 0.1)
y = np.log(1 + x)

plt.figure(0)
plt.figure(figsize=(10,8))
plt.plot(x, y)
plt.xlabel('x values')
plt.ylabel('ln(1+x)')


#1(c)

terms = np.array([1,3,5,20,50])

for term in terms:
    y = lnFunc(x, term)
    plt.plot(x, y)
    

#1(d)
    
terms = np.arange(1, 51)

errors = np.array([])

for term in terms:
    error = relApproxError(term)
    errors = np.append(errors, error)
    
plt.figure(1)
plt.figure(figsize=(10,8))
plt.plot(terms, errors)
plt.xlabel('No. of Terms')
plt.ylabel('Relative Approximation Error')