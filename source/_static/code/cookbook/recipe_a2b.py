from picodaq import *
import matplotlib.pyplot as plt

with AnalogIn(channels=[0, 1], rate=50*kHz) as ai:
    data, times = ai.read(200*ms, times=True)

plt.plot(times, data)
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
