import matplotlib.pyplot as plt
import numpy as np
import math
from coeffs import *

n1 = np.array([2,3])
n2 = np.array([2,-4]) 
n3 = np.array([-1,-1]) 
c =  np.array([11,-24]) 

#Intercepts
A1,B1 =  line_icepts(n1,c[0])
A2,B2 =  line_icepts(n2,c[1])


#Matrix Ranks
N=np.vstack((n1,n2))
M =np.vstack((N.T, c)).T
rank_N = np.linalg.matrix_rank(N)
rank_M = np.linalg.matrix_rank(M)
m,n = np.shape(N)
print(rank_M, rank_N, M)

#Checking for solution for two equations (2 3)x=11 and (2 -4)=-24
if rank_N==rank_M:
	if rank_N == m:
		print("Unique Solution Exists")
	else:
		print("Infinite Number of Solutions")
else:
	print("No solution")

print("\nunique solution will be the intersection point of two lines represented by equations")
#line_intersect
x=np.array([line_intersect(n1,c[0],n2,c[1])]);
print(x)
A3,B3 = line_icepts(n3,-3)
c =  np.array([-24,-3]) 
#Matrix Ranks
N=np.vstack((n2,n3))
M =np.vstack((N.T, c)).T
rank_N = np.linalg.matrix_rank(N)
rank_M = np.linalg.matrix_rank(M)
m,n = np.shape(N)
print(rank_M, rank_N, M)

#Checking for solution for two equations (-1 -1)x=-3 and (2 -4)=-24
if rank_N==rank_M:
	if rank_N == m:
		print("Unique Solution Exists:",np.linalg.inv(N)@c)
	else:
		print("Infinite Number of Solutions")
else:
	print("No solution")
c =  np.array([11,-3])
#Matrix Ranks
N=np.vstack((n1,n3))
M =np.vstack((N.T, c)).T
rank_N = np.linalg.matrix_rank(N)
rank_M = np.linalg.matrix_rank(M)
m,n = np.shape(N)
print(rank_M, rank_N, M)

#Checking for solution for two equations (-1 -1)x=-3 and (2 3)=11
if rank_N==rank_M:
	if rank_N == m:
		print("Unique Solution Exists:",np.linalg.inv(N)@c)
	else:
		print("Infinite Number of Solutions")
else:
	print("No solution")

head_length = 0.7

dx1 = B2[0] - A2[0]
dy1 = B2[1] - A2[1]
dx2 = B1[0] - A1[0]
dy2 = B1[1] - A1[1]
dx3 = B3[0] - A3[0]
dy3 = B3[1] - A3[1]

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

ax.arrow(A2[0], A2[1], vec_ab_magnitude*dx1, vec_ab_magnitude*dy1, head_width=0.5, head_length=0.7, fc='lightblue', ec='black', label='equation (2 -4)x=-24')
ax.arrow(A1[0], A1[1], vec_ab_magnitude*dx2, vec_ab_magnitude*dy2, head_width=0.5, head_length=0.7, fc='lightblue', ec='blue',label='equation (2 3)x=-11')
ax.arrow(A3[0], A3[1], vec_ab_magnitude*dx3, vec_ab_magnitude*dy3, head_width=0.5, head_length=0.7, fc='lightblue', ec='green',label='equation (-1 -1)x=-3')
plt.scatter(A2[0], A2[1],color='black')
plt.scatter(B2[0],B2[1],color='black')
plt.scatter(A1[0],A1[1],color='blue')
plt.scatter(B1[0],B1[1],color='blue')
plt.scatter(A3[0],A3[1],color='green')
plt.scatter(B3[0],B3[1],color='green')
ax.annotate('equation (2 -4)x=-24', xy=(-8,2),  xycoords='data',
            xytext=(0.6, 0.5), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top',
            )
ax.annotate('equation (2 3)x=-11', xy=(4,1),  xycoords='data',
            xytext=(0.9, 0.65), textcoords='axes fraction',
            arrowprops=dict(facecolor='blue', shrink=0.05),
            horizontalalignment='right', verticalalignment='top',
            )
ax.annotate('equation (-1 -1)x=-3', xy=(1,2),  xycoords='data',
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
