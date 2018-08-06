
from matplotlib import pyplot as plt
import numpy as np
 
plt.axis([0, 1000, 0, 1])
plt.ion()
 
while True:
    x = []
    y = []
    for i in range(512):
        x.append(i)
        y.append(np.random.random())
        # plt.pause(0.05)
    plt.cla()
    plt.plot(x, y)

    plt.pause(0.033)
