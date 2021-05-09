import math

'''
3 lines of input
x0 in first line
y0 in second line
y'0 in third line
'''

x0 = eval(input())
y0 = eval(input())
y0_ = eval(input())

# h is step size
h = 0.2
# n is number of mesh points
n = 2


'''
Please redefine 
the function 
as asked in given qn
'''
def f(x,y,y_):
    return (1+ x*x)*y


for i in range(1,n+1):
    k1 = h*f(x0,y0,y0_)
    k2 = h*f(x0+(h/2),y0 + h*y0_/2 + h*(k1/8),y0_ + k1/2)
    k3 = h*f(x0+(h/2),y0 + h*y0_/2 + h*(k1/8),y0_ + k2/2)
    k4 = h*f(x0+h,y0 + h*y0_ + h*k3/2,y0_ + k3)
    k1 = round(k1,5)
    k2 = round(k2,5)
    k3 = round(k3,5)
    k4 = round(k4,5)
    print("k1 = h*f(",str(x0)+", "+str(y0)+", "+str(y0_)+" ) =",k1)
    print("k2 = h*f(",str(x0+(h/2))+", "+str(y0 + h*y0_/2 + h*(k1/8))+", "+str(y0_ + k1/2)+" ) =",k2)
    print("k3 = h*f(",str(x0+(h/2))+", "+str(y0 + h*y0_/2 + h*(k1/8))+", "+str(y0_ + k2/2)+" ) =",k3)
    print("k4 = h*f(",str(x0+h)+", "+str(y0 + h*y0_ + h*k3/2)+", "+str(y0_ + k3)+" ) =",k4)    
    print()
    y1 = y0 + h*(y0_ + (k1 + k2 + k3)/6)
    y1_ = y0_ + (k1 + 2*k2 + 2*k3 + k4)/6
    print("y"+str(i)+" =",y1)
    print("y_"+str(i)+" =",y1_)
    print("-----------------------------")
    x0 = x0+h
    y0 = y1
    y0_ = y1_
