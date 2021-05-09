import copy
def mul(a,b):
    c = [[0 for _ in range(len(b[0]))] for __ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            s=0
            for x in range(len(b)):
                s+=a[i][x]*b[x][j]
            c[i][j]=s
    return c

def smul(a,b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            b[i][j]*=a
    return b

def m(a):
    s = abs(a[0][0])
    for i in a:
        for j in i:
            s = max(s,abs(j))
    return s

def aprx(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] = eval("%.6f"%round(a[i][j],6))
    return a


def pru(a):
    for i in a:
        for j in i:
            if j<0:
                print("%.6f"%round(j,6), end = " ")
            else:
                print("%.6f"%round(j,6), end = " ")
        print()
    print(end)
def pr(a,b):
    for i in range(len(a)):
        for j in a[i]:
            if j<0:
                print("%.4f"%round(j,4), end = " ")
            else:
                print("%.5f"%round(j,5), end = " ")
        print("|",end = "  ")
        for k in b[i]:
            if k<0:
                print("%.4f"%round(k,4), end = " ")
            else:
                print("%.5f"%round(k,5), end = " ")
        print()
    print(end)

end = "---------------------------------------------"

r = int(input())
c = int(input())
a = []
for _ in range(r):
    b = [eval(i) for i in input().split()]
    a.append(b)

b = [[1] for _ in range(len(a))]

pru(a)
print()
print("Power Method")
print()

for _ in range(50):
    print("Iteration -",_+1)
    c = mul(a,b)
    c = aprx(c)
    print("|Lambda| =",m(c))
    pru(c)
    c = smul(1/m(c),c)
    c = aprx(c)
    pru(c)
    print()
    if b==c:
        break
    b = c
