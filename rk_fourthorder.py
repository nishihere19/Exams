import math as m

'''
2 lines of input
x0 in first line
y0 in second line
'''

x0 = eval(input())
y0 = eval(input())
# h is step size
h = -0.1
# n is number of mesh points
n = 1

def f(x,y):
    return (m.e)**(3*x-2*y)

for i in range(n):
    k1 = h*f(x0,y0)
    k2 = h*f(x0+(h/2),y0+(k1/2))
    k3 = h*f(x0+(h/2),y0+k2/2)
    k4 = h*f(x0+h,y0+k3)
    k1 = round(k1,5)
    k2 = round(k2,5)
    k3 = round(k3,5)
    k4 = round(k4,5)
    print("k1 = h*f(",str(x0)+", "+str(y0)+") =",k1)
    print("k2 = h*f(",str(x0+(h/2))+", "+str(y0+(k1/2))+") =",k2)
    print("k3 = h*f(",str(x0+(h/2))+", "+str(y0+(k2/2))+") =",k3)
    print("k4 = h*f(",str(x0+h)+", "+str(y0+k3)+") =",k4)
    print()
    y = y0 + (k1 + 2*k2 + 2*k3 + k4)/6
    print("y"+str(i+1)+" =",y)
    print("-----------------------------")
    x0 = x0+h
    y0 = y

