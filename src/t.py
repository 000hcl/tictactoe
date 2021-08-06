import numpy as np
"""
s = np.array([0,0,0])
b = np.copy(s)
b[0] = 1

print(s,b)
"""

a = [0,0,0]
c = a.copy()

print(a,c)

s = [0 for _ in range(100)]
#s = np.array([0 for _ in range(100)])

for j in range(20):
    for i in range(1000000):
        
        #f = s[1]+s[2]+s[3]+s[4]+s[5]
        f = sum(s[1:6])

        #f = 0
        #for i in range(5):
        #    f+=s[i]
        #s[1] = 2

print(1)