import matplotlib.pyplot as plt
import numpy as np
import math
#For equation (2 -4)x=-24
a = [-12,0.0]
b = [0,6]
#For equation (2 3)x=11
c = [11/2,0.0]
d = [0,11/3]
#For equation (-1 -1)x=-3
e = [3,0.0]
f = [0,3]
head_length = 0.7

dx1 = b[0] - a[0]
dy1 = b[1] - a[1]
dx2 = d[0] - c[0]
dy2 = d[1] - c[1]
dx3 = f[0] - e[0]
dy3 = f[1] - e[1]

vec_ab = [dx1,dy1]
vec_cd = [dx2,dy2]
vec_ef = [dx3,dy3]

vec_ab_magnitude = math.sqrt(dx1**2+dy1**2)
vec_cd_magnitude = math.sqrt(dx2**2+dy2**2)
vec_ef_magnitude = math.sqrt(dx3**2+dy3**2)

dx1 = dx1 / vec_ab_magnitude
dy1 = dy1 / vec_ab_magnitude
vec_ab_magnitude = vec_ab_magnitude - head_length
dx2 = dx2 / vec_cd_magnitude
dy2 = dy2 / vec_cd_magnitude
vec_cd_magnitude = vec_cd_magnitude - head_length
dx3 = dx3 / vec_ef_magnitude
dy3 = dy3 / vec_ef_magnitude
vec_ef_magnitude = vec_ef_magnitude - head_length
ax = plt.axes()

ax.arrow(a[0], a[1], vec_ab_magnitude*dx1, vec_ab_magnitude*dy1, head_width=0.5, head_length=0.7, fc='lightblue', ec='black', label='equation (2 -4)x=-24')
ax.arrow(c[0], c[1], vec_ab_magnitude*dx2, vec_ab_magnitude*dy2, head_width=0.5, head_length=0.7, fc='lightblue', ec='blue',label='equation (2 3)x=-11')
ax.arrow(e[0], e[1], vec_ab_magnitude*dx3, vec_ab_magnitude*dy3, head_width=0.5, head_length=0.7, fc='lightblue', ec='green',label='equation (-1 -1)x=-3')
plt.scatter(a[0],a[1],color='black')
plt.scatter(b[0],b[1],color='black')
plt.scatter(c[0],c[1],color='blue')
plt.scatter(d[0],d[1],color='blue')
plt.scatter(e[0],e[1],color='green')
plt.scatter(f[0],f[1],color='green')
ax.annotate('equation (2 -4)x=-24', xy=(0,6),  xycoords='data',
            xytext=(0.6, 0.5), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top',
            )
ax.annotate('equation (2 3)x=-11', xy=(11/3,0),  xycoords='data',
            xytext=(0.9, 0.65), textcoords='axes fraction',
            arrowprops=dict(facecolor='blue', shrink=0.05),
            horizontalalignment='right', verticalalignment='top',
            )
ax.annotate('equation (-1 -1)x=-3', xy=(3,0),  xycoords='data',
            xytext=(0.3,0.25), textcoords='axes fraction',
            arrowprops=dict(facecolor='green', shrink=0.05),
            horizontalalignment='right', verticalalignment='top',
            )
ax.annotate('Unique Solution', xy=(-2,5),  xycoords='data',
            xytext=(0.8,0.95), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top',
            )
plt.grid()
plt.xlim(-13,10)
plt.ylim(-5,10)
plt.show()
#plt.close()
