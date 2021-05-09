import copy
def det(a):
    if len(a)>1:
        s = 0
        for i in range(len(a[0])):
            k = a[0][i]
            b = [[] for __ in range(len(a)-1)]
            for x in range(1,len(a)):
                for y in range(len(a[0])):
                    if y!=i:
                        b[x-1].append(a[x][y])                    
            s+=((-1)**i)*k*det(b)
        return s
    return a[0][0]

def inv(a):
    d = det(a)
    if d==0:
        return -1
    if len(a)==1:
        b = list(a)
        for i in range(len(a)):
            for j in range(len(a[0])):
                b[i][j]**=-1
        return b
    s = [[0 for _ in range(len(a[0]))] for __ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            b = [[] for __ in range(len(a)-1)]
            f = 0
            for x in range(len(a)):
                for y in range(len(a[0])):
                    if x==i:
                        f=-1
                    if (y!=j)and(x!=i):
                        b[x+f].append(a[x][y])
    
            s[j][i] = ((-1)**(i+j))*det(b)/d
    return s

def mul(a,b):
    c = [[0 for _ in range(len(b[0]))] for __ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            s=0
            for x in range(len(b)):
                s+=a[i][x]*b[x][j]
            c[i][j]=s
    return c

def ad(a,b):
    c = copy.deepcopy(a)
    for i in range(len(a)):
        for j in range(len(a[0])):
            c[i][j] = a[i][j] + b[i][j]
    return c

def smul(a,b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            b[i][j]*=a
    return b

def aprx(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] = eval("%.5f"%round(a[i][j],5))
    return a


def pru(a):
    for i in a:
        for j in i:
            if j<0:
                print("%.4f"%round(j,4), end = " ")
            else:
                print("%.5f"%round(j,5), end = " ")
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
r = int(input())
c = int(input())
a = []
for _ in range(r):
    b = [eval(i) for i in input().split()]
    a.append(b)
d = [[0 for _ in range(c)] for __ in range(r)]
lu = [[0 for _ in range(c)] for __ in range(r)]
l = [[0 for _ in range(c)] for __ in range(r)]
u = [[0 for _ in range(c)] for __ in range(r)]
dl = [[0 for _ in range(c)] for __ in range(r)]
du = [[0 for _ in range(c)] for __ in range(r)]
for i in range(r):
    for j in range(c):
        if i==j:
            d[i][j] = a[i][j]
            dl[i][j] = a[i][j]
            du[i][j] = a[i][j]
        else:
            lu[i][j] = a[i][j]
            if i<j:
                u[i][i] = a[i][j]
                du[i][j] = a[i][j]
            else:
                l[i][j] = a[i][j]
                dl[i][j] = a[i][j]

r = int(input())
c = int(input())
b = []
for _ in range(r):
    c = [eval(i) for i in input().split()]
    b.append(c)
end = "----------------------------------------"

print("Original Solution")
print()
pru(mul(inv(a),b))
print(end)
print()

print("Gauss Elimination")
print()
a1 = copy.deepcopy(a)
b1 = copy.deepcopy(b)

for i in range(r):
    for j in range(i+1,len(a1)):
        pr(a1,b1)
        ru = a1[j][i]/a1[i][i]
        for k in range(i,len(a1[0])):
            a1[j][k]-=(a1[i][k]*ru)
        for jj in range(len(b1[0])):
            b1[j][jj]-=b1[i][jj]*ru
pr(a1,b1)
print(end)
print()

print("Gauss Jordan")
print()
a1 = copy.deepcopy(a)
b1 = copy.deepcopy(b)

for i in range(r):
    for j in range(len(a1)):
        if j!=i:
            pr(a1,b1)
            ru = a1[j][i]/a1[i][i]
            for k in range(i,len(a1[0])):
                a1[j][k]-=(a1[i][k]*ru)
            for jj in range(len(b1[0])):
                b1[j][jj]-=(b1[i][jj]*ru)
pr(a1,b1)
print(end)
print()

print("Doo'Little")
print()
L = copy.deepcopy(dl)
U = copy.deepcopy(du)
for _ in range(len(L)):
    L[_][_] = 1
U[1-1][1-1] = a[1-1][1-1]
U[1-1][2-1] = a[1-1][2-1]
U[1-1][3-1] = a[1-1][3-1]
L[2-1][1-1] = a[2-1][1-1]/a[1-1][1-1]
L[3-1][1-1] = a[3-1][1-1]/a[1-1][1-1]
U[2-1][2-1] = a[2-1][2-1] - L[2-1][1-1]*a[1-1][2-1]
U[2-1][3-1] = a[2-1][3-1] - L[2-1][1-1]*a[1-1][3-1]
L[3-1][2-1] = (a[3-1][2-1] - L[3-1][1-1]*a[1-1][2-1])/U[2-1][2-1]
U[3-1][3-1] = a[3-1][3-1] - L[3-1][1-1]*U[1-1][3-1] - L[3-1][2-1]*U[2-1][3-1]
print("L,U")
pr(L,U)
print(end)
print()

print("Crout's")
print()
L = copy.deepcopy(dl)
U = copy.deepcopy(du)
for _ in range(len(L)):
    U[_][_] = 1
L[0][0] = a[0][0]
L[1][0] = a[1][0]
L[2][0] = a[2][0]
U[0][1] = a[0][1]/a[0][0]
U[0][2] = a[0][2]/a[0][0]
L[1][1] = a[1][1] - U[0][1]*a[1][0]
L[2][1] = a[2][1] - U[0][1]*a[2][0]
U[1][2] = (a[1][2] - U[0][2]*a[1][0])/L[1][1]
L[2][2] = a[2][2] - U[0][2]*L[2][0] - U[1][2]*L[2][1]
print("L,U")
pr(L,U)
print(end)
print()

print("Gauss Jacobi")
print()
h = mul(inv(d),lu)
h = smul(-1,h)
print("H")
pru(h)
c = mul(inv(d),b)
print("c")
pru(c)
x = copy.deepcopy(b)
x = smul(0,x)
print("Iteration -",0)
pru(x)
it = 1
for _ in range(10):
    soo = ad(mul(h,x),c)
    soo = aprx(soo)
    print("Iteration -",it)
    pru(soo)
    if soo==x:
        break
    x = copy.deepcopy(soo)
    it+=1
print(end)
print()

print("Gauss Seidal")
print()
h = mul(inv(dl),u)
h = smul(-1,h)
print("H")
pru(h)
c = mul(inv(dl),b)
print("c")
pru(c)
print("(D+L)^-1")
pru(inv(dl))
x = copy.deepcopy(b)
x = smul(0,x)
print("-------------")
print("Iteration -",0)
print("-------------")
pru(x)
it = 1
for _ in range(10):
    soo = ad(x,mul(inv(dl),ad(b,smul(-1,mul(a,x)))))
    soo = aprx(soo)
    print("-------------")
    print("Iteration -",it)
    print("-------------")
    print("B-AX =")
    pru(aprx(ad(b,smul(-1,mul(a,x)))))
    print(f"X_{it} =")
    pru(soo)
    if soo==x:
        break
    x = copy.deepcopy(soo)
    it+=1
print(end)
print()
