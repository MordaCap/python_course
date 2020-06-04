#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import statistics as stat
import sys
import matplotlib.pyplot as plt

filenames = ['m1=1.00 m2=1.00 m3=0.10 a_in=1.00 e_in=0.99 e_out=0.50',
             'm1=1.00 m2=1.00 m3=1.00 a_in=1.00 e_in=0.99 e_out=0.50',
             'm1=1.00 m2=1.00 m3=10.00 a_in=1.00 e_in=0.99 e_out=0.50',
             'm1=1.50 m2=0.50 m3=0.10 a_in=1.00 e_in=0.99 e_out=0.50',
             'm1=1.50 m2=0.50 m3=1.00 a_in=1.00 e_in=0.99 e_out=0.50',
             'm1=1.50 m2=0.50 m3=10.00 a_in=1.00 e_in=0.99 e_out=0.50',
             'm1=1.90 m2=0.10 m3=0.10 a_in=1.00 e_in=0.99 e_out=0.50',
             'm1=1.90 m2=0.10 m3=1.00 a_in=1.00 e_in=0.99 e_out=0.50',
             'm1=1.90 m2=0.10 m3=10.00 a_in=1.00 e_in=0.99 e_out=0.50',
             'm1=1.00 m2=1.00 m3=0.10 a_in=1.00 e_in=0.75 e_out=0.50',
             'm1=1.00 m2=1.00 m3=1.00 a_in=1.00 e_in=0.75 e_out=0.50',
             'm1=1.00 m2=1.00 m3=10.00 a_in=1.00 e_in=0.75 e_out=0.50',
             'm1=1.50 m2=0.50 m3=0.10 a_in=1.00 e_in=0.75 e_out=0.50',
             'm1=1.50 m2=0.50 m3=1.00 a_in=1.00 e_in=0.75 e_out=0.50',
             'm1=1.50 m2=0.50 m3=10.00 a_in=1.00 e_in=0.75 e_out=0.50',
             'm1=1.90 m2=0.10 m3=0.10 a_in=1.00 e_in=0.75 e_out=0.50',
             'm1=1.90 m2=0.10 m3=1.00 a_in=1.00 e_in=0.75 e_out=0.50',
             'm1=1.90 m2=0.10 m3=10.00 a_in=1.00 e_in=0.75 e_out=0.50',
             'm1=1.00 m2=1.00 m3=0.10 a_in=1.00 e_in=0.50 e_out=0.50',
             'm1=1.00 m2=1.00 m3=1.00 a_in=1.00 e_in=0.50 e_out=0.50',
             'm1=1.00 m2=1.00 m3=10.00 a_in=1.00 e_in=0.50 e_out=0.50',
             'm1=1.50 m2=0.50 m3=0.10 a_in=1.00 e_in=0.50 e_out=0.50',
             'm1=1.50 m2=0.50 m3=1.00 a_in=1.00 e_in=0.50 e_out=0.50',
             'm1=1.50 m2=0.50 m3=10.00 a_in=1.00 e_in=0.50 e_out=0.50',
             'm1=1.90 m2=0.10 m3=0.10 a_in=1.00 e_in=0.50 e_out=0.50',
             'm1=1.90 m2=0.10 m3=1.00 a_in=1.00 e_in=0.50 e_out=0.50',
             'm1=1.90 m2=0.10 m3=10.00 a_in=1.00 e_in=0.50 e_out=0.50',
             'm1=1.00 m2=1.00 m3=0.10 a_in=1.00 e_in=0.25 e_out=0.50',
             'm1=1.00 m2=1.00 m3=1.00 a_in=1.00 e_in=0.25 e_out=0.50',
             'm1=1.00 m2=1.00 m3=10.00 a_in=1.00 e_in=0.25 e_out=0.50',
             'm1=1.50 m2=0.50 m3=0.10 a_in=1.00 e_in=0.25 e_out=0.50',
             'm1=1.50 m2=0.50 m3=1.00 a_in=1.00 e_in=0.25 e_out=0.50',
             'm1=1.50 m2=0.50 m3=10.00 a_in=1.00 e_in=0.25 e_out=0.50',
             'm1=1.90 m2=0.10 m3=0.10 a_in=1.00 e_in=0.25 e_out=0.50',
             'm1=1.90 m2=0.10 m3=1.00 a_in=1.00 e_in=0.25 e_out=0.50',
             'm1=1.90 m2=0.10 m3=10.00 a_in=1.00 e_in=0.25 e_out=0.50',
             'm1=1.00 m2=1.00 m3=0.10 a_in=1.00 e_in=0.00 e_out=0.50',
             'm1=1.00 m2=1.00 m3=1.00 a_in=1.00 e_in=0.00 e_out=0.50',
             'm1=1.00 m2=1.00 m3=10.00 a_in=1.00 e_in=0.00 e_out=0.50',
             'm1=1.50 m2=0.50 m3=0.10 a_in=1.00 e_in=0.00 e_out=0.50',
             'm1=1.50 m2=0.50 m3=1.00 a_in=1.00 e_in=0.00 e_out=0.50',
             'm1=1.50 m2=0.50 m3=10.00 a_in=1.00 e_in=0.00 e_out=0.50',
             'm1=1.90 m2=0.10 m3=0.10 a_in=1.00 e_in=0.00 e_out=0.50',
             'm1=1.90 m2=0.10 m3=1.00 a_in=1.00 e_in=0.00 e_out=0.50',
             'm1=1.90 m2=0.10 m3=10.00 a_in=1.00 e_in=0.00 e_out=0.50']
A = []
for filename in filenames:
    qmax = []
    qmin = []
    inc = []
    i_q_o = []
    omega = []
    irange = 0
    omegarange = 0
    with open(filename + '.txt') as data_file:
        for line in data_file:
            if line.startswith('#'):
                continue
            if line.strip().startswith('Q_min'):
                irange += 1
                omegarange = 0
            elif float(line.split()[0]):
                omegarange += 1
    data_file = open(filename + '.txt')

    m1, m2, m3, a_in, e_in, e_out = filename.split(' ')[:6]
    m1 = float(m1[3:])
    m2 = float(m2[3:])
    m3 = float(m3[3:])
    ein = float(e_in[5:])
    eout = float(e_out[6:])
    for line in data_file:
        if line.strip().startswith('Q_min') or line.startswith('#'):
            continue
        i_q_o.append((math.cos(float(line.split()[8]) * math.pi / 180), float(line.split()[1]), float(line.split()[9])))
    for cos_i, q, o in i_q_o:
        line = (1*math.sqrt(10000)/(1 - eout))**(1/6)*((1 - 2/3*ein*(1 - 1/2*ein**2) - 0.3*cos_i*(1 - 1/2*ein + 2*cos_i*(1 - 5/2*ein**(3/2) - cos_i)))*(1 + m3/(m1 + m2)))**(1/3)
        A.append(q/line)

print (len(A))
print('mean {:.3f}'.format(stat.mean(A)))
print('median {:.3f}'.format(stat.median(A)))
print('stdev {:.3f}'.format(stat.stdev(A)))
print('pstdev {:.3f}'.format(stat.pstdev(A)))
print('median_high {:.3f}'.format(stat.median_high(A)))
print('median_low {:.3f}'.format(stat.median_low(A)))

plt.rc('font',**{'family':'serif', 'size': 13, 'weight':'bold'})
plt.rc('text', usetex=True)
plt.title(r"Histogram of $A_{max}$ parameter over all $e_{in} = 0, 0.25, 0.5, 0.75, 0.99$")
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.hist(A, bins=50)
plt.show()
