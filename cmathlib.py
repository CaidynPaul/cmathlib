class cmathcalc():
    def __init__(self, Normal, Sqrt, Cbrt, fort, ffrt, sxrt, svrt, egrt):
        self.Normal = Normal
        self.Sqrt = Sqrt
        self.Cbrt = Cbrt

    def Normal(expression, noDecimal = False):
        a = float(expression)
        if noDecimal == True:
            return int(a)
        else:
            return a
    
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
    def fort(item, noDecimal = False):
        a =  float(item)
        if noDecimal == True:
            return int(a**(1/4))
        else:
            return a**(1/4)
    def ffrt(item, noDecimal = False):
        a =  float(item)
        if noDecimal == True:
            return int(a**(1/5))
        else:
            return a**(1/5)
    def sxrt(item, noDecimal = False):
        a =  float(item)
        if noDecimal == True:
            return int(a**(1/6))
        else:
            return a**(1/6)
    def svrt(item, noDecimal = False):
        a =  float(item)
        if noDecimal == True:
            return int(a**(1/7))
        else:
            return a**(1/7)
    def egrt(item, noDecimal = False):
        a =  float(item)
        if noDecimal == True:
            return int(a**(1/8))
        else:
            return a**(1/8)

def Help():
    print('''Possible Commands and their arguments:
    cmathcalc.Normal(expression, True/False)
    cmathcalc.Sqrt(item,True/False)
    cmathcalc.Cbrt(item, True/False)''')

def main():
    print("> Hello from the Cyber Community o7")

if not __name__ == '__main__':
    main()