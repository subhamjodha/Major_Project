import numpy as np
P = np.genfromtxt('Training/Perdiction.csv', delimiter=',')
P[0]=1.0
print P[0]
