import sys,math

def hash_fraction(m,n):
    p=sys.hash_info.modulus
    while m%p==n%p==0:
        m,n=m//p,n//p
    if n%p==0:
        hash_value=sys.hash_info.inf
    else:
        hash_value=(abs(m)%p)*pow(n,p-2,p)%p
    if m<0:
        hash_value=-hash_value
    if hash_value==-1:
        hash_value=-2
    return hash_value

def hash_float(x):
    if math.isnan(x):
        return sys.hash_info.nan
    elif math.isinf(x):
        return sys.hash_info.inf if x>0 else -sys.hash_info.inf
    else:
        return hash_fraction(*x.as_integer_ratio())