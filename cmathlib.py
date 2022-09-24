class cmathcalc():
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

def Help():
    print('''Possible Commands and their arguments:
    cmathcalc.Normal(expression, True/False)
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
    cmathcalc.Fifrt(item, True/False)''')
    print('''
    Note that all root commands above and inclusive of ten consist of Five Letters
    ''')

def main():
    print("> Hello from the Cyber Community o7")

if not __name__ == '__main__':
    main()