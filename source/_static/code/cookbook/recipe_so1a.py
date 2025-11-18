from picodaq import *
from scipy.signal import sweep_poly
import matplotlib.pyplot as plt
import numpy as np

f0 = 10 * Hz
f1 = 100 * Hz
dur = 1 * s
fs = 10 * kHz

tt_s = np.arange(0, dur.as_('s'), (1/fs).as_('s'))
poly = [(f1-f0).as_('Hz') / dur.as_('s'), f0.as_('Hz')]
vv = sweep_poly(tt_s, poly, phi=-90)

plt.plot(tt_s, vv)
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
