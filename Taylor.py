import math as m

'''
Define the function to get all term coefficients of taylor series 
'''
def t(x,y):
    y_ = (m.e)**(3*x-2*y)
    yy_ = ((m.e)**(3*x-2*y))*(3-2*y_)
    yyy_ = ((m.e)**(3*x-2*y))*(-2*yy_ + (3-2*y_)**2)
    yyyy_ = ((m.e)**(3*x-2*y))*(-2*yyy_ - 6*(3-2*y_)*yy_ + (3-2*y_)**2)
    return y_,yy_,yyy_,yyyy_

x0 = eval(input())
y0 = eval(input())
# h is step size
h = 0.1
# n is number of mesh points
n = 2

for i in range(1,n+1):
    s = y0
    k = t(x0,y0)
    c = 1
    a = [y0]
    for j in range(len(k)):
        c = h*c/(j+1)
        print((j+1)*"y"+"_ =", round(k[j],5))
        s+=k[j]*c
        a.append(c*k[j])
    print()
    st = f"y{i} = "
    for v in a:
        st+=str(v)+" + "
    st = st[:-2]
    print(st)
    print("y"+str(i),"=",round(s,5))
    print("-----------------------")
    x0 = x0+h
    y0 = s