import numpy as np
from matplotlib import pyplot as plt

def F(x):
    
    return ( (x/(1-x)) * ((6/(2+x)) ** 0.5) ) - 0.05

 
def secant(f, x1, x2, es, max_it):
    
    ea = 1.1 * es
    i = 0
    
    while ea > es and i < max_it:
        x = x2 - (f(x2)*(x1-x2))/(f(x1)-f(x2))
        i = i + 1
        
        ea = abs((x - x2)/x) * 100
        x1, x2 = x2, x
        
    print('x:', x)
    print('f(x):', f(x))
    print('Error:', ea, '%')
    print('No. of Iterations:', i)


def falsePosition(f, xl, xu, es, max_it):
    
    if ( f(xl) * f(xu) ) > 0:
        print("The Bounds Don't Bracket a Root")
        return
    
    ea = 1.1 * es
    i = 0
    
    while ea > es and i < max_it:
        xr = xu - (f(xu)*(xl - xu)) / (f(xl) - f(xu))
        i = i + 1
           
        test = f(xl) * f(xr)
        
        if test == 0:
            break
        elif test < 0:
            xu = xr
        else:
            xl = xr        
        
        if i == 1 or xr == 0:
            xrp = xr
            continue
        else:
            ea = abs( (xr - xrp) * 100 / xr )
            xrp = xr

    print('x:', xr)
    print('f(x):', f(xr))
    print('Error:', ea, '%')
    print('No. of Iterations:', i)


#2(a)

x = np.arange(0.02, 0.04, 0.005)
y = F(x)

plt.figure(figsize=(10,8))
plt.plot(x, y)
plt.grid()
plt.xlabel('x values')
plt.ylabel('F values')

print('The Value of x from the graph is approximately 0.028')
print()


#2(b)

print('Using Secant Method:')
secant(F, 0, 0.1, 0.5, 10)
print()

print('Using False-Position Method:')
falsePosition(F, 0, 0.1, 0.5, 10)