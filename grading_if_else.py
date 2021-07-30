a,b,c = [int(x) for x in input('Enter 3 subject marks :').split( )]

if a < 35 or b <35 or c < 35:
    print("You have failed")
elif a > 35 and b >35 and c >35:
    average = (a+b+c)/3
    if average < 59:
        print("Grade is C")
    elif average < 69 and average >59:
        print("Grade is B")
    elif average >69:
        print("Grade is A")
    else:
        pass
pass

