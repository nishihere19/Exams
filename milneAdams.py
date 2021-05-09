import math as m
# h is step size
h = -0.1

'''
First line- Enter 'm' for Milne' method
            Enter 'a' for Adam's method
second line- Input x0
Next four lines- Input y0, y1, y2, y3
'''
method = input()
x0 = eval(input())
y0 = eval(input())
y1 = eval(input())
y2 = eval(input())
y3 = eval(input())

x1 = x0+h
x2 = x1+h
x3 = x2+h
x4 = x3+h

'''
Define the function f(x,y)
From the given question
'''
def f(x,y):
    return round((m.e)**(3*x-2*y),5)

# Milne predictor
def mp():
    return round(y0 + (4*h/3)*(2*f(x1,y1) - f(x2,y2) + 2*f(x3,y3)),5)

# Milne corrector
def mc():
    return round(y2 + (h/3)*(f(x2,y2) + 4*f(x3,y3) + f(x4,y4)),5)

# Adam predictor
def ap():
    return round(y3 + (h/54)*(55*f(x3,y3) - 59*f(x2,y2) + 37*f(x1,y1) - 9*f(x0,y0)),5)

# Adam corrector
def ac():
    return round(y3 + (h/24)*(9*f(x4,y4) + 19*f(x3,y3) - 5*f(x2,y2) + f(x1,y1)),5)

if method=="m":
    y4 = mp()
    print("Milne's Prediction -> y4 = "+f"{y0} + (4({h})/3)*[2({f(x1,y1)}) - {f(x2,y2)} + 2({f(x3,y3)})] =",y4)
    print()
    print("Milne's Correction:")
    for i in range(10):
        t = mc()
        print("y4 = "+f"{y2} + (({h})/3)*[{f(x2,y2)} + 4({f(x3,y3)}) + {f(x4,y4)}] =",t)
        if t == y4:
            break
        y4 = t

if method=="a":
    y4 = ap()
    print("Adam's Prediction -> y4 = "+f"{y3} + ({h}/54)*[55({f(x3,y3)}) - 59({f(x2,y2)}) + 37({f(x1,y1)}) - 9({f(x0,y0)})] =",y4)
    print()
    print("Adam's Correction:")
    for i in range(10):
        t = ac()
        print("y4 = "+f"{y3} + (({h})/24)*[9({f(x4,y4)}) + 19({f(x3,y3)}) - 5({f(x2,y2)}) + {f(x1,y1)}] =",t)
        if t == y4:
            break
        y4 = t

