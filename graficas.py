import matplotlib.pyplot as plt
import math as m

X = []
Y = []

n = 100
inc = 720 / n

vx = 0
for i in range(n):
    X.append((vx * m.pi) / 180 )
    vx = vx + inc
    
for i in range(n):
    Y.append(m.sin(X[i]))
    
print(X)
print(Y)

plt.plot(X, Y, "g-", X, Y, "r*")
plt.show()
