#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals

import sys, math
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

qmax=[]
qmin=[]
inc=[]
omega=[]

filename = 'm1=1.50 m2=0.50 m3=0.50 a_in=1.00 e_in=0.60 e_out=0.50 inc_0-180'
plot_title = '$m_1=1.5$ $m_2=0.5$ $m_3=0.5$ $a_{in}=1$ $e_{in}=0.6$ $e_{out}=0.5$'

irange = 0
omegarange = 0
with open(filename+'.txt') as data_file:
    for line in data_file:
        if line.startswith('#'):
            continue
        if line.strip().startswith('Q_min'):
            irange += 1
            omegarange = 0
        elif float(line.split()[0]):
            omegarange += 1
print (irange, omegarange)
data_file = open (filename+'.txt')

m1,m2,m3,a_in,e_in,e_out = filename.split(' ')[:6]
m1 = float(m1[3:])
m2 = float(m2[3:])
m3 = float(m3[3:])
ein = float(e_in[5:])
eout = float(e_out[6:])
print (m1,m2,m3,ein,eout)



for line in data_file:
    if line.strip().startswith('Q_min') or line.startswith('#'):
        continue
    if ((float(line.split()[9]) < 0) or (float(line.split()[9]) > 360)):
        continue
    qmin=np.append(qmin, float(line.split()[0]))
    qmax=np.append(qmax, float(line.split()[1]))
    inc=np.append(inc, math.cos(float(line.split()[8])*math.pi/180))
    omega=np.append(omega, float(line.split()[9]))

lambd = 1
cosi =[]
line1 = []
line2 = []
line3 = []
line4 = []

for i in range(200):
    cos_i = (i-100)/100
    line = (lambd*math.sqrt(10000)/(1-eout))**(1/6)*((1-2/3*ein*(1-1/2*ein**2)-0.3*cos_i*(1-1/2*ein+2*cos_i*(1-5/2*ein**(3/2)-cos_i)))*(1+m3/(m1+m2)))**(1/3)
    line1.append(1.15*line)
    line2.append(1.45*line)
    line3.append(1.75*line)
    line4.append(2.00*line)
    cosi.append(cos_i)

qmin = np.reshape(qmin,(-1,omegarange))
qmax = np.reshape(qmax,(-1,omegarange))
inc = np.reshape(inc,(-1,omegarange))
omega = np.reshape(omega,(-1,omegarange))


fig1 = plt.figure()

ax = fig1.gca(projection='3d')
ax.set_title (plot_title)
surf2 = ax.plot_surface(inc, omega, qmax, cmap=cm.Spectral_r, linewidth=0.1, antialiased=True, shade=True, rstride=1, cstride=1,alpha=1.0, edgecolors = 'k')
ax.set_xlabel('$\cos \iota$')
ax.set_ylabel('$\Omega$')
ax.set_zlabel('Q')
plt.colorbar(surf2,shrink=0.7)

if sys.platform == 'win32':
    plt.get_current_fig_manager().window.setGeometry(10,50,1024,768)
else:
    plt.get_current_fig_manager().window.wm_geometry("1024x768+10+50")


fig2 = plt.figure()

ax = fig2.gca(projection='3d')
ax.set_title (plot_title)
surf1 = ax.plot_surface(inc, omega, qmax, cmap=cm.Greys, linewidth=0, antialiased=False, shade=True, rstride=1, cstride=1,)
ax.view_init(elev=89.9, azim=-90)
ax.set_xlabel('$\cos \iota$')
ax.set_ylabel('$\Omega$')
ax.set_zlabel('')
ax.set_zticks([])
ax.w_zaxis.line.set_lw(0.)
ax.grid(False)
ax.dist=7.5
ax.left=0
plt.colorbar(surf1,shrink=0.7)

if sys.platform == 'win32':
    plt.get_current_fig_manager().window.setGeometry(100,100,1024,768)
else:
    plt.get_current_fig_manager().window.wm_geometry("1024x768+100+100")


fig3 = plt.figure()
plt.title (plot_title)
imin=inc.min()
imax=inc.max()
omin=omega.min()
omax=omega.max()
xticks=np.arange(imin, imax, (imax-imin)/10)
yticks=np.arange(omin, omax, (omax-omin)/18)
extent=(imin,imax,omin,omax)
plt.imshow(qmin.transpose(), cmap=cm.Spectral_r, aspect=1/150,interpolation='sinc', extent=extent)
plt.xticks(xticks)
plt.yticks(yticks)
plt.colorbar()

if sys.platform == 'win32':
    plt.get_current_fig_manager().window.setGeometry(200,150,1024,768)
else:
    plt.get_current_fig_manager().window.wm_geometry("1024x768+200+150")

plt.show()

