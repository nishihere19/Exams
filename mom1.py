# Created by Dwaraganathan 

import math
a = eval(input())
b = eval(input())
c = eval(input())
d = eval(input())
phi = math.radians(eval(input()))
omegaAB = eval(input())
alphaAB = eval(input())

def f(a,b,c,d,phi):
    su = a**2 + d**2 - 2*a*d*math.cos(phi)
    su = math.sqrt(su)
    
    if a<d:
        y1 = math.asin((a*math.sin(phi))/su)
        x1 = math.pi-y1-phi
    else:
        x1 = math.asin((d*math.sin(phi))/su)
        y1 = math.pi-x1-phi

    phu = math.acos((b**2 + c**2 - su**2)/(2*b*c))
    if b<c:
        y2 = math.asin((b*math.sin(phu))/su)
        x2 = math.pi-y2-phu
    else:
        x2 = math.asin((c*math.sin(phu))/su)
        y2 = math.pi-x2-phu
    
    bx = a*math.cos(phi) - b*math.cos(x1+x2+phi)
    by = a*math.sin(phi) - b*math.sin(x1+x2+phi)
    theta2 = x1+x2+phi-math.pi
    theta3 = math.pi-y1-y2
    return bx,by,theta2,theta3,a*math.cos(phi),a*math.sin(phi)

def v(a,b,c,d,phi):
    de = 0.0000001
    vbx = (f(a,b,c,d,phi+de)[0]-f(a,b,c,d,phi)[0])/de
    vby = (f(a,b,c,d,phi+de)[1]-f(a,b,c,d,phi)[1])/de
    vb = math.sqrt(vbx**2+vby**2)

    wbc = (f(a,b,c,d,phi+de)[2]-f(a,b,c,d,phi)[2])/de
    wcd = (f(a,b,c,d,phi+de)[3]-f(a,b,c,d,phi)[3])/de
    return vb, wbc, wcd

def ac(a,b,c,d,phi,om,al):
    de = 0.0001
    ax_b = (om*om)*((f(a,b,c,d,phi+de)[0]+f(a,b,c,d,phi-de)[0]-2*f(a,b,c,d,phi)[0])/(de*de)) + al*(f(a,b,c,d,phi+de)[0]-f(a,b,c,d,phi)[0])/de
    ay_b = (om*om)*((f(a,b,c,d,phi+de)[1]+f(a,b,c,d,phi-de)[1]-2*f(a,b,c,d,phi)[1])/(de*de)) + al*(f(a,b,c,d,phi+de)[1]-f(a,b,c,d,phi)[1])/de
    a_b = (ax_b*ax_b + ay_b*ay_b)**0.5

    ac_CB = b*(omegaAB*v(a,b,c,d,phi)[1])**2
    at_CB = (al*(f(a,b,c,d,phi+de)[2]-f(a,b,c,d,phi)[2])/de) + (om*om)*((f(a,b,c,d,phi+de)[2]+f(a,b,c,d,phi-de)[2]-2*f(a,b,c,d,phi)[2])/(de*de))
    at_CB*=b
    asu_b = (ac_CB**2 + at_CB**2)**0.5

    #ax_a = (f(a,b,c,d,phi+de)[4]+f(a,b,c,d,phi-de)[4]-2*f(a,b,c,d,phi)[4])/(de*de)
    #ay_a = (f(a,b,c,d,phi+de)[5]+f(a,b,c,d,phi-de)[5]-2*f(a,b,c,d,phi)[5])/(de*de)
    #a_a = (ax_a**2 + ay_a**2)**0.5

    ang = math.atan(ay_b/ax_b)
    if ang<0:
        ang+=math.pi
    ang-= f(a,b,c,d,phi)[2]
    
    ac_CD = c*(omegaAB*v(a,b,c,d,phi)[2])**2
    at_CD = (al*(f(a,b,c,d,phi+de)[3]-f(a,b,c,d,phi)[3])/de) + (om*om)*((f(a,b,c,d,phi+de)[3]+f(a,b,c,d,phi-de)[3]-2*f(a,b,c,d,phi)[3])/(de*de))
    at_CD*=c
    aku_C = (ac_CD**2 + at_CD**2)**0.5
    #ax_CB = ax_b-ax_a
    #ay_CB = ay_b-ay_a
    #aku = (ax_CB**2 + ay_CB**2)**0.5
    #ac_CB = aku*math.cos(ang)
    #at_CB = aku*math.sin(ang)
    
    return ax_b, ay_b, a_b, ac_CB, at_CB, asu_b, ac_CD, at_CD , aku_C



def ve(a,b,c,d,phi):
    vcwb = abs((a*math.sin(phi-f(a,b,c,d,phi)[2]))/(math.sin(f(a,b,c,d,phi)[3]-f(a,b,c,d,phi)[2])))
    vbcwb = abs((a*math.sin(f(a,b,c,d,phi)[3]-phi))/(math.sin(phi-f(a,b,c,d,phi)[2])))   

    wbcwb = vbcwb/b
    wcdwb = vcwb/c 

    return vcwb, vbcwb, wbcwb, wcdwb 

print("C=",f(a,b,c,d,phi)[:2])
print("V_CB = ",v(a,b,c,d,phi)[0]*omegaAB)
print("Theta2 = ",math.degrees(f(a,b,c,d,phi)[2]))
print("Theta3 = ",math.degrees(f(a,b,c,d,phi)[3]))
print("omega_BC = ",v(a,b,c,d,phi)[1]*omegaAB)
print("omega_CD = ",v(a,b,c,d,phi)[2]*omegaAB)

print()

print("A_CA = A_CD =",ac(a,b,c,d,phi,omegaAB,alphaAB)[2])
print("Ac_CB    =",ac(a,b,c,d,phi,omegaAB,alphaAB)[3])
print("At_CB    =",ac(a,b,c,d,phi,omegaAB,alphaAB)[4])
print("alpha_BC =",ac(a,b,c,d,phi,omegaAB,alphaAB)[4]/b)
print("A_CB     =",ac(a,b,c,d,phi,omegaAB,alphaAB)[5])
print("Ac_CD    =",ac(a,b,c,d,phi,omegaAB,alphaAB)[6])
print("At_CD    =",ac(a,b,c,d,phi,omegaAB,alphaAB)[7])
print("alpha_CD =",ac(a,b,c,d,phi,omegaAB,alphaAB)[7]/c)

#print(ve(a,b,c,d,phi))

