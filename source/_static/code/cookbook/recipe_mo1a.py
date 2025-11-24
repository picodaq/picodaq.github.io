from picodaq import *
from picodaq.stimulus import Triangle, TTL, Train
import matplotlib.pyplot as plt
import numpy as np

fs = 10 * kHz
apulse = Triangle(duration=50*ms, amplitude=1*V)
atrain = Train(apulse, pulseperiod=100*ms, pulsecount=9)
dpulse = TTL(duration=20*ms)
dtrain = Train(dpulse, pulseperiod=200*ms, pulsecount=5)

aplandata, att = mockstim(atrain, rate=fs, times=True)
dplandata, dtt = mockstim(dtrain, rate=fs, times=True)

plt.plot(att, aplandata)
plt.plot(dtt, -1.5 + .3*dplandata)
plt.xlabel('Time (s)')
plt.ylabel('Planned logic / voltage (V)')
plt.yticks([-1.5, -1.2, -1, 0, 1], ['Lo', 'Hi', -1, 0, 1])
