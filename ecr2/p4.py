from decimal import Decimal as D,getcontext
getcontext().prec=200

i=lambda:map(D,raw_input().split())
s=lambda x:x.sqrt()
a=lambda x:D(acos(x))
sqrt=s

def pi(context=None):
    if context is None:
        context = getcontext()
    context.prec += 2
    lasts = 0; t = D(3); s = 3; n = 1; na = 0; d = 0; da = 24
    while s != lasts:
        lasts = s
        n, na = n + na, na + 8
        d, da = d + da, da + 32
        t = (t * n) / d
        s += t
    context.prec -= 2
    return +s

def atan(x, context=None):
    """Return the arctangent of x in radians."""
    if context is None:
        context = getcontext()
    
    c = None
    
    if x == 0:
        return D(0, context=context)
    elif abs(x) > 1:
        PI = pi(context=context)
        x_is_inf = x._isinfinity()
        if x_is_inf:
            return PI / D((x._sign, (2,), 0), context=context)
        else:
            c = PI / D((x._sign, (2,), 0), context=context)
            x = 1 / x
    
    context.prec += 2
    x_squared = x ** 2
    y = x_squared / (1 + x_squared)
    y_over_x = y / x
    i = D(0); lasts = 0; s = y_over_x; coeff = 1; num = y_over_x
    while s != lasts:
        lasts = s 
        i += 2
        coeff *= i / (i + 1)
        num *= y
        s += coeff * num
    if c:
        s = c - s
    context.prec -= 2
    return +s

def atan2(y, x, context=None):
    abs_y = abs(y)
    abs_x = abs(x)
    y_is_real = not x._isinfinity()
    if x != 0:
        if y_is_real:
            a = y and atan(y / x, context=context) or D(0)
            if x < 0:
                a += D((y._sign, (1,), 0)) * pi(context=context)
            return a
        elif abs_y == abs_x:
            x = D((x._sign, (1,), 0))
            y = D((y._sign, (1,), 0))
            return pi(context=context) * (2 - x) / (4 * y)
    if y != 0:
        return atan(D((y._sign, (0,), 'F')))
    elif x < 0:
        return D((y._sign, (1,), 0)) * pi()
    else:
        return D(0)

def acos(x, context=None):
    """Return the arccosine of x in radians."""
    if abs(x) > 1:
        raise ValueError("Domain error: acos accepts -1 <= x <= 1")
    if context is None:
        context = getcontext()
    if x == 1:
        return D(0, context=context)
    else:
        PI = pi(context=context)
        if x == -1:
            return PI
        elif x == 0:
            return PI / 2
    return PI / 2 - atan2(x, sqrt(1 - x ** 2), context=context)

x1,y1,r=i()
x2,y2,R=i()
if r>R:(r,R)=(R,r)
d=s((x1-y1)**2+(x2-y2)**2)
if d>=r+R:print 0
elif d<=R-r:print pi*r*r
else: print r*r*a((d*d+r*r-R*R)/2/d/r)+R*R*a((d*d+R*R-r*r)/2/d/R)-s((-d+r+R)*(d+r-R)*(d-r+R)*(d+r+R))/2
