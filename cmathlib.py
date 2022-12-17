# Sneaky Imports
import math
import random
import sys
from functools import wraps
print("Hello from the Cyber Community o7")
def _0xround(item):
    round(item,0)
class cmathcalc():
    def Normal(expression, noDecimal = False, units=""):
        a = float(expression)
        if noDecimal == True:
            return str(_0xround(a))+" "+units
        else:
            return str(a)+" "+units
    def Power(expression, power, noDecimal = False):

        a = float(expression)
        b = a**power
        if noDecimal == True:
            return _0xround(b)
        else:
            return b
    
    def memoize(func):
        cache = {}

        @wraps(func)
        def wrapper(*args,**kwargs):
            key = str(args)+str(kwargs)
            if key not in cache:
                cache[key] = func(*args,**kwargs)
            return cache[key]
        return wrapper
    sys.setrecursionlimit(900000)
    @memoize
    def Fibonacci(n):
        if n < 2: 
            return n
        return cmathcalc.Fibonacci(n - 1) + cmathcalc.Fibonacci(n - 2)
        

    # Constants
    constants = {
        "pi" : 3.14159265358979323846264338327950,
        "pythagorus": 1.4142135623730950488016887242096980785696718753769480731766797379907324784621,
        "theodorus" : 1.7320508075688772935274463415058723669428052538103806280558069794,
        "euler": 0.5772156649015328606065120900824024310421593359399235988057672348,
        "mole": 6.02214179*(10**23)
    }
    def Sine(x):
        return math.sin(math.radians(x))
    def Cosine(x):
        return math.cos(math.radians(x))
    def Tang(x):
        return math.tan(math.radians(x))
    def InvSine(x):
        return math.degrees(math.asin(x))
    def InvCosine(x):
        return math.degrees(math.acos(x))
    def InvTang(x):
        return math.degrees(math.atan(x))
    # -----------------------
    class roots():
        def Sqrt(item, noDecimal = False):
            a =  float(item)
            if noDecimal == True:
                return _0xround(a**(1/2))
            else:
                return a**(1/2)

        def Cbrt(item, noDecimal = False):
            a =  float(item)
            if noDecimal == True:
                return _0xround(a**(1/3))
            else:
                return a**(1/3)
        def Fort(item, noDecimal = False):
            a =  float(item)
            if noDecimal == True:
                return _0xround(a**(1/4))
            else:
                return a**(1/4)
        def Ffrt(item, noDecimal = False):
            a =  float(item)
            if noDecimal == True:
                return _0xround(a**(1/5))
            else:
                return a**(1/5)
        def Sxrt(item, noDecimal = False):
            a =  float(item)
            if noDecimal == True:
                return _0xround(a**(1/6))
            else:
                return a**(1/6)
        def Svrt(item, noDecimal = False):
            a =  float(item)
            if noDecimal == True:
                return _0xround(a**(1/7))
            else:
                return a**(1/7)
        def Egrt(item, noDecimal = False):
            a =  float(item)
            if noDecimal == True:
                return _0xround(a**(1/8))
            else:
                return a**(1/8)
        def Nirt(item, noDecimal = False):
            a =  float(item)
            if noDecimal == True:
                return _0xround(a**(1/9))
            else:
                return a**(1/9)
        def Tenrt(item, noDecimal = False):
            a =  float(item)
            if noDecimal == True:
                return _0xround(a**(1/10))
            else:
                return a**(1/10)
        def Elert(item, noDecimal = False):
            a =  float(item)
            if noDecimal == True:
                return _0xround(a**(1/11))
            else:
                return a**(1/11)
        def Twert(item, noDecimal = False):
            a =  float(item)
            if noDecimal == True:
                return _0xround(a**(1/12))
            else:
                return a**(1/12)
        def Thtrt(item, noDecimal = False):
            a =  float(item)
            if noDecimal == True:
                return _0xround(a**(1/13))
            else:
                return a**(1/13)
        def Fotrt(item, noDecimal = False):
            a =  float(item)
            if noDecimal == True:
                return _0xround(a**(1/14))
            else:
                return a**(1/14)
        def Fifrt(item, noDecimal = False):
            a =  float(item)
            if noDecimal == True:
                return _0xround(a**(1/15))
            else:
                return a**(1/15)
        def Sxtrt(item, noDecimal = False):
            a =  float(item)
            if noDecimal == True:
                return _0xround(a**(1/16))
            else:
                return a**(1/16)
    print("Calculator Initiated")
def Help():
    print('Github Wiki Page :https://github.com/CaidynPaul/cmathlib/wiki')

class cmathutil():
    def Bubble(arr):
        n =  len(arr)
        swapped = True
        while n > 0 and swapped == True:
            swapped = False
            n -= 1

            for i in range(n):
                if arr[i] > arr[i+1]:
                    arr[i],arr[i+1]=arr[i+1],arr[i]
                    swapped = True
        return arr
    def ConvBase(x,base=None):
        if base == 2:
            return bin(x)
        elif base == 10:
            return float(x)
        elif base == 16:
            return hex(x)
        elif base==None:
            return bin(x)

def irange(min,max,step=1):
    return range(min,max+1,step)
def xrange(min,max,step=1):
    return range(min+1,max,step)

if __name__ == '__main__':
    Help()

randommsgs = ["https://discord.gg/5sAd4mQvRZ","Support Duck Supremacy","Remember to hydrate", "If it tastes disgusting don't eat it!", "One Calculation at a time", "Support Duck Supremacy","This is a random Message","Hello World","'Hello World' - A Devs First Words"]
print(random.choice(randommsgs))
