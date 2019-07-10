# I wrote a kind of function to simulate Leetcode 887(drop egg problem) dynamic program.
def superEggDrop1(K, N):
    dp = [0] * (K + 1)
    m = 0
    while dp[K] < N:
        for k in range(K, 0, -1):
            dp[k] = dp[k - 1] + dp[k] + 1
        m += 1
    return m

import numpy as np 
from matplotlib import pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D 
import math

K=np.arange(1,100)
N=np.arange(1,100)
n1=np.zeros((100,100))
n2=np.zeros((100,100))

for i in range(0,99):
    for j in range(0,99):
        n1[i,j]=superEggDrop1(K[i],N[j])

for i in range(0,99):
    for j in range(0,99):
        b0=N[j]-K[i]
        if b0<=2:
            b0=2
        n2[i,j]=math.floor(1+math.log2(b0))

        

K,N= np.meshgrid(range(100),range(100))
fig = plt.figure()
ax = Axes3D(fig)
ax.set_title("demonstrate of fomulation(black) and dynamic programing(yellow)") 
ax.set_xlabel("K axis caption") 
ax.set_ylabel("N axis caption") 
ax.set_zlabel("n axis caption") 
ax.scatter(K, N, n1,c='y')


ax.scatter(K,N,n2,c='black')

plt.show()

