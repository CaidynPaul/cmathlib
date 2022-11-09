# Sneaky Imports
import math

print("Hello from the Cyber Community o7")
class cmathcalc():
    def Normal(expression, noDecimal = False, units=""):
        a = float(expression)
        if noDecimal == True:
            return str(int(a))+" "+units
        else:
            return str(a)+" "+units
    def Power(expression, power, noDecimal = False):
        
        a = float(expression)
        b = a**power
        if noDecimal == True:
            return int(b)
        else:
            return b
    # Constants
    constants = {
        "pi" : 3.14159265358979323846264338327950,
        "pythagorus": 1.4142135623730950488016887242096980785696718753769480731766797379907324784621,
        "theodorus" : 1.7320508075688772935274463415058723669428052538103806280558069794,
        "euler": 0.5772156649015328606065120900824024310421593359399235988057672348
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
                return int(a**(1/2))
            else:
                return a**(1/2)

        def Cbrt(item, noDecimal = False):
            a =  float(item)
            if noDecimal == True:
                return int(a**(1/3))
            else:
                return a**(1/3)
        def Fort(item, noDecimal = False):
            a =  float(item)
            if noDecimal == True:
                return int(a**(1/4))
            else:
                return a**(1/4)
        def Ffrt(item, noDecimal = False):
            a =  float(item)
            if noDecimal == True:
                return int(a**(1/5))
            else:
                return a**(1/5)
        def Sxrt(item, noDecimal = False):
            a =  float(item)
            if noDecimal == True:
                return int(a**(1/6))
            else:
                return a**(1/6)
        def Svrt(item, noDecimal = False):
            a =  float(item)
            if noDecimal == True:
                return int(a**(1/7))
            else:
                return a**(1/7)
        def Egrt(item, noDecimal = False):
            a =  float(item)
            if noDecimal == True:
                return int(a**(1/8))
            else:
                return a**(1/8)
        def Nirt(item, noDecimal = False):
            a =  float(item)
            if noDecimal == True:
                return int(a**(1/9))
            else:
                return a**(1/9)
        def Tenrt(item, noDecimal = False):
            a =  float(item)
            if noDecimal == True:
                return int(a**(1/10))
            else:
                return a**(1/10)
        def Elert(item, noDecimal = False):
            a =  float(item)
            if noDecimal == True:
                return int(a**(1/11))
            else:
                return a**(1/11)
        def Twert(item, noDecimal = False):
            a =  float(item)
            if noDecimal == True:
                return int(a**(1/12))
            else:
                return a**(1/12)
        def Thtrt(item, noDecimal = False):
            a =  float(item)
            if noDecimal == True:
                return int(a**(1/13))
            else:
                return a**(1/13)
        def Fotrt(item, noDecimal = False):
            a =  float(item)
            if noDecimal == True:
                return int(a**(1/14))
            else:
                return a**(1/14)
        def Fifrt(item, noDecimal = False):
            a =  float(item)
            if noDecimal == True:
                return int(a**(1/15))
            else:
                return a**(1/15)
    print("Calculator Initiated")
def Help():
    return('''Possible Commands and their arguments:
    cmathcalc.Normal(expression, True/False, units)
    cmathcalc.Sqrt(item,True/False)
    cmathcalc.Fort(item, True/False)
    cmathcalc.Ffrt(item, True/False)
    cmathcalc.Sxrt(item, True/False)
    cmathcalc.Svrt(item, True/False)
    cmathcalc.Egrt(item, True/False)
    cmathcalc.Nirt(item, True/False)
    cmathcalc.Tenrt(item, True/False)
    cmathcalc.Elert(item, True/False)
    cmathcalc.Twert(item, True/False)
    cmathcalc.Thtrt(item, True/False)
    cmathcalc.Fotrt(item, True/False)
    cmathcalc.Fifrt(item, True/False)
    cmathcalc.Sine(x) requires value in degrees not radians
    cmathcalc.Cosine(x) requires value in degrees not radians
    cmathcalc.Tang(x) requires value in degrees not radians
    cmathcalc.InvSine(x) returns value in degrees not radians
    cmathcalc.InvCosine(x) returns value in degrees not radians
    cmathcalc.InvTang(x) returns value in degrees not radians
    Note that all root commands above and inclusive of ten consist of Five Letters
-------------------------------------------------------------------------------------
    cmathutil
    Bubble(arr) 

    where arr is an array
    ''')

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
