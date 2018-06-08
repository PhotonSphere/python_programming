def general_poly(L):
    k = 1
    
    for i in L:
        return lambda x: i * x ** (len(L)-k) + general_poly(L[(len(L)+1-len(L)):])
        



'''
Write a function called general_poly, that meets the specifications below.
For example, general_poly([1, 2, 3, 4])(10) should evaluate to 1234 because .
1 * 10 ^3 + 2*10^2 + 3*10^1 + 4*10^0
def general_poly (L,x):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #YOUR CODE HERE
    if len(L) == 1:
        return L[0]
    else:
        return L[0] * x ** (len(L)-1) + general_poly(L[(len(L)+1-len(L)):],x)
'''
x = 10
for i in general_poly([1, 2, 3,4]):
    print(i(10))

#print(r(10))
