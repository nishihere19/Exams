import math

'''
3 lines of input
x0 in first line
y0 in second line
z0 in third line
'''

x0 = eval(input())
y0 = eval(input())
z0 = eval(input())

# h is step size
h = 0.1
# n is number of mesh points
n = 2

'''
Please redefine 
the functions 
as asked in given qn
'''
def f1(x,y,z):
    return x+z

def f2(x,y,z):
    return x - y*y

for i in range(1,n+1):
    k1 = h*f1(x0,y0,z0)
    l1 = h*f2(x0,y0,z0)
    k2 = h*f1(x0+(h/2),y0+(k1/2),z0+(l1/2))
    l2 = h*f2(x0+(h/2),y0+(k1/2),z0+(l1/2))
    k3 = h*f1(x0+(h/2),y0+(k2/2),z0+(l2/2))
    l3 = h*f2(x0+(h/2),y0+(k2/2),z0+(l2/2))
    k4 = h*f1(x0+h,y0+k3,z0+l3)
    l4 = h*f2(x0+h,y0+k3,z0+l3)
    k1 = round(k1,5)
    k2 = round(k2,5)
    k3 = round(k3,5)
    k4 = round(k4,5)
    l1 = round(l1,5)
    l2 = round(l2,5)
    l3 = round(l3,5)
    l4 = round(l4,5)
    print(f"k1 = h*f1({x0},{y0},{z0}) =",k1)
    print(f"k2 = h*f1({x0+(h/2)},{y0+(k1/2)},{z0+(l1/2)}) =",k2)
    print(f"k3 = h*f1({x0+(h/2)},{y0+(k2/2)},{z0+(l2/2)}) =",k3)
    print(f"k4 = h*f1({x0+h},{y0+k3},{z0+l3}) =",k4)
    print()
    print(f"l1 = h*f2({x0},{y0},{z0}) =",l1)
    print(f"l2 = h*f2({x0+(h/2)},{y0+(k1/2)},{z0+(l1/2)}) =",l2)
    print(f"l3 = h*f2({x0+(h/2)},{y0+(k2/2)},{z0+(l2/2)}) =",l3)
    print(f"l4 = h*f2({x0+h},{y0+k3},{z0+l3}) =",l4)
    y1 = y0 + (1/6)*(k1+2*k2+2*k3+k4)
    z1 = z0 + (1/6)*(l1+2*l2+2*l3+l4)
    print()
    print(f"y{i} = y{i-1} + (1/6)*({k1+2*k2+2*k3+k4}) =",y1)
    print(f"z{i} = z{i-1} + (1/6)*({l1+2*l2+2*l3+l4}) =",z1)
    print()
    print("---------------------------------------------------")
    print()
    x0 = x0+h
    y0 = y1
    z0 = z1



