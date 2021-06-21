import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
def angle(tup):
    tanAngle = None
    if tup[0] == 0.0:
        if tup[1] > 0:
            tanAngle = np.pi / 2
        elif tup[1] < 0:
            tanAngle = - np.pi / 2
        else:
            return np.nan

    else:
        tanAngle = np.arctan(float(tup[1] / tup[0]))

    if tanAngle > 0:
        if tup[0] >= 0:
            return tanAngle
        else:
            return tanAngle + np.pi
    elif tanAngle < 0:
        if tup[1] < 0:
            return tanAngle + 2 * np.pi
        else:
            return tanAngle + np.pi
    else:
        return 0.0

xspace = np.linspace(-np.pi,+np.pi,1000)
yspace = []
for x in xspace:
    piv = (np.cos(x), np.sin(x))
    tans = angle(piv)
    yspace.append(tans)

yspace_atan2 = []
for  x in xspace:
    piv = (np.cos(x), np.sin(x))
    tans = np.arctan2(np.cos(x), np.sin(x))
    yspace_atan2.append(tans)

yspace_atan = []
for x in xspace:
    piv = (np.cos(x), np.sin(x))
    tans = np.arctan(piv[0]/piv[1])
    yspace_atan.append(tans)


plt.plot(xspace,yspace)
plt.plot(xspace, yspace_atan2)
plt.plot(xspace, yspace_atan)
plt.plot(xspace, xspace)
plt.plot(xspace, xspace + np.pi*2)
plt.show()


