from picodaq import *
import matplotlib.pyplot as plt

with AnalogIn(channels=[0, 1], rate=50*kHz) as ai:
    data = ai.read(200*ms)

plt.plot(data)
plt.xlabel('Sample #')
plt.ylabel('Voltage (V)')
