import tifffile as tf
import numpy as np
from scipy import integrate
from scipy import special


def benchmark_ellipsoid(res):
    side = np.int_(res*np.ones(3))
    side[np.mod(side, 2) == 0] += 1
    midVoxel = (side - 1)//2
    axes = np.int_(0.9*np.array([1, 0.75, 0.5])*midVoxel)
    l, h, w = side

    voxel = np.empty(side)


    white = 2**16-1
    black = 0
    def inEllipsoid(pos):
        dist = (1/axes**2)@(pos - midVoxel)**2
        if dist > 1.0:
            return black
        else:
            return white

    for i in range(l):
        for j in range(h):
            for k in range(w):
                voxel[i,j,k] = inEllipsoid(np.array([i,j,k]))
    voxel = np.uint16(voxel)
    tf.imwrite("ellipsoid_"+str(l)+".tif", voxel, photometric='minisblack')
    filename = "ellipsoid_"+str(l)+".tif"
    return filename


def theoretisch(res):

# Abmessung Definition
    side = np.int_(res*np.ones(3))
    side[np.mod(side, 2) == 0] += 1
    midVoxel = (side - 1)//2
    axes = np.int_(0.9*np.array([1, 0.75, 0.5])*midVoxel)
    a=float(axes[0])
    b=float(axes[1])
    c=float(axes[2])
#Berechnung über w000
    w000=4*np.pi*a*b*c/3
#Berechnung über w102
    alpha= np.square(c)/np.square(a)
    beta= np.square(c)/np.square(b)
    fi= np.arccos(c/a)
    m=(1-beta)/(1-alpha)
    # def f(x):
    #     return 1 / np.sqrt(1-np.square(np.sin(x)*np.sin(alpha)))
    # F=integrate.quad(f, 0, fi)[0]
    # def e(x):
    #     return np.sqrt(1-np.square(np.sin(x)*np.sin(alpha)))
    # E=integrate.quad(e, 0, fi)[0]

    F=special.ellipkinc(fi,m)
    E=special.ellipeinc(fi,m)
    w11102=2*np.pi/3*np.square(c)*alpha*((-1)/(beta-alpha)+ 1/np.sqrt(alpha*beta*(1-alpha))*(F+alpha/(beta-alpha)*E))
    w12202=2*np.pi/3*np.square(c)*beta*(1/(beta-alpha)+ 1/(np.sqrt(alpha*beta*(1-alpha))*(1-beta))*(F-beta/(1-m)*E))
    w13302=2*np.pi/3*np.square(c)/(np.sqrt(alpha*beta*(1-alpha))*(1-beta))*(E-beta*F)

    e1=np.array([1,0,0])
    e2=np.array([0,1,0])
    e3=np.array([0,0,1])
    w102=w11102*e1+w12202*e2+w13302*e3

# Berechnung über w100
    w100=2*np.pi/3*np.square(c)*(1 + 1/np.sqrt(alpha*beta*(1-alpha))*(alpha*F+(1-alpha)*E))

# Berechnung über w202
    alpha2 = np.square(a) / np.square(c)
    beta2 = np.square(b) / np.square(c)
    m2 = (alpha2 - beta2) / (alpha2-1)

    w21102=np.pi/3*c*(beta2/(np.sqrt(alpha2*beta2)) + (alpha2*beta2+alpha2-beta2) / ((alpha2-beta2)*np.sqrt(alpha2-1))*(F-E))
    w22202=np.pi/3*c/(beta2-1)*(-1*beta2/(np.sqrt(alpha2*beta2)) + (alpha2-beta2-alpha2*beta2) / (m2*np.sqrt(alpha2-1))*((1-m2)*F-E))
    w23302=np.pi/3*c/(beta2-1)*(np.square(beta2)/(np.sqrt(alpha2*beta2)) + (alpha2*beta2-alpha2-beta2) / (np.sqrt(alpha2-1))*E)

    w202=w21102*e1+w22202*e2+w23302*e3

# Berechnung über w200
    w200=2*np.pi/3*c*(beta2/np.sqrt(alpha2*beta2)+1/np.sqrt(alpha2-1)*(F+(alpha2-1)*E))
# Berechnung über w300
    w300=4*np.pi/3
# als txt speichern
    with open("w000.txt", "w") as m:
        m.write(str(w000))
    with open("w100.txt", "w") as m:
        m.write(str(w100))
    with open("w200.txt", "w") as m:
        m.write(str(w200))
    with open("w300.txt", "w") as m:
        m.write(str(w300))
    np.savetxt("w102.txt",w102)
    np.savetxt("w202.txt",w202)


res = input("please input the resolution for Ellipsoid (Example:51, 101 or 151): ")
res = int(res)
tifffile =benchmark_ellipsoid(res)
print("create Ellipsoid successfully!")
print("Tiff-File name is :", tifffile)
theoretisch(res)
print("The theoretical MT are calculated!")
    