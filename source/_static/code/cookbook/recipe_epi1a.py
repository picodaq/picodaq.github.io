from picodaq import *
import matplotlib.pyplot as plt
import numpy as np

data = []
K = 20
with AnalogIn(channel=0, rate=100*kHz) as ai:
    ai.episodic(duration=20*ms, period=100*ms)
    for k in range(K):
        data.append(ai.read())
data = np.stack(data, 1)
                    
plt.plot(data)
plt.xlabel('Sample #')
plt.ylabel('Voltage (V)')
