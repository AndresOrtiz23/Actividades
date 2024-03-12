import math
def cin_inv(x,y,z):
    a1=1
    a2=1
    a3=1
    r2=z-a1
    r1=math.sqrt((x**2)+(y**2))
    th1=math.atan2(y,x)
    b2=math.atan2(r2,r1)
    r3=math.sqrt((r1**2)+(r2**2))
    b1=math.acos(((a3**2)-(a2**2)-(r3**2))/(-2*a3*r3))
    th2=b2-b1
    b3=math.acos(((r3**2)-(a2**2)-(a3**2))/(-2*a2*a3))
    th3=180-b3
    return th1,th2,th3
