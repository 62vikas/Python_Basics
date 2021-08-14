def decdouble(func):
    def double(x):
        y=func(x)*2
        print(y)
        return(y)
    return(double)

@decdouble
def numb(x):
    print("Number is :",x)
x=numb(5)
