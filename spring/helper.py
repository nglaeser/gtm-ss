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

# Lagrange interpolation
def interpolate_at(points, x_value):
    # Lagrange basis polynomials evaluated at 0
    ell = [1]*len(points)
    for i in range(len(points)):
        for j in range(len(points)):
            if i!=j:
                ell[i] *= float(x_value-points[j][0])/(points[i][0]-points[j][0])

    # f(X) = sum_1^{t+1} ell_i(X) * y_i
    # y = f(x_value)
    y = 0
    for i in range(len(points)):
        y += ell[i]*points[i][1]
    return y

######## convert between message and arr of numbers ########
alphabet = "abcdefghijklmnopqrstuvwxyz"
def convert_msg(string):
    arr = []
    for c in string.lower():
        try:
            i = alphabet.index(c)+1
            arr.append(i)
        except:
            continue
    return arr

def nums_to_msg(arr):
    msg = ""
    for num in arr:
        try:
            msg += alphabet[num-1]
        except Exception as e:
            print("nums_to_msg: ERROR {} ({} is <1 or >26). Make sure you provided at least t+1 shares to the reconstruction function".format(e, num))
#             msg += "¿"
#             continue
            return
    return msg