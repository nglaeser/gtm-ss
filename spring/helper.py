from numpy import linspace
from random import randint
from sympy import isprime
from matplotlib.pyplot import plot, scatter

######## polynomial stuff ########
def term_to_string(coeff, deg):
    if coeff == 0:
        return ""

    temp = "{}".format(coeff)
    app = ""
    # constant term
    if deg == 0:
        return temp
    # x term
    elif deg == 1:
        app = "x"
    # others
    else:
        app = "x^{}".format(deg)
    return app if coeff == 1 else temp+app

def print_poly(coeffs):
    poly_str = ""
    
    # coefficients from highest to lowest degree
    deg = len(coeffs)-1
    for i in range(len(coeffs)):
        if(coeffs[i]!=0):
            poly_str += "{} + ".format(term_to_string(coeffs[i], deg-i))
    
    # remove extra + at end
    print(poly_str[:-3])
    
def eval_poly(coeffs, x):
    # coefficients from highest to lowest degree
    deg = len(coeffs)-1
    ans = 0
    for i in range(len(coeffs)):
        ans += coeffs[i]*x**(deg-i)
        
    # in real SSS, this is over a finite field (mod p)
    # return ans%p
    
    # but this is not representable in 2D so we will use int arith
    # (note this is not secure)
    return ans

def interpolate(points, degree):
    # Lagrange interpolation
    coeffs = []
    return coeffs