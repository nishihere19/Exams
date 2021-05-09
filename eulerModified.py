'''
Give input in 2 lines

x0 in first line
y0 in second line 

'''
import math
x0 = eval(input())
y0 = eval(input())
# h is step size
h = 0.2
# n is no. of mesh points
n = 2
# p is maximum iteration to find y(x+rh) using modified euler
p = 10

def f(x,y):
    return (y*y)-(y/x)

for i in range(n):
    y = y0 + h*f(x0,y0)
    y = round(y,5)
    print("Normal Euler ->","y_{0}(x0 +",str(i+1)+"h) =",y)
    print()
    print("Modified Euler:")
    print()
    for j in range(1,p):
        t = y0 + (h/2)*(f(x0,y0)+f(x0+h,y))
        t = round(t,5)
        print("f(x0+"+str(i+1)+"h, y_{"+str(j-1)+"}() = ",f(x0+h,y))
        print("y_{"+str(j)+"}(x0 +",str(i+1)+"h) =",t)
        print()
        if t==y:
            break
        y = t
    print("-----------------------------")
    x0 = x0+h
    y0 = y

